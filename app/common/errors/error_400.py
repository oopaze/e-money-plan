from app.common.utils.response import error_response


def error_400(error):
    return error_response(error.description, "error")
