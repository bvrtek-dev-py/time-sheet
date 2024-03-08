from datetime import datetime
from time_sheet.src.core.modules.common.exceptions.domain import (
    InvalidDateFormat,
    InvalidDateRange,
)


def validate_date_format(date: str) -> None:
    try:
        datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError as exc:
        raise InvalidDateFormat from exc


def validate_date_range(start: datetime, end: datetime) -> None:
    if start > end:
        raise InvalidDateRange
