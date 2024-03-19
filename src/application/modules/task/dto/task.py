from datetime import datetime
from pydantic import BaseModel


class TaskBaseDTO(BaseModel):
    name: str
    start: datetime
    end: datetime
    additional_information: str


class TaskCreateDTO(TaskBaseDTO):
    owner_id: str


class TaskUpdateDTO(TaskBaseDTO):
    pass
