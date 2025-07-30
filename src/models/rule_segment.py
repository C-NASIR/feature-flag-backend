from sqlalchemy import Column, Table, ForeignKey, text, DateTime, func
from sqlalchemy.dialects.postgresql import UUID

from src.db.base import Base

rule_segments = Table(
    "rule_segments",
    Base.metadata,
    Column("rule_id", UUID(as_uuid=True),
           ForeignKey("rules.id"), primary_key=True),
    Column("segment_id", UUID(as_uuid=True),
           ForeignKey("segments.id"), primary_key=True),
    Column("created_at", DateTime(timezone=True),
           server_default=text("now()")),
    Column("updated_at", DateTime(timezone=True),
           server_default=text("now()"), onupdate=func.now()),
)
