from os import environ


def register_environ(app):
    env = environ.get("FLASK_ENV")

    if env == "production":
        app.config.from_object("app.config.production.ProductionConfig")
    else:
        app.config.from_object("app.config.development.DevelopmentConfig")
