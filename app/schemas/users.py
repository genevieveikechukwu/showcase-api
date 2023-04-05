from pydantic import BaseModel,EmailStr
from app.enums.users import Acct_type, Country
from typing import Any, Optional
import datetime

class UserBase(BaseModel):
    email: str
    acct_type: Acct_type
    country: Country
    password: str


class IndividualCreate(UserBase):
    first_name: str
    last_name: str

class OrgarnizationCreate(UserBase):
    Business_name: str

class UserInDB(UserBase):
    hashed_password: str

class User(UserBase):
    id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    class Config:
        orm_mode = True

class UpdateUser(UserBase):
    email: str
    password: str