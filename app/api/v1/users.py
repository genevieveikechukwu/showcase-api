from fastapi import FastAPI, Depends, APIRouter
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import users
from typing import Optional
from app.crud import user_crud
from .auth  import get_current_active_user, get_current_user


router = APIRouter()



@router.get("/profile")
async def user_profile(current_user: users.User = Depends(get_current_active_user)):
    return current_user


@router.patch('/update/')
def update_email(user: users.UpdateUser, q: str,  current_user: users.User = Depends(get_current_user)):
    if q == current_user.email: 
        user_crud.update_user_email(db=get_db, user=user.email)
        return {"data": {user},
                "message": "Email updated successfully",
                "success": True,
                "status_code": 200,
                }
    return {
        "data": "null",
        "message": "Unable to update email",
        "success": False,
        "error": {},
        "status_code": 404,
    }



@router.patch('/update')
def update_password():
    pass
@router.post('/billing/add')
def add_billing():
    pass
@router.delete('/delete')
def delete_user():
    pass
@router.get('/events')
def get_events():
    pass
