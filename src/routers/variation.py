from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from uuid import UUID
from src.schemas.variation import VariationCreate, VariationUpdate, VariationInDB
from src.services import variation_service
from src.db.session import get_db

router = APIRouter(prefix='/variations', tags=['Variation'])


@router.get('/', response_model=List[VariationInDB], status_code=200)
def get_variations(db: Session = Depends(get_db)):
    return variation_service.get_variations(db)


@router.get('/{id}', response_model=VariationInDB, status_code=200)
def get_variation(id: UUID, db: Session = Depends(get_db)):
    return variation_service.get_variation(db, id)


@router.post('/', response_model=VariationInDB, status_code=201)
def create_variation(variation_in: VariationCreate, db: Session = Depends(get_db)):
    return variation_service.create_variation(db, variation_in)


@router.put('/{id}', response_model=VariationInDB, status_code=200)
def update_variation(id: UUID, variation_in: VariationUpdate, db: Session = Depends(get_db)):
    return variation_service.update_variation(db, id, variation_in)


@router.delete('/{id}', status_code=200)
def delete_variation(id: UUID, db: Session = Depends(get_db)):
    return variation_service.delete_variation(db, id)
