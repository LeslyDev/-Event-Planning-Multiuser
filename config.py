import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:docker@localhost:32769/event_planning'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
