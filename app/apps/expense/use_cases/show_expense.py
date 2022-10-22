from flask_jwt_extended import get_jwt_identity

from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase
from ..repositories.expense import ExpenseRepository


class ShowExpenseUseCase(UseCase):
    def set_repository(self, repository):
        self.repository: ExpenseRepository = repository

    def execute(self, id):
        instance = self.repository.get_expense(id, get_jwt_identity())
        dumped_instance = self.output_schema.dump(instance)
        return success_response(dumped_instance, "expense")
