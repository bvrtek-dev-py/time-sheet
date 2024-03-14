from bson import ObjectId
from bson.errors import InvalidId
from pydantic import BaseModel, Field, model_validator

from time_sheet.src.core.modules.common.exceptions.domain import InvalidObjectIdType


class ProjectBaseRequest(BaseModel):
    name: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=5, max_length=200)
    owner_id: str

    @model_validator(mode="after")
    def validate_owner_id_type(self) -> "ProjectBaseRequest":
        owner_id = self.owner_id

        try:
            ObjectId(owner_id)
        except InvalidId as exception:
            raise InvalidObjectIdType() from exception

        return self


class ProjectCreateRequest(ProjectBaseRequest):
    pass


class ProjectUpdateRequest(ProjectBaseRequest):
    pass
