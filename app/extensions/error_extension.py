from flask import Flask
from sqlalchemy.exc import NoResultFound

from ..common.errors import error_400, error_404, error_500
from ..common.exceptions import DoesNotExist


def register_errors(app: Flask):
    app.register_error_handler(404, error_404)
    app.register_error_handler(DoesNotExist, error_404)
    app.register_error_handler(NoResultFound, error_404)
    app.register_error_handler(500, error_500)
    app.register_error_handler(400, error_400)
