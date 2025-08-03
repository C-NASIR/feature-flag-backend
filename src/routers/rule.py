from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from src.schemas.rule import RuleUpdate, RuleInDB
from src.schemas.rule import ConditionCreate, ConditionInDB
from src.services import rule_service, condition_service
from src.db.session import get_db

router = APIRouter(prefix='/rules', tags=['Rules'])


@router.get('/{id}', response_model=RuleInDB, status_code=200)
def get_rule(id: UUID, db: Session = Depends(get_db)):
    return rule_service.get_rule(db, id)


@router.put('/{id}', response_model=RuleInDB, status_code=200)
def update_rule(id: UUID, rule_in: RuleUpdate, db: Session = Depends(get_db)):
    return rule_service.update_rule(db, id, rule_in)


@router.delete('/{id}', status_code=200)
def delete_rule(id: UUID, db: Session = Depends(get_db)):
    return rule_service.delete_rule(db, id)


# conditions routes


@router.post("/{rule_id}/conditions", response_model=ConditionInDB, status_code=201)
def create_condition(rule_id: UUID, cond: ConditionCreate, db: Session = Depends(get_db)):
    return condition_service.create_condition(db, rule_id, cond)


@router.get("/{rule_id}/conditions", response_model=List[ConditionInDB], status_code=200)
def get_conditions(rule_id: UUID, db: Session = Depends(get_db)):
    return rule_service.get_rule(db, rule_id).conditions
