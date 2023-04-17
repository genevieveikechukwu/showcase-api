from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from app.database.database import get_db
from app.schemas import users, payment_details
from typing import Optional
from app.crud import user_crud
from .auth  import  get_current_user


router = APIRouter()



@router.get("/profile")
async def user_profile(current_user: users.User = Depends(get_current_user)):
    """
    user_profile return current user details

    Args:
        current_user (users.User, optional): _description_. Defaults to Depends(get_current_user).

    Returns:
        _type_: returns the user object
    """
    return current_user


@router.patch('/update/')
def update_email(q: str, current_user: users.UpdateUser, db:Session=Depends(get_current_user)):
    """
    update_email update the email

    Args:
        q (str): _description_
        current_user (users.UpdateUser): _description_
        db (Session, optional): _description_. Defaults to Depends(get_current_user).

    Returns:
        _type_: _updated email and the users hashed password
    """
    try:
            if q == current_user.email: 
                user_crud.update_user_email(db=db, user=current_user.email)
                return {"data": {current_user},
                        "message": "Email updated successfully",
                        "success": True,
                        "status_code": 200,
                        }
    except HTTPException as error:
            return {
                "data": "null",
                "message": "Unable to update email",
                "success": False,
                "error": {error},
                "status_code": 500,
        }
    return {
      "data": "null",
      "message": "User not found",
      "success": False,
      "error": {"Unable to find user"},
      "status_code": 500,
  }



@router.patch('/update')
def update_password(q: str, current_user: users.UpdateUser, db: Session = Depends(get_current_user)):
    """
    update_password 

    Args:
        q (str): _description_
        current_user (users.UpdateUser): _description_
        db (Session, optional): _description_. Defaults to Depends(get_current_user).

    Returns:
        _type_: _description_
    """
    try:
            if q == current_user.email:
                user_crud.update_user_password(db=db, user=current_user.password)
                return {"data": {current_user},
                        "message": "Password updated successfully",
                        "success": True,
                        "status_code": 200,
                        }
    except HTTPException as error:
            return {
                "data": "null",
                "message": "Unable to update password",
                "success": False,
                "error": {error},
                "status_code": 500,
            }

    
@router.post('/billing/add')
def add_billing(token: payment_details.PaymentDetailBase, db: Session=Depends(get_current_user)):
    """
    add_billing _summary_

    Args:
        token (payment_details.PaymentDetailBase): _description_
        db (Session, optional): _description_. Defaults to Depends(get_current_user).

    Returns:
        _type_: the bill details
    """
    try:
       billing = user_crud.add_payment_token(token=token)
       return {"data": {billing},
               "message": "Password updated successfully",
               "success": True,
               "status_code": 200,
               }
    except:
        return {"data": "null",
                "message": "Unable to add billing",
                "success": False,
                "status_code": 404,
                }

@router.delete('/delete')
def delete_user(user_id: int, db: Session = Depends(get_current_user)):
    """
    delete_user _summary_

    Args:
        user_id (int): _description_
        db (Session, optional): _description_. Defaults to Depends(get_current_user).
    """
    user_crud.delete_users(db=db, user_id=user_id)
   
    return {"data": "null",
                "message": "User deleted successfully",
                "success": True,
                "status_code": 201,
                }

@router.get('/events')
def get_events(user_id: int, db: Session=Depends(get_current_user)):
    """
    get_event _summary_

    Args:
        db (Session): _description_
        user_id (int): _description_

    Returns:
        _type_: Event
    """
    return user_crud.get_event(db=db, user_id=user_id)
