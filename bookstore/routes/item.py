from typing import List
from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from bookstore.repository.item import ItemRepository
from bookstore.schemas.item import ItemSchemaCreate, ItemSchemaFull, ItemSchemaResponse
from db import get_db

item_router = APIRouter(prefix="/item", tags=['Item'])
items_router = APIRouter(prefix="/items", tags=['Items'])

get_db = get_db


@items_router.get("/", response_model=List[ItemSchemaResponse])
def get_all(db: Session = Depends(get_db)):
    return ItemRepository.get_all(db)


@item_router.post('/', status_code=status.HTTP_201_CREATED, response_model=ItemSchemaFull)
def create(request: ItemSchemaCreate, db: Session = Depends(get_db)):
    y = ItemRepository.create(request, db)
    return y


@item_router.delete('/{id}', status_code=status.HTTP_202_ACCEPTED)
def delete(id: int, db: Session = Depends(get_db)):
    return ItemRepository.delete(id, db)


@item_router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: ItemSchemaCreate, db: Session = Depends(get_db)):
    return ItemRepository.update(id, request, db)


@item_router.get('/{id}', status_code=200, response_model=ItemSchemaFull)
def get(id: int, db: Session = Depends(get_db)):
    return ItemRepository.get(id, db)
