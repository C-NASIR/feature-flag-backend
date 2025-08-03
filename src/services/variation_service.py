from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.models.variation import Variation
from src.schemas.variation import VariationCreate, VariationUpdate
from uuid import UUID


def get_variations(db: Session):
    return db.query(Variation).all()


def get_variation(db: Session, id: UUID):
    variation = db.query(Variation).filter(Variation.id == id).first()
    if not variation:
        raise HTTPException(status_code=404, detail='variation not found')
    return variation


def create_variation(db: Session, flag_id: UUID, variation_in: VariationCreate):
    variation = Variation(flag_id=flag_id, **variation_in.model_dump())
    db.add(variation)
    db.commit()
    db.refresh(variation)
    return variation


def update_variation(db: Session, id: UUID, variation_in: VariationUpdate):
    variation = get_variation(db, id)
    for field, value in variation_in.model_dump(exclude_unset=True).items():
        setattr(variation, field, value)
    db.commit()
    db.refresh(variation)
    return variation


def delete_variation(db: Session, id: UUID):
    variation = get_variation(db, id)
    db.delete(variation)
    db.commit()
    return {'ok': True}
