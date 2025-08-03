from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional


class ConditionBase(BaseModel):
    attribute: str
    operator: str
    value: str


class ConditionCreate(ConditionBase):
    pass


class ConditionUpdate(BaseModel):
    attribute: Optional[str] = None
    operator: Optional[str] = None
    value: Optional[str] = None


class ConditionInDB(ConditionBase):
    id: UUID4
    rule_id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
