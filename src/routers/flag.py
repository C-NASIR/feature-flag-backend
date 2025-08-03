from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from typing import List
from src.db.session import get_db
from src.schemas.flag import FlagCreate, FlagUpdate, FlagInDB
from src.schemas.variation import VariationCreate, VariationInDB
from src.schemas.rule import RuleCreate, RuleUpdate, RuleInDB
from src.services import flag_service, variation_service, rule_service

router = APIRouter(prefix="/flags", tags=["Flags"])


@router.get("/{id}", response_model=FlagInDB, status_code=200)
def read_flag(id: UUID, db: Session = Depends(get_db)):
    return flag_service.get_flag(db, id)


@router.put("/{id}", response_model=FlagInDB, status_code=200)
def update_flag(id: UUID, flag_in: FlagUpdate, db: Session = Depends(get_db)):
    return flag_service.update_flag(db, id, flag_in)


@router.delete("/{id}", status_code=200)
def delete_flag(id: UUID, db: Session = Depends(get_db)):
    return flag_service.delete_flag(db, id)

# variation routes


@router.post("/{flag_id}/variations", response_model=VariationInDB, status_code=201)
def create_variation(var: VariationCreate, flag_id: UUID, db: Session = Depends(get_db)):
    return variation_service.create_variation(db, flag_id, var)


@router.get("/{flag_id}/variations", response_model=List[VariationInDB], status_code=200)
def get_variations(flag_id: UUID, db: Session = Depends(get_db)):
    return flag_service.get_flag(db, flag_id).variations

# rule routes


@router.post("/{flag_id}/rules", response_model=RuleInDB, status_code=201)
def create_variation(rule: RuleCreate, flag_id: UUID, db: Session = Depends(get_db)):
    return rule_service.create_rule(db, flag_id, rule)


@router.get("/{flag_id}/rules", response_model=List[RuleInDB], status_code=200)
def get_rules(flag_id: UUID, db: Session = Depends(get_db)):
    return flag_service.get_flag(db, flag_id).rules
