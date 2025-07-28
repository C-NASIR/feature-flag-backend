from sqlalchemy import String, DateTime, func, text
from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from uuid import uuid4, UUID
from datetime import datetime
from typing import List

from src.db.base import Base


class Environment(Base):
    __tablename__ = 'environments'
    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    key: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text('now()'))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()"), onupdate=func.now()
    )

    flags: Mapped[List["Flag"]] = relationship(  # type: ignore
        back_populates="environment")
