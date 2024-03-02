from pydantic import BaseModel, EmailStr


class UserCreateRequest(BaseModel):
    fullname: str
    email: EmailStr
    password: str


class UserUpdateRequest(BaseModel):
    fullname: str
