from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from schemas.phone import PhoneCreate, Phone, StatusPayload
from crud.phone_crud import create_phone, get_phone, get_phones, delete_phone, update_timestamp, update_phone_active_status, update_geolocation
from db.database import SessionLocal
from datetime import datetime


router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/phones/", response_model=Phone)
def create(phone: PhoneCreate, db: Session = Depends(get_db)):
    db_phone = create_phone(db, phone)

    return db_phone

@router.get("/phones/{phone_id}", response_model=Phone)
def read(phone_id: int, db: Session = Depends(get_db)):
    return get_phone(db, phone_id)

@router.get("/phones/", response_model=list[Phone])
def read_all(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    return get_phones(db, skip, limit)

@router.delete("/phones/{phone_id}")
def delete(phone_id: int, db: Session = Depends(get_db)):
    success = delete_phone(db, phone_id)
    return {"deleted": success}
# @router.put("/phones/{phone_id}", response_model=Phone)



@router.post("/status/")
def update_status(payload: StatusPayload, db: Session = Depends(get_db)):
    # Sprawdzenie czy telefon istnieje
    phone = get_phone(db, payload.id_phone)
    if not phone:
        raise HTTPException(status_code=404, detail="Phone not found")

    # Aktualizacja statusów
    update_phone_active_status(db, payload.id_phone, True)
    update_timestamp(db, payload.id_phone)
    updated = update_geolocation(
        db,
        phone_id=payload.id_phone,
        X_coordinate=payload.X_coordinate,
        Y_coordinate=payload.Y_coordinate,
        geolocation=payload.geolocation,
        battery=payload.battery
    )

    return {
        "status": "updated",
        "id_phone": updated.id_phone,
        "is_active": updated.is_active,
        "battery": updated.battery,
        "X_coordinate": updated.X_coordinate,
        "Y_coordinate": updated.Y_coordinate,
        "geolocation": updated.geolocation,
        "timestatus": updated.timestatus
    }