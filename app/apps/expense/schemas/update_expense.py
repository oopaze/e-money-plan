from marshmallow import Schema, fields

from ....common.fields import Enum, Money, Related
from ....entities import Expense
from ...profile.repositories.profile import profile_repository


class UpdateExpenseSchema(Schema):
    value = Money(required=False)
    name = fields.String(required=False, allow_none=False)
    color = fields.String(required=False, allow_none=False)
    total = Money(required=False)
    due_date = fields.Date("%x", required=False)
    status = Enum(enum=Expense.ExpenseStatus, required=False)
    paid = fields.Boolean(required=False)
    is_mine = fields.Boolean(required=False)
    profile_id = Related(repository=profile_repository, required=False)
