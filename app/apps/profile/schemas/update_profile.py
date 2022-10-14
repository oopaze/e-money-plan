from marshmallow import Schema

from ....common.fields import Email, Money
from ..repositories.profile import profile_repository


class UpdateProfileSchema(Schema):
    email = Email(required=False, repository=profile_repository)
    salary = Money(required=False)
