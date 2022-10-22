from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..repositories.expense import expense_repository
from ..schemas.show_expense import ShowExpenseSchema
from ..use_cases.show_expense import ShowExpenseUseCase

show_expense_bp = Blueprint("show_expense", __name__)


@show_expense_bp.route("/<int:id>")
@jwt_required()
def show_expense(id):

    output_schema = ShowExpenseSchema()
    use_case = ShowExpenseUseCase(expense_repository, output_schema)

    return use_case.execute(id=id)
