# coding: utf8

from flask import Flask
# Import the fixer
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.DevConfig')

# Now we can access the configuration variables via app.config["VAR_NAME"].

# Use the fixer
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/')
def index():
    return "Hello World!"
