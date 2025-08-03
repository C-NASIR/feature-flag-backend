from pydantic import BaseModel, UUID4
from typing import Optional, List
from datetime import datetime
from .condition import ConditionCreate, ConditionInDB


class RuleBase(BaseModel):
    priority: int
    variation: str
    conditions: Optional[List[ConditionCreate]]


class RuleCreate(RuleBase):
    pass


class RuleUpdate(BaseModel):
    variation: Optional[str] = None
    priority: Optional[int] = None


class RuleInDB(RuleBase):
    id: UUID4
    flag_id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
