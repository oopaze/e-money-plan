from flask import Blueprint, request

from ..repositories.profile import profile_repository
from ..schemas.show_profile import ShowProfileSchema
from ..schemas.update_profile import UpdateProfileSchema
from ..use_cases.update_profile import UpdateProfileUseCase

update_profile_bp = Blueprint("update_profile", __name__)


@update_profile_bp.route("/<int:id>", methods=["PUT", "PATCH"])
def update_profile(id):
    payload = request.json

    output_schema = ShowProfileSchema()
    validation_schema = UpdateProfileSchema()

    use_case = UpdateProfileUseCase(profile_repository, output_schema, validation_schema)

    return use_case.execute(payload, id)
