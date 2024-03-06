from pydantic import BaseModel


class ProjectCreateRequest(BaseModel):
    name: str
    description: str


class ProjectUpdateRequest(BaseModel):
    name: str
    description: str
