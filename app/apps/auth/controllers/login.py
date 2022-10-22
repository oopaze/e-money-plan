from flask import Blueprint, request

from ...profile.repositories.profile import profile_repository
from ..schemas.login import LoginSchema
from ..use_cases.login import LoginUseCase

login_bp = Blueprint("login", __name__)


@login_bp.route("login/", methods=["POST"])
def login():
    payload = request.json

    validation_schema = LoginSchema()
    use_case = LoginUseCase(profile_repository, validation_schema=validation_schema)

    return use_case.execute(payload)
