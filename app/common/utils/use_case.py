from abc import ABC, abstractmethod

from marshmallow import Schema
from marshmallow_sqlalchemy import SQLAlchemyAutoSchema

from ..utils.repository import Repository


class UseCase(ABC):
    def __init__(self, repository, output_schema=None, validation_schema=None):
        self.repository: Repository = repository
        self.output_schema: SQLAlchemyAutoSchema = output_schema
        self.validation_schema: Schema = validation_schema

    @abstractmethod
    def execute(self, payload=None, id=None):
        raise NotImplementedError("'handle' should be implemented")
