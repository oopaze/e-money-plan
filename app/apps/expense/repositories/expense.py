from ....common.utils.repository import Repository
from ....entities import Expense


class ExpenseRepository(Repository):
    ...


expense_repository = ExpenseRepository(Expense)
