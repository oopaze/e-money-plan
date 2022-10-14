from flask import Blueprint

from ..repositories.profile import profile_repository
from ..use_cases.delete_profile import DeleteProfileUseCase

delete_profile_bp = Blueprint("delete_profile", __name__)


@delete_profile_bp.route("/<int:id>", methods=["DELETE"])
def delete_profile(id):
    use_case = DeleteProfileUseCase(profile_repository)
    return use_case.execute(id=id)
