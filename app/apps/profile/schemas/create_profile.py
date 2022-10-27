from marshmallow import Schema
from marshmallow.fields import String

from ....common.fields import Email, Money
from ..repositories.profile import profile_repository


class CreateProfileSchema(Schema):
    email = Email(required=True, repository=profile_repository)
    name = String(required=True, allow_none=False)
    salary = Money(required=True)
