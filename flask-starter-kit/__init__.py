# coding: utf8

from flask import Flask
# Import the fixer
from werkzeug.contrib.fixers import ProxyFix


def create_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object('config.DevConfig')

    # Use the fixer
    app.wsgi_app = ProxyFix(app.wsgi_app)

    with app.app_context():
        return app
