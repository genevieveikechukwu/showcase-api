from fastapi import APIRouter
from app.api.v1 import users
from app.api.v1 import auth
from app.api.v1 import events
from app.api.v1 import tickets

api_router = APIRouter()


api_router.include_router(
    auth.router,  tags=["auth"]
)
api_router.include_router(
    users.router, prefix="/users", tags=["users"]
)
api_router.include_router(
    events.router, prefix="/events", tags=["events"]
)
api_router.include_router(
    tickets.router, prefix="/tickets", tags=["tickets"]
)
