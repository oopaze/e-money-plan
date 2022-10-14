from flask import Blueprint

from ..repositories.profile import profile_repository
from ..schemas.show_profile import ShowProfileSchema
from ..use_cases.show_profile import ShowProfileUseCase

show_profile_bp = Blueprint("show_profile", __name__)


@show_profile_bp.route("/<int:id>")
def show_profile(id):

    output_schema = ShowProfileSchema()
    use_case = ShowProfileUseCase(profile_repository, output_schema)

    return use_case.execute(id=id)
