from pydantic import BaseModel, Field


class UserModel(BaseModel):
    name: str
    age: int = Field(gt=0, lt=100)
    address: str

class UserResponse(BaseModel):
    id: int
    name: str
    age: int
    birth_date: int
    balans: int
