from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from database.database import get_db
from fastapi_pagination import add_pagination


router = APIRouter()
add_pagination(router)

@router.get("/users")
def users():
    return {"message": "welcome"}