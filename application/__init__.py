# coding: utf8
import os
from flask import Flask
from werkzeug.contrib.fixers import ProxyFix


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object('config.DevConfig')

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Use the fixer
    app.wsgi_app = ProxyFix(app.wsgi_app)

    with app.app_context():
        # Include our Routes
        from . import views

        return app
