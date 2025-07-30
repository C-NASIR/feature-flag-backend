
from sqlalchemy import String, DateTime, func, text
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, TEXT
from uuid import uuid4, UUID
from datetime import datetime
from typing import List

from src.db.base import Base
from src.models.rule_segment import rule_segments


class Segment(Base):
    __tablename__ = 'segments'
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    key: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(TEXT, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text('now()'))

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=text("now()"),
        onupdate=func.now())

    rules: Mapped[List["Rule"]] = relationship(
        secondary=rule_segments,
        back_populates="segments"
    )
