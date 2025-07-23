from sqlalchemy.orm import Session
from fastapi import HTTPException
from src.models.flag import Flag
from src.schemas.flag import FlagCreate, FlagUpdate

def get_flags(db: Session):
    return db.query(Flag).all()

def get_flag(db: Session, flag_id):
    flag = db.query(Flag).filter(Flag.id == flag_id).first()
    if not flag:
        raise HTTPException(status_code=404, detail="Flag not found")
    return flag

def create_flag(db: Session, flag_in: FlagCreate):
    db_flag = Flag(**flag_in.dict())
    db.add(db_flag)
    db.commit()
    db.refresh(db_flag)
    return db_flag

def update_flag(db: Session, flag_id, flag_in: FlagUpdate):
    flag = get_flag(db, flag_id)
    for field, value in flag_in.dict(exclude_unset=True).items():
        setattr(flag, field, value)
    db.commit()
    db.refresh(flag)
    return flag

def delete_flag(db: Session, flag_id):
    flag = get_flag(db, flag_id)
    db.delete(flag)
    db.commit()
    return {"ok": True}