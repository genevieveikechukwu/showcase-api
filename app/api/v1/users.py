from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.database import get_db


router = APIRouter()


@router.get("/users")
def users():
    return {"message": "welcome"}