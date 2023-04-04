from typing import Any, Optional
import datetime
from pydantic import BaseModel, EmailStr
from enums.events import Event_categories,Event_frequency, Event_type


class EventBase(BaseModel):
    event_name: str

class EventPhysicalCreate(EventBase):
    description: str
    location: str
    location_tip: str
    event_type: Event_type
    category: str
    custom_url: str
    frequency: Event_frequency
    start_date: Optional[datetime.date]
    start_time: Optional[datetime.datetime]
    end_date: Optional[datetime.date]
    end_time: Optional[datetime.datetime]
    twitter_url: str    
    facebook_url: str    
    instagram_url: str    


class EventVirtualCreate(EventBase):
    description: str
    location: str
    event_type: Event_type
    virtual_meet_link: str
    category: Event_categories
    custom_url: str
    frequency: Event_frequency
    start_date: Optional[datetime.date]
    start_time: Optional[datetime.datetime]
    end_date: Optional[datetime.date]
    end_time: Optional[datetime.datetime]
    twitter_url: str    
    facebook_url: str    
    instagram_url: str 





class Event(EventBase):
    id: int
    user_id: int
    created_at: Optional[datetime.datetime]
    updated_at: Optional[datetime.datetime]
    
    class Config:
        orm_mode = True
