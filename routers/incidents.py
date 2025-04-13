from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.incident import IncidentCreate, Incident
from crud.incident_crud import create_incident, get_incident, get_incidents, delete_incident
from db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/incidents/", response_model=Incident)
def create(incident: IncidentCreate, db: Session = Depends(get_db)):
    print(f"Creating incident: {incident}")
    return create_incident(db, incident)

@router.get("/incidents/{incident_id}", response_model=Incident)
def read(incident_id: int, db: Session = Depends(get_db)):
    return get_incident(db, incident_id)

@router.get("/incidents/", response_model=list[Incident])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_incidents(db, skip, limit)

@router.delete("/incidents/{incident_id}")
def delete(incident_id: int, db: Session = Depends(get_db)):
    success = delete_incident(db, incident_id)
    return {"deleted": success}
# # @router.put("/incidents/{incident_id}", response_model=Incident)