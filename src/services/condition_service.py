from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.condition import Condition
from src.schemas.condition import ConditionCreate, ConditionUpdate
from uuid import UUID


def get_condition(db: Session, id: UUID):
    condition = db.query(Condition).filter(Condition.id == id).first()
    if not condition:
        raise HTTPException(status_code=404, detail='condition not found')
    return condition


def get_conditions(db: Session):
    return db.query(Condition).all()


def create_condition(db: Session, rule_id: UUID, condition_in: ConditionCreate):
    condition = Condition(rule_id=rule_id, **condition_in.model_dump())
    db.add(condition)
    db.commit()
    db.refresh(condition)
    return condition


def update_condition(db: Session, id: UUID, condition_in: ConditionUpdate):
    condition = get_condition(db, id)
    for field, value in condition_in.model_dump(exclude_unset=True).items():
        setattr(condition, field, value)
    db.commit()
    db.refresh(condition)
    return condition


def delete_condition(db: Session, id: UUID):
    condition = get_condition(db, id)
    db.delete(condition)
    db.commit()
    return {'ok': True}
