from sqlalchemy import Table, ForeignKey, DateTime, func, text
from sqlalchemy.orm import mapped_column
from sqlalchemy.dialects.postgresql import UUID
from src.db.base import Base

rule_segments = Table(
    "rule_segments",
    Base.metadata,
    mapped_column("rule_id", UUID(as_uuid=True),
                  ForeignKey("rules.id"), primary_key=True),
    mapped_column("segment_id", UUID(as_uuid=True),
                  ForeignKey("segments.id"), primary_key=True),
    mapped_column("created_at", DateTime(
        timezone=True), server_default=text('now()')),
    mapped_column("updated_at", DateTime(timezone=True),
                  server_default=text("now()"), onupdate=func.now()),
)
