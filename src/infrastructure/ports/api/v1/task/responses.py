from datetime import datetime
from pydantic import BaseModel


class TaskBaseResponse(BaseModel):
    id: str
    name: str
    start: datetime
    end: datetime
    additional_information: str
