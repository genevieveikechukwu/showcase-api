from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, Date
from datetime import date, datetime
from database.database import Base
from enums.events import Event_type, Enum, Event_categories, Event_frequency


class Event(Base):
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
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

