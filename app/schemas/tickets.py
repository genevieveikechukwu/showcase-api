from typing import Any,Optional
import datetime
from pydantic import BaseModel, EmailStr
from enums.tickets import Ticket_stock, Ticket_type


class TicketBase(BaseModel):
    name: str
    description: str


class TicketCreate(TicketBase):
    ticket_type: Ticket_type
    stock: Ticket_stock
    no_of_stock: int
    purchase_limit: int
    price: int




class Ticket(TicketBase):
    id: int
    event_id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
  

    class Config:
        orm_mode = True
