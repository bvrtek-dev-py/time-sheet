from pydantic import BaseModel

from time_sheet.src.infrastructure.ports.api.v1.user.responses import UserBaseResponse


class ProjectBaseResponse(BaseModel):
    id: str
    name: str
    description: str
    owner: UserBaseResponse
