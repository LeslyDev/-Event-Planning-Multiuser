from app import db
from flask_login import UserMixin


class Author(db.Model, UserMixin):
    name = db.Column(db.String(50), primary_key=True)
    lastname = db.Column(db.String(50), nullable=True)
    email = db.Column(db.String(50))
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)
    task = db.relationship('Task', backref='author', lazy='dynamic')

    def get_id(self):
        return self.name

    def is_authenticated(self):
        return self.authenticated
