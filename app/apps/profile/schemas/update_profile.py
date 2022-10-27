from marshmallow import Schema
from marshmallow.fields import String

from ....common.fields import Email, Money
from ..repositories.profile import profile_repository


class UpdateProfileSchema(Schema):
    email = Email(required=False, repository=profile_repository)
    name = String(required=False, allow_none=False)
    salary = Money(required=False)
