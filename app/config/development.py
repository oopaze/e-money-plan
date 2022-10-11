from . import BaseConfig


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BaseConfig.BASE_DIR}/dev-storage.db"
