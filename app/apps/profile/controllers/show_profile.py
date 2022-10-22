from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..repositories.profile import profile_repository
from ..schemas.show_profile import ShowProfileSchema
from ..use_cases.show_profile import ShowProfileUseCase

show_profile_bp = Blueprint("show_profile", __name__)


@show_profile_bp.route("")
@jwt_required()
def show_profile():
    id = get_jwt_identity()
    output_schema = ShowProfileSchema()
    use_case = ShowProfileUseCase(profile_repository, output_schema)

    return use_case.execute(id=id)
