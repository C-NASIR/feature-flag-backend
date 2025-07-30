from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime
from typing import Optional, List


class FlagBase(BaseModel):
    key: str
    name: str
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
    environment_id: UUID
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None

    model_config = {'from_attributes': True}


class FlagsInDB(BaseModel):
    flags: Optional[List[FlagInDB]]
