from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

from ..repositories.profile import profile_repository
from ..use_cases.delete_profile import DeleteProfileUseCase

delete_profile_bp = Blueprint("delete_profile", __name__)


@delete_profile_bp.route("", methods=["DELETE"])
@jwt_required()
def delete_profile():
    id = get_jwt_identity()

    use_case = DeleteProfileUseCase(profile_repository)
    return use_case.execute(id=id)
