from os import environ

from ..config import BaseConfig


class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = environ.get("DATABASE_URL")
