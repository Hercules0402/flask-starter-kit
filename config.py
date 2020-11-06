# coding: utf8


"""Flask config."""
from os import environ, path
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY')
    FLASK_APP = 'flask-starter-kit'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class StagConfig(Config):
    ENV = 'staging'
    FLASK_ENV = 'staging'
    DEBUG = False
    TESTING = True


class ProdConfig(Config):
    ENV = 'production'
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    ENV = 'development'
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
