from .apps_extension import register_apps
from .database_extension import register_database
from .environ_extension import register_environ
from .error_extension import register_errors
from .marshmallow_extension import register_marshmallow
from .migration_extension import register_migrate


def register_extensions(app):
    register_environ(app)
    register_marshmallow(app)
    register_database(app)
    register_migrate(app, app.db)
    register_apps(app)
    register_errors(app)
