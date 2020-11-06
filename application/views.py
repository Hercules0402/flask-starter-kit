# coding utf8
from flask import current_app


@current_app.route('/')
def index():
    return 'Index page'