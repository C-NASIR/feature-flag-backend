from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime


class SegmentBase(BaseModel):
    key: str
    name: str
    description: Optional[str] = None


class SegmentCreate(SegmentBase):
    pass


class SegmentUpdate(BaseModel):
    key: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None


class SegmentInDB(SegmentBase):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
