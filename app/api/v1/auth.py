from fastapi import FastAPI, APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

router = APIRouter()

Oauth2_scheme = OAuth2PasswordBearer(tokenUrl='token')

@router.post("/auth")
async def token(form_data: OAuth2PasswordBearer = Depends()):
    return{"acess_token": form_data.username + 'token'}

@router.get('/')
async def index(token:str = Depends(Oauth2_scheme)):
    return{'token': token}
