from flask_jwt_extended import get_jwt_identity

from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class DeleteExpenseUseCase(UseCase):
    def execute(self, id):
        self.repository.delete(id, get_jwt_identity())
        return success_response("Despesa deleted successfuly", "message", 204)
