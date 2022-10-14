from flask import Blueprint

from .controllers.create_profile import create_profile_bp
from .controllers.delete_profile import delete_profile_bp
from .controllers.show_profile import show_profile_bp
from .controllers.update_profile import update_profile_bp

profile_routes = Blueprint("profile", __name__, url_prefix="/profile")
profile_routes.register_blueprint(create_profile_bp)
profile_routes.register_blueprint(show_profile_bp)
profile_routes.register_blueprint(update_profile_bp)
profile_routes.register_blueprint(delete_profile_bp)
