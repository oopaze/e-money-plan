from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..repositories.expense import expense_repository
from ..schemas.show_expense import ShowExpenseSchema
from ..use_cases.list_expensies import ListExpensiesUseCase

list_expensies_bp = Blueprint("list_expensies", __name__)


@list_expensies_bp.route("/")
@jwt_required()
def list_expensies():

    output_schema = ShowExpenseSchema()
    use_case = ListExpensiesUseCase(expense_repository, output_schema)

    return use_case.execute()
