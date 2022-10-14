from flask import jsonify


def response(data, status_code=200, success=True, context_key="data"):
    body = {"status_code": status_code, "success": success, context_key: data}

    return jsonify(body), status_code


def success_response(data, context_key, status_code=200):
    return response(data, status_code, context_key=context_key)


def error_response(data, context_key="errors", status_code=400):
    return response(data, status_code, success=False, context_key=context_key)
