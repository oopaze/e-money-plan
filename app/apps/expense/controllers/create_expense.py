from flask import Blueprint, request

from ..repositories.expense import expense_repository
from ..schemas.create_expense import CreateExpenseSchema
from ..schemas.show_expense import ShowExpenseSchema
from ..use_cases.create_expense import CreateExpenseUseCase

create_expense_bp = Blueprint("create_expense", __name__)


@create_expense_bp.route("/", methods=["POST"])
def create_expense():
    payload = request.json

    output_schema = ShowExpenseSchema()
    create_schema = CreateExpenseSchema()
    use_case = CreateExpenseUseCase(expense_repository, output_schema, create_schema)

    return use_case.execute(payload)
