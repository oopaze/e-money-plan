from marshmallow import Schema

from ....common.fields import Related
from ...profile.repositories.profile import profile_repository


class LoginSchema(Schema):
    email = Related(field="email", repository=profile_repository, required=True)
