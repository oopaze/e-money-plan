from app.common.utils.response import error_response


def error_404(_):
    return error_response("NOT FOUND", "error", 404)
