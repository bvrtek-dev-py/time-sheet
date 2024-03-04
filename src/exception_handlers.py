from fastapi import status
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from time_sheet.src.core.modules.common.exceptions.domain import (
    BaseHttpException,
    ObjectDoesNotExist,
)


def http_exception_handler(request: Request, exception: BaseHttpException):
    if isinstance(exception, ObjectDoesNotExist):
        return JSONResponse(
            status_code=status.HTTP_404_NOT_FOUND,
            content={"detail": exception.detail},
        )
