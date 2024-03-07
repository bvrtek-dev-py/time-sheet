from pydantic import BaseModel


class ProjectCreateDTO(BaseModel):
    name: str
    description: str


class ProjectUpdateDTO(BaseModel):
    name: str
    description: str
