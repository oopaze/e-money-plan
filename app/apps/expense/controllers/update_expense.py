from flask import Blueprint, request

from ..repositories.expense import expense_repository
from ..schemas.show_expense import ShowExpenseSchema
from ..schemas.update_expense import UpdateExpenseSchema
from ..use_cases.update_expense import UpdateExpenseUseCase

update_expense_bp = Blueprint("update_expense", __name__)


@update_expense_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_expense(id):
    payload = request.json

    output_schema = ShowExpenseSchema()
    create_schema = UpdateExpenseSchema()
    use_case = UpdateExpenseUseCase(expense_repository, output_schema, create_schema)

    return use_case.execute(payload, id)
