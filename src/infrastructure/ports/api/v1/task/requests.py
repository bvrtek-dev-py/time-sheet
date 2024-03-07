from datetime import datetime
from pydantic import BaseModel
from pydantic import Field


class TaskBaseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    start: datetime
    end: datetime
    additional_information: str = Field(..., min_length=5, max_length=100)


class TaskCreateRequest(TaskBaseRequest):
    pass


class TaskUpdateRequest(TaskBaseRequest):
    pass
