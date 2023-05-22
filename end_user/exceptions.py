from rest_framework.views import exception_handler
from constant import ret_codes


def status_code_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None and response.status_code == 401:
        return ret_codes.ResponseUnauthorized()

    if response is not None and response.status_code == 405:
        return ret_codes.ResponseNotAllowed()

    return response
