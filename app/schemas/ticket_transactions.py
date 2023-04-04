from typing import Any, Optional
import datetime
from pydantic import BaseModel, EmailStr
from enums.ticket_transactions import Transaction_status


class TicketTransactionBase(BaseModel):
    email: EmailStr


class TicketTransactionCreate(TicketTransactionBase):
    first_name: str
    last_name: str
    fee: int
    status: Transaction_status
    no_of_purchase: int
    amount: int
    


class TicketTransaction(TicketTransactionBase):
    id: int
    ticket_id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
   

    class Config:
        orm_mode = True
