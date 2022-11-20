from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    dni: str
    firstname: str
    lastname: str
    email: EmailStr
    password: str
    date_of_birth: datetime
    activated: int
    admin: int
    chofer: int
    created_at: datetime


class User(UserBase):
    id: int

    class Config:
        orm_mode = True
