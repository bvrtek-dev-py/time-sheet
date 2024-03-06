from pydantic import BaseModel, EmailStr, Field


class UserBaseRequest(BaseModel):
    fullname: str = Field(..., min_length=5, max_length=50)


class UserCreateRequest(UserBaseRequest):
    email: EmailStr = Field(..., min_length=5, max_length=50)
    password: str = Field(..., min_length=8, max_length=20)


class UserUpdateRequest(UserBaseRequest):
    pass
