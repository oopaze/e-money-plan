from flask_jwt_extended import JWTManager

jwt = JWTManager()


def register_jwt(app):
    jwt.init_app(app)
