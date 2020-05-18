import os


class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:docker@192.168.0.154:32769/event_planning'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
