from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from src.db.session import get_db
from src.schemas.flag import FlagCreate, FlagUpdate, FlagInDB
from src.services import flag_service

router = APIRouter(prefix="/flags", tags=["Flags"])


@router.get("/", response_model=List[FlagInDB])
def list_flags(db: Session = Depends(get_db)):
    return flag_service.get_flags(db)


@router.get("/{flag_id}", response_model=FlagInDB)
def read_flag(flag_id: str, db: Session = Depends(get_db)):
    return flag_service.get_flag(db, flag_id)


@router.post("/", response_model=FlagInDB)
def create_flag(flag: FlagCreate, db: Session = Depends(get_db)):
    return flag_service.create_flag(db, flag)


@router.put("/{flag_id}", response_model=FlagInDB)
def update_flag(flag_id: str, flag_in: FlagUpdate, db: Session = Depends(get_db)):
    return flag_service.update_flag(db, flag_id, flag_in)


@router.delete("/{flag_id}")
def delete_flag(flag_id: str, db: Session = Depends(get_db)):
    return flag_service.delete_flag(db, flag_id)
