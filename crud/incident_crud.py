from sqlalchemy.orm import Session
from models.incident import Incident
from schemas.incident import IncidentCreate

def create_incident(db: Session, incident: IncidentCreate):
    db_incident = Incident(**incident.dict())
    db.add(db_incident)
    db.commit()
    db.refresh(db_incident)
    return db_incident

def get_incident(db: Session, incident_id: int):
    return db.query(Incident).filter(Incident.id_incident == incident_id).first()

def get_incidents(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Incident).offset(skip).limit(limit).all()

def delete_incident(db: Session, incident_id: int):
    db_incident = get_incident(db, incident_id)
    if db_incident:
        db.delete(db_incident)
        db.commit()
        return True
    return False
