import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'lCmYHJtjOJQDLUHHIH0w5mOcXXmztmg3'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
