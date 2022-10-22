from ....common.utils.generate_token import create_auth_tokens
from ....common.utils.response import error_response, success_response
from ....common.utils.use_case import UseCase


class LoginUseCase(UseCase):
    def execute(self, payload):
        if self.validation_schema.validate(payload):
            return error_response("Credenciais inválidas", "message", 401)
        return self.handle_success(payload)

    def handle_success(self, payload):
        profile = self.repository.authenticate(payload.get("email", ""))
        return success_response(create_auth_tokens(profile.id), "auth")
