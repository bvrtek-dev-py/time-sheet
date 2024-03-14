from pydantic import BaseModel


class ProjectCreateDTO(BaseModel):
    name: str
    description: str
    owner_id: str


class ProjectUpdateDTO(BaseModel):
    name: str
    description: str
    owner_id: str
