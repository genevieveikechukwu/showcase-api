from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import users
from app.api.v1.auth  import get_current_user


router = APIRouter()


@router.post('/create')
def create_event():
    pass
@router.get('/explore')
def get_tickets():
    pass
@router.get('/explore/{id}')
def get_event_by_id():
    pass
@router.patch('/manage/{id}')
def update_event():
    pass
@router.delete('/delete')
def delete_event():
    pass