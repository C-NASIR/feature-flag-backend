from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from src.db.session import get_db
from src.schemas.flag import FlagCreate, FlagUpdate, FlagInDB
from src.services import flag_service

router = APIRouter(prefix="/flags", tags=["Flags"])


@router.get("/", response_model=List[FlagInDB])
def list_flags(db: Session = Depends(get_db)):
    return flag_service.get_flags(db)


@router.get("/{id}", response_model=FlagInDB)
def read_flag(id: UUID, db: Session = Depends(get_db)):
    return flag_service.get_flag(db, id)


@router.post("/", response_model=FlagInDB)
def create_flag(flag: FlagCreate, db: Session = Depends(get_db)):
    return flag_service.create_flag(db, flag)


@router.put("/{id}", response_model=FlagInDB)
def update_flag(id: UUID, flag_in: FlagUpdate, db: Session = Depends(get_db)):
    return flag_service.update_flag(db, id, flag_in)


@router.delete("/{id}")
def delete_flag(id: UUID, db: Session = Depends(get_db)):
    return flag_service.delete_flag(db, id)
