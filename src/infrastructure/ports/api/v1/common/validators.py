from datetime import datetime

from bson.errors import InvalidId

from time_sheet.src.core.modules.common.exceptions.domain import (
    InvalidDateFormat,
    InvalidDateRange,
)
from time_sheet.src.core.modules.common.models.object_id import ObjectId


def validate_date_format(date: str) -> None:
    try:
        datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError as exc:
        raise InvalidDateFormat from exc


def validate_date_range(start: datetime, end: datetime) -> None:
    if start > end:
        raise InvalidDateRange


def validate_owner_id_type(self) -> "None":
    owner_id = self.owner_id

    try:
        ObjectId(owner_id)
    except InvalidId as exception:
        raise ValueError("Not a valid ObjectId") from exception

    return self
