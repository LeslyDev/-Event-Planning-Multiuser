from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField
from wtforms.fields.html5 import EmailField, DateTimeField, DateTimeLocalField
from wtforms.validators import DataRequired, Email
# from datetime import datetime


class LoginForm(FlaskForm):
    name = StringField('Name')
    password = PasswordField('Password', validators=[DataRequired()])


class AuthorForm(FlaskForm):
    name = StringField('Имя')
    lastname = StringField('Фамилия')
    email = EmailField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])


class TaskForm(FlaskForm):
    title = StringField('title')
    description = TextAreaField('description')
    start_time = DateTimeField('End time', format='%H:%M %d.%m.%Y', validators=[DataRequired()])
    end_time = DateTimeField('End time', format='%H:%M %d.%m.%Y', validators=[DataRequired()])
