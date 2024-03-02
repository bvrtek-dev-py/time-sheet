from typing import Optional

from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    id: Optional[str] = Field(alias="_id")
    fullname: str
    email: str
    password: str
