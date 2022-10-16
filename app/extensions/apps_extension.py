from flask import Flask

from ..apps.expense.routes import expense_routes
from ..apps.profile.routes import profile_routes


def register_apps(app: Flask):
    app.register_blueprint(profile_routes)
    app.register_blueprint(expense_routes)
