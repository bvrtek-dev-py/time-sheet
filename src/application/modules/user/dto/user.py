from pydantic import BaseModel, EmailStr


class UserBaseDTO(BaseModel):
    fullname: str


class UserCreateDTO(UserBaseDTO):
    email: EmailStr
    password: str


class UserUpdateDTO(UserBaseDTO):
    pass


class UserGetDTO(UserBaseDTO):
    id: str
    email: EmailStr
