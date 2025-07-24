from pydantic import BaseModel, UUID4
from typing import Optional, Dict, List, Union, Any
from datetime import datetime

JsonValue = Union[str, int, float, bool, None, Dict[str, Any], List[Any]]


class VariationBase(BaseModel):
    value: JsonValue
    description: Optional[str] = None


class VariationCreate(VariationBase):
    pass


class VariationUpdate(BaseModel):
    value: Optional[JsonValue]
    description: Optional[str]


class VariationInDB(BaseModel):
    id: UUID4
    flag_id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    model_config = {'from_attributes': True}
