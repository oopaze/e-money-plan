from ....common.utils.generate_token import create_auth_tokens
from ....common.utils.response import success_response
from ....common.utils.use_case import UseCase


class RefreshUseCase(UseCase):
    def execute(self, id):
        return success_response(create_auth_tokens(id), "auth")
