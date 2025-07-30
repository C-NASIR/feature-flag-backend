from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime
from src.schemas.flag import FlagCreate, FlagInDB


class EnvironmentBase(BaseModel):
    key: str
    name: Optional[str]


class EnvCreate(EnvironmentBase):
    pass


class EnvUpdate(BaseModel):
    key: Optional[str] = None
    name: Optional[str] = None


class EnvInDB(EnvironmentBase):
    id: UUID4
    key: str
    name: Optional[str]
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
