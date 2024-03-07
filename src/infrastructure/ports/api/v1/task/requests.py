from datetime import datetime
from pydantic import BaseModel


class TaskBaseRequest(BaseModel):
    name: str
    start: datetime
    end: datetime
    additional_information: str


class TaskCreateRequest(TaskBaseRequest):
    pass


class TaskUpdateRequest(TaskBaseRequest):
    pass
