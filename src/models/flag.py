from sqlalchemy import String, Boolean, DateTime, ForeignKey, func, text
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import relationship, mapped_column, Mapped
from uuid import uuid4, UUID
from datetime import datetime
from typing import List

from src.db.base import Base


class Flag(Base):
    __tablename__ = "flags"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), primary_key=True, default=uuid4)
    key: Mapped[str] = mapped_column(String, unique=True, nullable=False)
    name: Mapped[str] = mapped_column(String, nullable=False)
    description: Mapped[str] = mapped_column(String, nullable=True)
    environment_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True), ForeignKey('environments.id'), nullable=False)
    default_variation: Mapped[str] = mapped_column(String, nullable=True)
    enabled: Mapped[bool] = mapped_column(Boolean, nullable=False)

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text('now()'))
    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=text("now()"), onupdate=func.now())

    environment: Mapped['Environment'] = relationship(  # type: ignore
        back_populates="flags")
    variations: Mapped[List['Variation']] = relationship(  # type: ignore
        back_populates='flag', cascade='all, delete-orphan')
    rules: Mapped[List['Rule']] = relationship(  # type: ignore
        back_populates='flag', cascade='all, delete-orphan')
