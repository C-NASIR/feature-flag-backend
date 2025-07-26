from sqlalchemy import Column, String, DateTime, ForeignKey
from sqlalchemy.dialects.postgresql import UUID, JSONB
from sqlalchemy.sql import func
from uuid import uuid4

from src.db.base import Base


class Variation(Base):
    __tablename__ = 'variations'

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid4)
    key = Column(String, nullable=False)
    flag_id = Column(UUID(as_uuid=True), ForeignKey(
        'flags.id', ondelete='CASCADE'), nullable=False)

    value = Column(JSONB, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())
