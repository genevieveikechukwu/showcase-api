from typing import Any, Optional
import datetime
from pydantic import BaseModel, EmailStr



class PaymentDetailBase(BaseModel):
    token: str


class PaymentDetail(PaymentDetailBase):
    id: int
    user_id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    
    class Config:
        orm_mode = True
