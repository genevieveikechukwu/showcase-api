from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date, Enum
from datetime import date, datetime
from database.database import Base
from enums.events import Event_type, Event_categories, Event_frequency
from enums.users import Country, Acct_type
from enums.tickets import Ticket_type, Ticket_stock
from enums.ticket_transactions import Transaction_status


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    event_name = Column(String(100))
    description = Column(String(300))
    location = Column(String(300))
    location_tip = Column(String(300))
    event_type = Column(Enum(Event_type), default=Event_type.PHYSICAL)
    virtual_meet_link = Column(String(255))
    category = Column(Enum(Event_categories))
    custom_url = Column(String(300))
    frequency = Column(Enum(Event_frequency))
    start_date = Column(Date(), default=date.today())
    start_time = Column(DateTime(timezone=True), default=datetime.now())
    end_date = Column(Date(), default=date.today())
    end_time = Column(DateTime(timezone=True), default=datetime.now())
    twitter_url = Column(String(300))
    facebook_url = Column(String(300))
    instagram_url = Column(String(300))
    created_at = Column(DateTime(timezone=True), default=datetime.now())
    updated_at = Column(DateTime(timezone=True), default=datetime.now())
    user_id = Column(
        Integer, ForeignKey("users.id")
    )

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(300))
    last_name = Column(String(300))
    business_name = Column(String(300))
    country = Column(Enum(Country))
    email = Column(String, unique=True, index=True)
    password = Column(String(100), nullable=False)
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    acct_type = Column(Enum(Acct_type))


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
    event_id = Column(Integer, ForeignKey("events.id"))
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    

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
    ticket_id = Column(Integer, ForeignKey("tickets.id"))
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())


class Payment_detail(Base):
    __tablename__ = "payment_details"
    id = Column(Integer, primary_key=True, index=True)
    token = Column(String(100))
    user_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
    updated_at = Column(DateTime(timezone=True),
                        nullable=False, default=datetime.now())
