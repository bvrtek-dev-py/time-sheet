from typing import Optional

from pydantic import BaseModel, Field

from time_sheet.src.core.modules.common.models.object_id import ObjectId


class MongoDBModel(BaseModel):
    id: Optional[ObjectId] = Field(alias="_id", default=None)

    class ConfigDict:
        json_encoders = {
            ObjectId: lambda value: str(value),
        }
