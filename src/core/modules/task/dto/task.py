from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field


class TaskDTO(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    start: datetime
    end: datetime
    additional_information: str
