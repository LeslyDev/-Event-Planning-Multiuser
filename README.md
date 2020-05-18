# -Event-Planning-Multiuser
Implemented multi-user event planning service with deploy to Heroku on Flask

docker run --rm --name flask-db -e POSTGRES_PASSWORD=docker -d -p 5432:5432 postgres:12-alpine

docker exec -it flask-db psql -U postgres -c "create database event_planning"

git clone https://github.com/LeslyDev/-Event-Planning-Multiuser.git

cd -Event-Planning-Multiuser

pip install -r requirements.txt

export FLASK_APP=app.py

export DATABASE_URL=postgresql://postgres:docker@localhost:5432/event_planning

flask db upgrade

gunicorn -w 4 -b 127.0.0.1:5000 app:app
