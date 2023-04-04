import uvicorn
from fastapi import Depends, HTTPException, FastAPI
from app.database.database import SessionLocal, engine
from app.models.models import Base
from app.api.v1 import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Showcase API")



app.include_router(api_router, prefix="/v1")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
