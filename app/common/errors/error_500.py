from app.common.utils.response import error_response


def error_500(err):
    default_message = "INTERNAL_SERVER ERROR"
    return error_response(err.description or default_message, "error", 500)
