from marshmallow import Schema

from ....common.fields import Email, Money
from ..repositories.profile import profile_repository


class CreateProfileSchema(Schema):
    email = Email(required=True, repository=profile_repository)
    salary = Money(required=True)
