from flask import Blueprint
from flask_jwt_extended import jwt_required

from ..repositories.expense import expense_repository
from ..use_cases.delete_expense import DeleteExpenseUseCase

delete_expense_bp = Blueprint("delete_expense", __name__)


@delete_expense_bp.route("/<int:id>", methods=["DELETE"])
@jwt_required()
def delete_expense(id):
    use_case = DeleteExpenseUseCase(expense_repository)
    return use_case.execute(id=id)
