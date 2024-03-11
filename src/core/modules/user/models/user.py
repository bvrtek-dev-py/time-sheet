from pydantic import Field, EmailStr

from time_sheet.src.core.modules.common.models.base_model import MongoDBModel


class User(MongoDBModel):
    fullname: str = Field(..., min_length=5, max_length=50)
    email: EmailStr = Field(..., min_length=5, max_length=50, unique=True)
    password: str = Field(..., min_length=8)
