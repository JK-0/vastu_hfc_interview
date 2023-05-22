
from rest_framework import status
from rest_framework.response import Response


class ResponseOk(Response):

    status_code = status.HTTP_200_OK

    def __init__(self, data=None):
        if data is None:
            data = {"success": 1, "message": "OK", "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 1, "message": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 1
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "message" not in data.keys():
                data["message"] = "OK"
        super(ResponseOk, self).__init__(data, status=self.status_code)


class ResponseCreated(Response):

    status_code = status.HTTP_201_CREATED

    def __init__(self, data=None):
        if data is None:
            data = {"success": 1, "message": "Created",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 1, "message": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 1
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "message" not in data.keys():
                data["message"] = "Created"
        super(ResponseCreated, self).__init__(data, status=self.status_code)


class ResponseAccepted(Response):

    status_code = status.HTTP_202_ACCEPTED

    def __init__(self, data=None):
        if data is None:
            data = {"success": 1, "message": "Created",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 1, "message": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 1
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "message" not in data.keys():
                data["message"] = "Created"
        super(ResponseAccepted, self).__init__(data, status=self.status_code)


class ResponseReset(Response):

    status_code = status.HTTP_205_RESET_CONTENT

    def __init__(self, data=None):
        if data is None:
            data = {"success": 1, "message": "Created",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 1, "message": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 1
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "message" not in data.keys():
                data["message"] = "Created"
        super(ResponseReset, self).__init__(data, status=self.status_code)


class ResponseBadRequest(Response):

    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Bad Request",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Bad Request"
        super(ResponseBadRequest, self).__init__(data, status=self.status_code)


class ResponseUnauthorized(Response):

    status_code = status.HTTP_401_UNAUTHORIZED

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Unauthorized",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Unauthorized"
        super(ResponseUnauthorized, self).__init__(
            data, status=self.status_code)


class ResponseForbidden(Response):

    status_code = status.HTTP_403_FORBIDDEN

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Forbidden",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Forbidden"
        super(ResponseForbidden, self).__init__(data, status=self.status_code)


class ResponseNotFound(Response):

    status_code = status.HTTP_404_NOT_FOUND

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Not found",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Not found"
        super(ResponseNotFound, self).__init__(data, status=self.status_code)


class ResponseNotAllowed(Response):

    status_code = status.HTTP_405_METHOD_NOT_ALLOWED

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Method Not Allowed",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Method Not Allowed"
        super(ResponseNotAllowed, self).__init__(data, status=self.status_code)


class ResponseConflict(Response):

    status_code = status.HTTP_409_CONFLICT

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Conflict with data",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Conflict with data"
        super(ResponseConflict, self).__init__(data, status=self.status_code)


class ResponseInternalServerError(Response):

    status_code = status.HTTP_500_INTERNAL_SERVER_ERROR

    def __init__(self, data=None):
        if data is None:
            data = {"success": 0, "error": "Internal Server Error",
                    "status": self.status_code}
        if isinstance(data, str):
            data = {"success": 0, "error": data, "status": self.status_code}
        elif isinstance(data, dict):
            if "success" not in data.keys():
                data["success"] = 0
            if "status" not in data.keys():
                data["status"] = self.status_code
            if "error" not in data.keys():
                data["error"] = "Internal Server Error"
        super(ResponseInternalServerError, self).__init__(
            data, status=self.status_code)
