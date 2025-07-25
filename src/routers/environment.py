from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from src.db.session import get_db
from src.services import environment_service
from src.schemas.environment import (
    EnvironmentCreate, EnvironmentUpdate, EnvironmentInDB
)

router = APIRouter(prefix='/environments', tags=['Environment'])


@router.get('/', response_model=List[EnvironmentInDB])
def get_environments():
    return environment_service.get_environments()


@router.get('/{env_id}', response_model=EnvironmentInDB)
def get_environment(id: UUID, db: Session = Depends(get_db)):
    return environment_service.get_environment(db, id)


@router.post('/', response_model=EnvironmentInDB)
def create_environment(env: EnvironmentCreate, db: Session = Depends(get_db)):
    return environment_service.create_environment(db, env)


@router.put('/{id}', response_model=EnvironmentInDB)
def update_environment(id: UUID, env_in: EnvironmentUpdate, db: Session = Depends(get_db)):
    return environment_service.update_environment(db, id, env_in)


@router.delete('/{env_id}')
def delete_environment(id, db: Session = Depends(get_db)):
    return environment_service.delete_environment(db, id)
