from datetime import datetime
from pydantic import Field
from time_sheet.src.core.modules.common.models.base_model import MongoDBModel


class Task(MongoDBModel):
    name: str = Field(..., min_length=5, max_length=50)
    start: datetime = None
    end: datetime = None
    additional_information: str = Field(..., min_length=5, max_length=100)
