from ..config import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{BaseConfig.BASE_DIR}/storage.db"
