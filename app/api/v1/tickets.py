from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import users
from app.api.v1.auth  import get_current_user


router = APIRouter()

@router.post('/create')
def create_ticket_by_event_id():
    pass
@router.patch('/manage/{id}')
def update_ticket():
    pass
@router.get('/info/{id}')
def get_ticket():
    pass
@router.delete('/delete{id}')
def delete_ticket():
    pass
@router.post('/checkout/{id}')
def make_payment_for_ticket():
    pass