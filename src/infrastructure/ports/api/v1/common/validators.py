from datetime import datetime

from time_sheet.src.core.modules.common.exceptions.domain import (
    InvalidDateFormat,
    InvalidDateRange,
)


def validate_date_format(date):
    try:
        datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%fZ")
    except ValueError as exc:
        x = exc
        raise InvalidDateFormat from exc


def validate_date_range(start, end):
    if start > end:
        raise InvalidDateRange
