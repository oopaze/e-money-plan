from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def register_database(app):
    db.init_app(app)
    app.db = db
