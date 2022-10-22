from flask_jwt_extended import create_access_token, create_refresh_token


def create_auth_tokens(profile_id: int):
    return {
        "access_token": create_access_token(profile_id, fresh=True),
        "refresh_token": create_refresh_token(profile_id),
    }
