from fastapi import HTTPException
from sqlalchemy.orm import Session
from uuid import UUID
from src.models import Segment
from src.schemas.segment import SegmentCreate, SegmentUpdate


def get_segments(db: Session):
    return db.query(Segment).all()


def get_segment(db: Session, id: UUID):
    segment = db.query(Segment).filter(Segment.id == id).first()
    if not segment:
        raise HTTPException(status_code=404, detail='Segment not found')
    return segment


def create_segment(db: Session, segment_in: SegmentCreate):
    segment = Segment(**segment_in.model_dump())
    db.add(segment)
    db.commit()
    db.refresh(segment)
    return segment


def update_segment(db: Session, id: UUID, segment_in: SegmentUpdate):
    segment = get_segment(db, id)
    for field, value in segment_in.model_dump(exclude_unset=True).items():
        setattr(segment, field, value)
    db.commit()
    db.refresh(segment)
    return segment


def delete_segment(db: Session, id: UUID):
    segment = get_segment(db, id)
    db.delete(segment)
    db.commit()
    return {'ok': True}
