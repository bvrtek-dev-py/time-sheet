from pydantic import Field, model_validator

from time_sheet.src.core.modules.common.models.base_model import MongoDBModel
from time_sheet.src.infrastructure.ports.api.v1.common.validators import (
    validate_owner_id_type,
)


class Project(MongoDBModel):
    name: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=5, max_length=200)
    owner_id: str

    @model_validator(mode="after")
    def validate_owner_id(self):
        validate_owner_id_type(self)
