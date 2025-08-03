from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.rule import Rule
from src.schemas.rule import RuleCreate, RuleUpdate
from uuid import UUID


def get_rules(db: Session):
    return db.query(Rule).all()


def get_rule(db: Session, id: UUID):
    rule = db.query(Rule).filter(Rule.id == id).first()
    if not rule:
        raise HTTPException(status_code=404, detail='rule not found')
    return rule


def create_rule(db: Session, flag_id: UUID, rule_in: RuleCreate):
    rule = Rule(flag_id=flag_id, **rule_in.model_dump())
    db.add(rule)
    db.commit()
    db.refresh(rule)
    return rule


def update_rule(db: Session, id: UUID, rule_in: RuleUpdate):
    rule = get_rule(db, id)
    for field, value in rule_in.model_dump(exclude_unset=True).items():
        setattr(rule, field, value)
    db.commit()
    db.refresh(rule)
    return rule


def delete_rule(db: Session, id: UUID):
    rule = get_rule(db, id)
    db.delete(rule)
    db.commit()
    return {'ok': True}
