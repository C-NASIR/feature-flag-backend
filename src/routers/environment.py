from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from src.db.session import get_db
from src.services import environment_service
from src.schemas.environment import (
    EnvCreate, EnvUpdate, EnvInDB
)
from src.schemas.flag import FlagCreate, FlagInDB
from src.services.flag_service import create_flag

router = APIRouter(prefix='/environments', tags=['Environment'])


@router.get('/', response_model=List[EnvInDB], status_code=200)
def get_environments(db: Session = Depends(get_db)):
    return environment_service.get_envs(db)


@router.get('/{id}', response_model=EnvInDB, status_code=200)
def get_environment(id: UUID, db: Session = Depends(get_db)):
    return environment_service.get_env(db, id)


@router.post('/', response_model=EnvInDB, status_code=201)
def create_environment(env: EnvCreate, db: Session = Depends(get_db)):
    return environment_service.create_env(db, env)


@router.put('/{id}', response_model=EnvInDB, status_code=200)
def update_environment(id: UUID, env_in: EnvUpdate, db: Session = Depends(get_db)):
    return environment_service.update_env(db, id, env_in)


@router.delete('/{id}', status_code=200)
def delete_environment(id, db: Session = Depends(get_db)):
    return environment_service.delete_env(db, id)


# Flag routes
@router.post('/{env_id}/flags', response_model=FlagInDB, status_code=201)
def create_environment(env_id: UUID, flag: FlagCreate, db: Session = Depends(get_db)):
    return create_flag(db, env_id, flag)


@router.get('/{id}/flags', response_model=List[FlagInDB], status_code=200)
def get_environment(id: UUID, db: Session = Depends(get_db)):
    return environment_service.get_env(db, id).flags
