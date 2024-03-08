from time_sheet.src.core.modules.common.exceptions.domain import (
    InvalidDateRange,
)


def validate_date_range(start, end):
    if start > end:
        raise InvalidDateRange
