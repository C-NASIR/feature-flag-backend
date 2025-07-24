from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import uuid4
from src.schemas.variation import VariationCreate, VariationUpdate, VariationInDB
from src.services import variation_service
from src.db.session import get_db

router = APIRouter(prefix='/variation', tags=['Variation'])


@router.get('/', response_model=List[VariationInDB])
def get_variations(db: Session = Depends(get_db)):
    return variation_service.get_variations(db)


@router.get('/{id}', response_model=VariationInDB)
def get_variation(id: uuid4, db: Session = Depends(get_db)):
    return variation_service.get_variation(db, id)


@router.post('/', response_model=VariationInDB)
def create_variation(variation_in: VariationCreate, db: Session = Depends(get_db)):
    return variation_service.create_variation(db, variation_in)


@router.put('/{id}', response_model=VariationInDB)
def update_variation(id: uuid4, variation_in: VariationUpdate, db: Session = Depends(get_db)):
    return variation_service.update_variation(db, id, variation_in)


@router.delete('/{id}')
def delete_variation(id: uuid4, db: Session = Depends(get_db)):
    return variation_service.delete_variation(db, id)
