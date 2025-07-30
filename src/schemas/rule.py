from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime


class RuleBase(BaseModel):
    variation: str
    priority: int


class RuleCreate(RuleBase):
    pass


class RuleUpdate(BaseModel):
    variation: Optional[str] = None
    priority: Optional[int] = None


class RuleInDB(BaseModel):
    id: UUID4
    flag_id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
