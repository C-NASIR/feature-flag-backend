from sqlalchemy import String, ForeignKey, DateTime, func, text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from uuid import uuid4, UUID
from datetime import datetime
from typing import List

from src.db.base import Base
from src.models.rule_segment import rule_segments


class Rule(Base):
    __tablename__ = 'rules'
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    variation: Mapped[str] = mapped_column(String, nullable=False)
    priority: Mapped[int] = mapped_column(nullable=False)
    flag_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("flags.id"),
        nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text('now()'))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()"), onupdate=func.now())

    flag: Mapped["Flag"] = relationship(back_populates="rules")  # type: ignore
    conditions: Mapped[List["Condition"]] = relationship(        # type: ignore
        back_populates="rule", cascade="all, delete-orphan")
    segments: Mapped[List["Segment"]] = relationship(
        secondary=rule_segments, back_populates="rules"
    )
