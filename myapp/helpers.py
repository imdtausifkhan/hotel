from rest_framework import status
from rest_framework.response import Response


def to_success(data=None, message=None, status_code=status.HTTP_200_OK):
    return {
        "status_code": status_code,
        "message": message,
        "data": data,
    }


def http_response(data=None, message=None, status_code=status.HTTP_200_OK):
    return Response(
        {
            "status_code": status_code,
            "message": message,
            "data": data,
        },
        status_code,
    )