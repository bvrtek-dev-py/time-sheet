from pydantic import BaseModel


class ProjectBaseResponse(BaseModel):
    id: str
    name: str
    description: str
