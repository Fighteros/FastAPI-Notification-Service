from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    email: str
    full_name: str
    reminder_date: datetime

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        orm_mode = True