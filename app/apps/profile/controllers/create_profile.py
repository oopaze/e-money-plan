from flask import Blueprint, request

from ..repositories.profile import profile_repository
from ..schemas.create_profile import CreateProfileSchema
from ..schemas.show_profile import ShowProfileSchema
from ..use_cases.create_profile import CreateProfileUseCase

create_profile_bp = Blueprint("create_profile", __name__)


@create_profile_bp.route("", methods=["POST"])
def create_profile():
    payload = request.json

    output_schema = ShowProfileSchema()
    validation_schema = CreateProfileSchema()

    use_case = CreateProfileUseCase(profile_repository, output_schema, validation_schema)

    return use_case.execute(payload)
