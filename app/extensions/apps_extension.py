from flask import Flask

from ..apps.profile.routes import profile_routes


def register_apps(app: Flask):
    app.register_blueprint(profile_routes)
