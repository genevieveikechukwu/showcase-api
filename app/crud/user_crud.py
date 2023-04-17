from sqlalchemy.orm import Session
from app.models import models
from fastapi import Depends
from app.schemas import users
from app.schemas import payment_details
from .hash import get_password_hash, verify_password, hash_token, decode_token
from fastapi.encoders import jsonable_encoder
from app.api.v1.auth import get_current_user

def get_user(db: Session, user_id:int):
    return db.query(models.User).filter(models.User.id == user_id)

def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()

def create_individual_user(db:Session, user:users.IndividualCreate):
    password = get_password_hash(user.password)
    db_user = models.User(password=password, **user.dict(exclude={"password"},))
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_business_user(db: Session, user: users.OrgarnizationCreate):
    password = get_password_hash(user.password)
    db_user = models.User(password=password, **user.dict(exclude={"password"})
                          )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user_password(user: users.UserBase, db: Session = Depends(get_current_user)):
    user = get_user_by_email(db, email=user.email)
    if user is None:
        return{"message": "user not found"}
    stored_item_data = models.User.password
    stored_item_model = user(**stored_item_data)
    update_data = user.dict(exclude_unset=True)
    if update_data:
        hashed_password = get_password_hash(user.password)
        update_data = hashed_password
    updated_password = stored_item_model.copy(update=update_data)
    models.User.password = jsonable_encoder(updated_password)
    db.add(updated_password)
    db.commit()
    db.refresh(updated_password)
    return user

    
def update_user_email(db: Session, user: users.UserBase):
    user = get_user_by_email(db, email=user.email)
    if user is None:
        return {"message": "user not found"}
    stored_item_data = models.User.email
    stored_item_model = user(**stored_item_data)
    update_data = user.dict(exclude_unset=True)
    updated_email = stored_item_model.copy(update=update_data)
    models.User.email = jsonable_encoder(updated_email)
    db.add(updated_email)
    db.commit()
    db.refresh(updated_email)
    return user

def add_payment_token(db:Session, token:payment_details.PaymentDetailBase ):
    token_hash = hash_token(token=token.token)
    db_data = models.Payment_detail(token=token_hash)
    db.add(db_data)
    db.commit()
    db.refresh(db_data)

def get_billing(db:Session, user_id:int):
    return db.query(models.Payment_detail).filter(models.Payment_detail.user_id
                                                   == user_id).first()
    
    
def delete_users(db:Session, user_id:int):
    user = get_user(db, user_id=user_id)
    if user is None:
        return None
    db.delete(user)
    db.commit()
    return user

def get_event(db:Session, user_id:int):

    return db.query(models.Event).filter(models.Event.user_id == user_id).all()