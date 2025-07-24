from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from src.models.environment import Environment
from src.schemas.environment import (
    EnvironmentCreate, EnvironmentUpdate
)


def get_environments(db: Session):
    return db.query(Environment).all()


def get_environment(db: Session, id: UUID):
    env = db.query(Environment).filter(Environment.id == id).first()
    if not env:
        raise HTTPException(status_code=404, detail='Environment not found')
    return env


def create_environment(db: Session, env_in: EnvironmentCreate):
    env = Environment(**env_in.model_dump())
    db.add(env)
    db.commit()
    db.refresh(env)
    return env


def update_environment(db: Session, id: UUID, env_in: EnvironmentUpdate):
    env = get_environment(db, id)
    for field, value in env_in.model_dump(exclude_unset=True).items():
        setattr(env, field, value)
    db.commit()
    db.refresh(env)
    return env


def delete_environment(db: Session, id: UUID):
    env = get_environment(db, id)
    db.delete(env)
    return {"ok": True}
