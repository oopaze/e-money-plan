from app.entities import Expense
from marshmallow.fields import Date, Enum
from marshmallow_sqlalchemy.schema import SQLAlchemyAutoSchema


class ShowExpenseSchema(SQLAlchemyAutoSchema):
    class Meta:
        model = Expense
        fields = ("id", "value", "name", "color", "due_date", "paid", "status", "is_mine")

    status = Enum(enum=Expense.ExpenseStatus)
    due_date = Date("%d/%m/%Y")
