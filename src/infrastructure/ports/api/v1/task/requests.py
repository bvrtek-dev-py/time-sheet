from datetime import datetime
from typing import Any
from pydantic import BaseModel, model_validator
from pydantic import Field
from time_sheet.src.infrastructure.ports.api.v1.common.validators import (
    validate_date_range,
)


class TaskBaseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    start: datetime
    end: datetime
    additional_information: str = Field(..., min_length=5, max_length=100)

    @model_validator(mode="after")
    def validate_dates(self) -> Any:
        validate_date_range(self.start, self.end)
        return self


class TaskCreateRequest(TaskBaseRequest):
    pass


class TaskUpdateRequest(TaskBaseRequest):
    pass
