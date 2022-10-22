from flask import Blueprint
from flask_jwt_extended import get_jwt_identity, jwt_required

from ...profile.repositories.profile import profile_repository
from ..use_cases.refresh import RefreshUseCase

refresh_bp = Blueprint("refresh", __name__)


@refresh_bp.route("refresh/", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    use_case = RefreshUseCase(profile_repository)
    return use_case.execute(get_jwt_identity())
