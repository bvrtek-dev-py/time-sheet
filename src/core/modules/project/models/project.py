from pydantic import Field

from time_sheet.src.core.modules.common.models.base_model import MongoDBModel


class Project(MongoDBModel):
    name: str = Field(..., min_length=5, max_length=50)
    description: str = Field(..., min_length=5, max_length=200)
    owner_id: str
