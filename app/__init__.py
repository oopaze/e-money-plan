from flask import Flask

from .extensions import register_extensions


def create_app():
    app = Flask(__name__)

    register_extensions(app)

    return app
