from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from datetime import  datetime
from database.database import Base
from enums.ticket_transactions import Transaction_status, Enum


class Ticket_transaction(Base):
    __tablename__ = "ticket_transactions"
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    email = Column(String(300))
    fee = Column(Integer)
    status = Column(Enum(Transaction_status))
    no_of_purchase = Column(Integer)
    amount = Column(Integer)
    ticket_id = Column(Integer, ForeignKey("ticket.id"))
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
