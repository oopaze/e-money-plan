from flask import Blueprint, request
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..repositories.profile import profile_repository
from ..schemas.show_profile import ShowProfileSchema
from ..schemas.update_profile import UpdateProfileSchema
from ..use_cases.update_profile import UpdateProfileUseCase

update_profile_bp = Blueprint("update_profile", __name__)


@update_profile_bp.route("", methods=["PUT", "PATCH"])
@jwt_required()
def update_profile():
    payload = request.json

    output_schema = ShowProfileSchema()
    validation_schema = UpdateProfileSchema()

    use_case = UpdateProfileUseCase(profile_repository, output_schema, validation_schema)

    return use_case.execute(payload, get_jwt_identity())
