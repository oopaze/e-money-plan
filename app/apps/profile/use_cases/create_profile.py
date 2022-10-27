from this import d

from ....common.utils.generate_token import create_auth_tokens
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
        return self.handle_response(dumped_instance, create_auth_tokens(id))

    def handle_response(self, data, token_data):
        response = {}
        response.update(data)
        response["auth_token"] = token_data
        return success_response(response, "profile", 201)
