from pydantic import BaseModel,EmailStr
from enums.users import Acct_type
from typing import Any, Optional
import datetime

class UserBase(BaseModel):
    email: EmailStr



class IndividualCreate(UserBase):
    first_name: str
    last_name: str
    acct_type: Acct_type
    country: str
    password: str

class OrgarnizationCreate(UserBase):
    Business_name: str
    password: str
    country: str


class User(UserBase):
    id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    class Config:
        orm_mode = True
