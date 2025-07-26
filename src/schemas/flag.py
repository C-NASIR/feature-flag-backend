# src/schemas/flag.py

from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional


class FlagBase(BaseModel):
    key: str = Field(..., max_length=100)
    name: str = Field(..., max_length=100)
    environment_id: UUID
    description: Optional[str] = None
    default_variation: str
    enabled: bool = False


class FlagCreate(FlagBase):
    pass


class FlagUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    default_variation: Optional[str] = None
    enabled: Optional[bool] = None


class FlagInDB(FlagBase):
    id: UUID
    created_at: datetime
    updated_at: Optional[datetime] = None

    model_config = {'from_attributes': True}


class FlagResponse(FlagInDB):
    pass
