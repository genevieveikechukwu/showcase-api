from sqlalchemy.orm import Session
from app.models import models
from typing import Union, Dict, Any
from app.schemas import events
from .hash import get_password_hash, verify_password, hash_token, decode_token
from fastapi.encoders import jsonable_encoder


def create_physical_event(db:Session, event:events.EventPhysicalCreate):
    event_data = models.Event(**event())
    db.add(event_data)
    db.commit()
    db.refresh(event_data)

def get_all_events(db:Session):
   return db.query(models.Event).all()


def get_event_details(db:Session, id:int):
    return db.query(models.Event).filter(models.Event.id == id)


def update_event(db: Session, db_obj: models.Event, obj_in: Union[events.EventPhysicalCreate, Dict[str, Any]]):
    # get_event_details(db, id=id)
    obj_data = jsonable_encoder(db_obj)
    if isinstance(obj_in, dict):
        update_data = obj_in
    else:
        update_data = obj_in.dict(exclude_unset=True)
    for field in obj_data:
        if field in update_data:
            setattr(db_obj, field, update_data[field])
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def delete_event(db:Session, id:int ):
        event = get_event_details(db, id=id)
        if event is None:
            return None
        db.delete(event)
        db.commit()
        return event