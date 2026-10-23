from pydantic import BaseModel, ConfigDict, EmailStr

class UserBase(BaseModel):
    email : EmailStr
    hashed_password : str
    is_admin : bool = False

class UserCreate(UserBase):
    model_config = ConfigDict(from_attributes=True)

class UserUpdate(UserBase):
    email : str | None = None
    hashed_password : str | None = None
    is_admin : bool | None = None

class UserPublic(UserBase):
    id : int

class Token(BaseModel):
    access_token: str
    token_type: str = "bearer"
