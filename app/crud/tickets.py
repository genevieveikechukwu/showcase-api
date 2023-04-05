from sqlalchemy.orm import Session
from app.models import models
from typing import Union, Dict, Any
from app.schemas import tickets, payment_details
from .hash import decode_token, hash_token
from fastapi.encoders import jsonable_encoder

def create_ticket(db:Session, ticket:tickets.TicketCreate):
    ticket = models.Ticket(**tickets.dict())
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    return ticket


def update_event(db: Session, db_obj: models.Event, obj_in: Union[tickets.TicketCreate, Dict[str, Any]]):
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

def get_ticket(db: Session, id:int):
    return db.query(models.Ticket).filter(models.Ticket.id == id)


def delete_event(db: Session, id: int):
        ticket = get_ticket(db, id=id)
        if ticket is None:
            return None
        db.delete(ticket)
        db.commit()
        return ticket

def create_payment_details(db: Session, details:payment_details.PaymentDetailBase):
        token_hash = hash_token(token=details.token)
        db_data = models.Payment_detail(token=token_hash)
        db.add(db_data)
        db.commit()
        db.refresh(db_data)