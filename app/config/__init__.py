from os import environ
from pathlib import Path


class BaseConfig:
    SECRET_KEY = environ.get("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JSON_SORT_KEYS = False
    BASE_DIR = Path(__name__).resolve().parent
