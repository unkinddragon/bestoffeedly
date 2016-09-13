import os

DEBUG = True
SECRET_KEY = 'top secret!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(os.path.dirname(__file__), 'data.sqlite3')
SQLALCHEMY_TRACK_MODIFICATIONS = False