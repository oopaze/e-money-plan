from flask import Blueprint

from .controllers.create_expense import create_expense_bp
from .controllers.delete_expense import delete_expense_bp
from .controllers.list_expensies import list_expensies_bp
from .controllers.show_expense import show_expense_bp
from .controllers.update_expense import update_expense_bp

expense_routes = Blueprint("expenses", __name__, url_prefix="/expense")
expense_routes.register_blueprint(create_expense_bp)
expense_routes.register_blueprint(list_expensies_bp)
expense_routes.register_blueprint(update_expense_bp)
expense_routes.register_blueprint(show_expense_bp)
expense_routes.register_blueprint(delete_expense_bp)
