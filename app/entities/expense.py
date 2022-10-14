from decimal import Decimal

import sqlalchemy as sa

from ..common.models.numeric_id import NumericIdModel
from ..common.models.time_stamped import TimeStampedModel
from ..common.utils.enum import Enum
from ..extensions.database_extension import db


class Expense(db.Model, NumericIdModel, TimeStampedModel):
    class ExpenseStatus(Enum):
        active = "active"
        cancelled = "cancelled"

    value = sa.Column(sa.Numeric(14, 2))
    name = sa.Column(sa.String())
    color = sa.Column(sa.String(40))
    total = sa.Column(sa.Numeric(14, 2))
    due_date = sa.Column(sa.Date())
    status = sa.Column(sa.Enum(ExpenseStatus))
    paid = sa.Column(sa.Boolean)

    profile_id = sa.Column(sa.Integer, sa.ForeignKey("profiles.id"))
    profile = sa.orm.relationship("Profile", back_populates="expensies", lazy=True)

    def __init__(
        self,
        value,
        name,
        color,
        total,
        due_date,
        profile_id,
        paid=False,
        status=ExpenseStatus.active,
    ):
        self.value = Decimal(value)
        self.name = name
        self.color = color
        self.total = Decimal(total)
        self.due_date = due_date
        self.profile_id = profile_id
        self.paid = paid
        self.status = status

    @property
    def percent(self):
        return (self.value * 100) / self.total
