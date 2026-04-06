from pydantic import BaseModel, Field

class UserCreate(BaseModel):
    name: str
    role: str = Field(..., example="admin")


class RecordCreate(BaseModel):
    amount: float = Field(..., gt=0)
    type: str = Field(..., example="income")
    category: str
    date: str
    note: str