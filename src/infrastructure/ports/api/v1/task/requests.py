from datetime import datetime
from typing import Dict, Any
from pydantic import BaseModel, model_validator
from pydantic import Field
from time_sheet.src.infrastructure.ports.api.v1.common.validators import (
    validate_date_range,
    validate_date_format,
)


class TaskBaseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    start: datetime
    end: datetime
    additional_information: str = Field(..., min_length=5, max_length=100)

    @model_validator(mode="before")
    @classmethod
    def validate_dates(cls, data: Dict[str, Any]) -> Dict[str, Any]:
        validate_date_format(data["start"])
        validate_date_format(data["end"])
        validate_date_range(data["start"], data["end"])

        return data


class TaskCreateRequest(TaskBaseRequest):
    pass


class TaskUpdateRequest(TaskBaseRequest):
    pass
