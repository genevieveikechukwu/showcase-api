from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Date
from datetime import datetime
from database.database import Base
from enums.tickets import Ticket_type, Enum, Ticket_stock

class Ticket(Base):
    __tablename__ = "tickets"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    description = Column(String(300))
    ticket_type = Column(Enum(Ticket_type))
    stock = Column(Enum(Ticket_stock))
    no_of_stock = Column(Integer, nullable=True)
    purchase_limit = Column(Integer, nullable=True)
    price = Column(Integer)
    event_id = Column(Integer, ForeignKey("event.id"))
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())

