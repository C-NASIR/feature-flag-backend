from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID
from src.db.session import get_db
from src.schemas.segment import SegmentInDB, SegmentCreate, SegmentUpdate
from src.services import segment_service

router = APIRouter(prefix='/segments', tags=['Segment'])


@router.get('/', response_model=list[SegmentInDB], status_code=200)
def get_segments(db: Session = Depends(get_db)):
    return segment_service.get_segments(db)


@router.get('/{id}', response_model=SegmentInDB, status_code=200)
def get_segment(id: UUID, db: Session = Depends(get_db)):
    return segment_service.get_segment(db, id)


@router.post('/', response_model=SegmentInDB, status_code=201)
def create_segment(segment_in: SegmentCreate, db: Session = Depends(get_db)):
    return segment_service.create_segment(db, segment_in)


@router.put('/{id}', response_model=SegmentInDB)
def update_segment(id: UUID, segment_in: SegmentUpdate, db: Session = Depends(get_db)):
    return segment_service.update_segment(db, id, segment_in)


@router.delete('/{id}', status_code=204)
def delete_segment(id: UUID, db: Session = Depends(get_db)):
    return segment_service.delete_segment(db, id)
