from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class DeleteExpenseUseCase(UseCase):
    def execute(self, id):
        self.repository.delete(id)
        return success_response("Despesa deleted successfuly", "message", 204)
