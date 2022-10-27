from decimal import Decimal

import sqlalchemy as sa

from ..common.models.numeric_id import NumericIdModel
from ..common.models.time_stamped import TimeStampedModel
from ..extensions.database_extension import db


class Profile(db.Model, NumericIdModel, TimeStampedModel):
    __tablename__ = "profiles"

    email = sa.Column(sa.String(45))
    name = sa.Column(sa.String(100))
    salary = sa.Column(sa.Numeric(15, 2))

    expensies = sa.orm.relationship("Expense", back_populates="profile")

    def __init__(self, name, email, salary):
        self.email = email
        self.name = name
        self.salary = Decimal(salary)
