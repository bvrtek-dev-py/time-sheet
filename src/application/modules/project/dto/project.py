from pydantic import BaseModel


class ProjectBaseDTO(BaseModel):
    name: str
    description: str


class ProjectCreateDTO(ProjectBaseDTO):
    owner_id: str


class ProjectUpdateDTO(ProjectBaseDTO):
    pass
