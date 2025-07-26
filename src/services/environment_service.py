from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from src.models.environment import Environment
from src.schemas.environment import (
    EnvCreate, EnvUpdate
)


def get_envs(db: Session):
    return db.query(Environment).all()


def get_env(db: Session, id: UUID):
    env = db.query(Environment).filter(Environment.id == id).first()
    if not env:
        raise HTTPException(status_code=404, detail='Environment not found')
    return env


def create_env(db: Session, env_in: EnvCreate):
    env = Environment(**env_in.model_dump())
    db.add(env)
    db.commit()
    db.refresh(env)
    return env


def update_env(db: Session, id: UUID, env_in: EnvUpdate):
    env = get_env(db, id)
    for field, value in env_in.model_dump(exclude_unset=True).items():
        setattr(env, field, value)
    db.commit()
    db.refresh(env)
    return env


def delete_env(db: Session, id: UUID):
    env = get_env(db, id)
    db.delete(env)
    db.commit()
    return {"ok": True}
