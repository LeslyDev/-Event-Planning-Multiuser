from app import db
from datetime import datetime


class Task(db.Model):
    _id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text, nullable=False)
    start = db.Column(db.DateTime, default=datetime.now())
    end = db.Column(db.DateTime)
    author_name = db.Column(db.String, db.ForeignKey('author.name'), nullable=False)
