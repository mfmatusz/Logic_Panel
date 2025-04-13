from fastapi import FastAPI
from routers import phones,incidents
from db.base import Base
from db.database import engine

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(phones.router, prefix="/api", tags=["phones"])
# app.include_router(groups.router, prefix="/api", tags=["groups"])
app.include_router(incidents.router, prefix="/api", tags=["incidents"])
