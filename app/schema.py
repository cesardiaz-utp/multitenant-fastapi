from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    username: str
    email: str

class UserRequest(UserBase):
    password: str

class UserResponse(UserBase):
    id: int
