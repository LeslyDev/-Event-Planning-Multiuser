from app import app, db, bcrypt, login_manager
from flask import render_template, request, redirect

from flask_login import login_user, logout_user, login_required

from app.models import Author, Task
from app.forms import TaskForm, AuthorForm, LoginForm

from datetime import datetime


@login_manager.user_loader
def user_loader(user_id):
    return Author.query.get(user_id)


@app.route("/")
@login_required
def index():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        user = Author.query.get(name)
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                user.authenticated = True
                db.session.add(user)
                db.session.commit()
                login_user(user, remember=True)
                return redirect("/")
    return render_template("login.html", form=form)


@app.route("/create_user", methods=["GET", "POST"])
def create_user():
    form = AuthorForm()
    if form.validate_on_submit():
        name = request.form.get('name')
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        password = request.form.get('password')
        user = Author(
            name=name,
            lastname=lastname,
            email=email,
            password=bcrypt.generate_password_hash(password).decode('utf-8')
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/")
    return render_template('create_user.html', form=form)


@app.route('/logout/<name>')
@login_required
def logout(name):
    user = Author.query.get(name)
    user.authenticated = False
    db.session.add(user)
    db.session.commit()
    logout_user()
    return redirect("/")


@app.route('/admin')
@login_required
def admin():
    return render_template('admin.html')


@app.route('/change_user_data/<name>', methods=['GET', 'POST'])
@login_required
def change_user_data(name):
    user = Author.query.get(name)
    form = AuthorForm()
    method = request.form.get('_method')
    if method == 'PATCH':
        lastname = request.form.get('lastname')
        email = request.form.get('email')
        user.lastname = lastname
        user.email = email
        db.session.add(user)
        db.session.commit()
        return redirect('/admin')
    return render_template('change_user_data.html', user=user, form=form)


@app.route('/author_data/<name>')
@login_required
def author_data(name):
    author = Author.query.get(name)
    return render_template('author_info.html', author=author)


@app.route('/tasks')
@login_required
def tasks():
    tasks = Task.query.all()
    return render_template('tasks_list.html', tasks=tasks)


@app.route('/tasks/<name>')
@login_required
def author_tasks(name):
    tasks = Task.query.filter(Task.author_name == name)
    return render_template('tasks_list.html', tasks=tasks)


@app.route('/create_task', methods=["GET", "POST"])
@login_required
def create_task():
    form = TaskForm()
    if form.validate_on_submit():
        title = request.form.get('title')
        body = request.form.get('description')
        start = request.form.get('start_time')
        end = request.form.get('end_time')
        author_name = request.form.get('author_name')
        task = Task(
            title=title,
            body=body,
            start=datetime.strptime(start, '%H:%M %d.%m.%Y'),
            end=datetime.strptime(end, '%H:%M %d.%m.%Y'),
            author_name=author_name
        )
        db.session.add(task)
        db.session.commit()
        return redirect(f'/tasks/{author_name}')
    return render_template('create_task.html', form=form)


@app.route('/task_data/<id>')
@login_required
def task_data(id):
    task = Task.query.get(id)
    return render_template('task_data.html', task=task)


@app.route('/change_task_data/<id>', methods=['GET', 'POST'])
@login_required
def change_task_data(id):
    task = Task.query.get(id)
    form = TaskForm()
    method = request.form.get('_method')
    if method == 'PATCH':
        body = request.form.get('description')
        start = request.form.get('start_time')
        end = request.form.get('end_time')
        task.body = body
        task.end = datetime.strptime(start, '%H:%M %d.%m.%Y')
        task.end = datetime.strptime(end, '%H:%M %d.%m.%Y')
        db.session.add(task)
        db.session.commit()
        return redirect(f'/task_data/{task._id}')
    return render_template('change_task_data.html', task=task, form=form)


@app.route('/delete_task/<id>')
@login_required
def delete_task(id):
    task = Task.query.get(id)
    author = task.author_name
    db.session.delete(task)
    db.session.commit()
    return redirect(f'/tasks/{author}')
