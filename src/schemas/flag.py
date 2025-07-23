from pydantic import BaseModel, UUID4
from typing import Optional
from datetime import datetime

class FlagBase(BaseModel):
    key: str
    name: str
    description: Optional[str] = None
    enabled: bool = False

class FlagCreate(FlagBase):
    pass

class FlagUpdate(BaseModel):
    name: Optional[str]
    description: Optional[str]
    enabled: Optional[bool]

class FlagInDB(FlagBase):
    id: UUID4
    created_at: datetime
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True 
