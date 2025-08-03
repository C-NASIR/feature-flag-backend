from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from src.schemas.condition import ConditionUpdate, ConditionInDB
from src.services import condition_service
from src.db.session import get_db

router = APIRouter(prefix='/conditions', tags=['Conditions'])


@router.get('/{id}', response_model=ConditionInDB, status_code=200)
def get_condition(id: UUID, db: Session = Depends(get_db)):
    return condition_service.get_condition(db, id)


@router.put('/{id}', response_model=ConditionInDB, status_code=200)
def update_condition(id: UUID, condition_in: ConditionUpdate, db: Session = Depends(get_db)):
    return condition_service.update_condition(db, id, condition_in)


@router.delete('/{id}', status_code=200)
def delete_condition(id: UUID, db: Session = Depends(get_db)):
    return condition_service.delete_condition(db, id)
