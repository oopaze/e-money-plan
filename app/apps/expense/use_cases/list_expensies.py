from flask_jwt_extended import get_jwt_identity

from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class ListExpensiesUseCase(UseCase):
    def execute(self, payload=None, id=None):
        instances = self.repository.get_all_expenses_from_profile(get_jwt_identity())
        dumped_instances = self.output_schema.dump(instances, many=True)
        return success_response(dumped_instances, "expensies")
