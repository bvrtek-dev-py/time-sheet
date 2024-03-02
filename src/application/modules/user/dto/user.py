from pydantic import BaseModel, EmailStr


class UserCreateDTO(BaseModel):
    fullname: str
    email: EmailStr
    password: str


class UserUpdateDTO(BaseModel):
    fullname: str
