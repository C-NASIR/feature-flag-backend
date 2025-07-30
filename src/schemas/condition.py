from pydantic import BaseModel, UUID4
from datetime import datetime
from typing import Optional


class ConditionBase(BaseModel):
    attrbiute: str
    operator: int
    value: str


class ConditionCreate(ConditionBase):
    pass


class ConditionUpdate(BaseModel):
    attrbiute: Optional[str]
    operator: Optional[int]
    value: Optional[str]


class ConditionInDB(BaseModel):
    id: UUID4
    rule_id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
