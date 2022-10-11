from flask_migrate import Migrate

migrate = Migrate()


def register_migrate(app, db):
    migrate.init_app(app, db)
    app.migrate = migrate
