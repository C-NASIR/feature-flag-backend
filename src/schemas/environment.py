from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime


class EnvironmentBase(BaseModel):
    name: str
    description: Optional[str]


class EnvironmentCreate(EnvironmentBase):
    pass


class EnvironmentUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]


class EnvironmentInDB(EnvironmentBase):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
