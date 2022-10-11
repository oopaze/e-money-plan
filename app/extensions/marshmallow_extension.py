from flask_marshmallow import Marshmallow

marshmallow = Marshmallow()


def register_marshmallow(app):
    marshmallow.init_app(app)
    app.marshmallow = marshmallow
