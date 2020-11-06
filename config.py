# coding: utf8


"""Flask config."""
import re
from os import environ, path, urandom
from dotenv import load_dotenv

basedir = path.abspath(path.dirname(__file__))
load_dotenv(path.join(basedir, '.env'))


class Config:
    """Base config."""
    SECRET_KEY = environ.get('SECRET_KEY') or urandom(16)
    FLASK_APP = 'flask-starter-kit'
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'


class StagConfig(Config):
    FLASK_ENV = 'staging'
    DEBUG = False
    TESTING = True


class ProdConfig(Config):
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False


class DevConfig(Config):
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True
