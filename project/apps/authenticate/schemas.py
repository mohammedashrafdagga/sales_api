from pydantic import BaseModel


# Token Model
class Token(BaseModel):
    access_token: str
    token_type: str


# Token Data Model
class TokenData(BaseModel):
    username: str or None = None


# For User
class UserLogin(BaseModel):
    username: str
    password: str

    class Config:
        orm_mode = True


class UserModel(BaseModel):
    name: str
    email: str
    username: str

    class Config:
        orm_mode = True


class UserCreateSuperuser(UserModel):
    password: str
    is_superuser: bool or None = True
    is_active: bool or None = True

    class Config:
        orm_mode = True
