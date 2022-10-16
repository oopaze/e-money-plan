from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class ListExpensiesUseCase(UseCase):
    def execute(self, payload=None, id=None):
        instances = self.repository.list()
        dumped_instances = self.output_schema.dump(instances, many=True)
        return success_response(dumped_instances, "expensies")
