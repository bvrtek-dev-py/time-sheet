from datetime import datetime
from typing import Any
from pydantic import BaseModel, model_validator
from pydantic import Field
from time_sheet.src.infrastructure.ports.api.v1.common.validators import (
    validate_date_format,
    validate_date_range,
)


class TaskBaseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    start: datetime
    end: datetime
    additional_information: str = Field(..., min_length=5, max_length=100)

    @model_validator(mode="before")
    def validate_dates(self) -> Any:
        validate_date_format(self.get("start"))
        validate_date_format(self.get("end"))
        validate_date_range(self.get("start"), self.get("end"))
        return self


class TaskCreateRequest(TaskBaseRequest):
    pass


class TaskUpdateRequest(TaskBaseRequest):
    pass
