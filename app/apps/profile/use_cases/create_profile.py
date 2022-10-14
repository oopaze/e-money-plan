from ....common.utils.response import error_response, success_response
from ....common.utils.use_case import UseCase


class CreateProfileUseCase(UseCase):
    def execute(self, payload):
        if errors := self.validation_schema.validate(payload):
            return error_response(errors)
        return self.handle_success(payload)

    def handle_success(self, payload):
        instance = self.repository.create(payload)
        dumped_instance = self.output_schema.dump(instance)
        return success_response(dumped_instance, "profile", 201)
