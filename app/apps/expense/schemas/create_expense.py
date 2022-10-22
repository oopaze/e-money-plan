from marshmallow import Schema, fields

from ....common.fields import Enum, Money, Related
from ....entities import Expense
from ...profile.repositories.profile import profile_repository

default_error_messages = {"required": "Este campo é obrigatório"}


class CreateExpenseSchema(Schema):
    value = Money(required=True)
    name = fields.String(
        required=True, allow_none=False, error_messages=default_error_messages
    )
    color = fields.String(
        required=True, allow_none=False, error_messages=default_error_messages
    )
    due_date = fields.Date(
        "%d/%m/%Y", required=True, error_messages=default_error_messages
    )
    status = Enum(enum=Expense.ExpenseStatus)
    paid = fields.Boolean(required=True, error_messages=default_error_messages)
    is_mine = fields.Boolean(required=True, error_messages=default_error_messages)
    profile_id = Related(required=True, repository=profile_repository)
