from sqlalchemy.orm import Session
from models.phone import Phone
from schemas.phone import PhoneCreate
from datetime import datetime

def create_phone(db: Session, phone: PhoneCreate):
    db_phone = Phone(**phone.dict())
    db.add(db_phone)
    db.commit()
    db.refresh(db_phone)
    return db_phone

def get_phone(db: Session, phone_id: int):
    return db.query(Phone).filter(Phone.id_phone == phone_id).first()

def get_phones(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Phone).offset(skip).limit(limit).all()

def delete_phone(db: Session, phone_id: int):
    db_phone = get_phone(db, phone_id)
    if db_phone:
        db.delete(db_phone)
        db.commit()
        return True
    return False
#def update_phone(db: Session, phone_id: int, phone_data: PhoneCreate):
# ...existing code...

def update_phone_active_status(db: Session, phone_id: int, is_active: bool):
    phone = db.query(Phone).filter(Phone.id_phone == phone_id).first()
    if phone:
        phone.is_active = is_active
        db.commit()
        db.refresh(phone)
        return phone
    return None

def update_timestamp(db: Session, phone_id: int):
    phone = db.query(Phone).filter(Phone.id_phone == phone_id).first()
    if phone:
        phone.timestatus = datetime.now().strftime("%H:%M:%S")
        db.commit()
        db.refresh(phone)
        return phone
    return None
def update_geolocation(db: Session, phone_id: int, X_coordinate: str, Y_coordinate: str, geolocation: int, battery: int):
    phone = db.query(Phone).filter(Phone.id_phone == phone_id).first()
    if phone:
        phone.X_coordinate = X_coordinate
        phone.Y_coordinate = Y_coordinate
        phone.geolocation = geolocation
        phone.battery = battery
        db.commit()
        db.refresh(phone)
        return phone
    return None