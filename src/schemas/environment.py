from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime


class EnvironmentBase(BaseModel):
    name: str


class EnvCreate(EnvironmentBase):
    pass


class EnvUpdate(BaseModel):
    name: Optional[str]


class EnvInDB(EnvironmentBase):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
