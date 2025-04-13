from sqlalchemy.orm import Session
from models.group import Group
from schemas.group import GroupCreate

def create_group(db: Session, group: GroupCreate):
    db_group = Group(**group.dict())
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

def get_group(db: Session, group_id: int):
    return db.query(Group).filter(Group.id_group == group_id).first()

def get_groups(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Group).offset(skip).limit(limit).all()

def delete_group(db: Session, group_id: int):
    db_group = get_group(db, group_id)
    if db_group:
        db.delete(db_group)
        db.commit()
        return True
    return False
# def update_group(db: Session, group_id: int, group_data: GroupCreate):