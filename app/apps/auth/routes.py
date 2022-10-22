from flask import Blueprint

from .controllers.login import login_bp
from .controllers.refresh import refresh_bp

auth_routes = Blueprint("auth", __name__, url_prefix="/auth")
auth_routes.register_blueprint(login_bp)
auth_routes.register_blueprint(refresh_bp)
