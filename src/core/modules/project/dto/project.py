from typing import Optional

from pydantic import BaseModel, Field


class ProjectDTO(BaseModel):
    id: Optional[str] = Field(alias="_id")
    name: str
    description: str
