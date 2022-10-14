from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class ShowProfileUseCase(UseCase):
    def execute(self, id):
        instance = self.repository.get(id)
        dumped_instance = self.output_schema.dump(instance)
        return success_response(dumped_instance, "profile")
