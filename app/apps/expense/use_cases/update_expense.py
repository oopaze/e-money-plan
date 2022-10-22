from ....common.utils.response import error_response, success_response
from ....common.utils.use_case import UseCase
from ..repositories.expense import ExpenseRepository


class UpdateExpenseUseCase(UseCase):
    def execute(self, payload, id):
        if errors := self.validation_schema.validate(payload):
            return error_response(errors)
        return self.handle_success(payload, id)

    def set_repository(self, repository):
        self.repository: ExpenseRepository = repository

    def handle_success(self, payload, id):
        instance = self.repository.update(id, payload)
        dumped_instance = self.output_schema.dump(instance)
        return success_response(dumped_instance, "expense", 201)
