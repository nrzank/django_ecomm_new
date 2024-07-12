from rest_framework.exceptions import APIException
from rest_framework import status


class PermissionDeniedException(APIException):
    status_code = status.HTTP_403_FORBIDDEN
    default_detail = "У вас нет доступа к изменению этого товара"
    default_code = "permission_denied"
