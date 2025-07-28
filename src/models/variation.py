from sqlalchemy import String, DateTime, ForeignKey, func, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID, JSONB
from uuid import uuid4, UUID
from datetime import datetime

from src.db.base import Base


class Variation(Base):
    __tablename__ = 'variations'

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    key: Mapped[str] = mapped_column(String, nullable=False)
    flag_id: Mapped[UUID] = mapped_column(PG_UUID(as_uuid=True), ForeignKey(
        'flags.id', ondelete='CASCADE'), nullable=False)
    value: Mapped[JSONB] = mapped_column(JSONB, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text('now()'))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()"), onupdate=func.now())

    flag: Mapped["Flag"] = relationship(            # type: ignore
        back_populates="variations")
