from sqlalchemy.orm import Session
from bookstore.models.item import ItemModel
from bookstore.schemas.item import ItemSchemaCreate
from fastapi import HTTPException, status


class ItemRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        items = self.db.query(ItemModel).all()
        return items

    def create(self, request: ItemSchemaCreate):
        new_item = ItemModel(title=request.title, description=request.description)
        self.db.add(new_item)
        self.db.commit()
        self.db.refresh(new_item)
        return new_item

    def delete(self, id: int):
        item = self.db.query(ItemModel).filter(ItemModel.id == id)

        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with id {id} not found")

        item.delete(synchronize_session=False)
        self.db.commit()
        return f"item with {id} deleted successfully"

    def update(self, id: int, request: ItemSchemaCreate):
        item = self.db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with id {id} not found")

        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(item, key, value) if value else None
        self.db.commit()
        self.db.refresh(item)
        return f"item with {id} updated successfully"

    def get(self, id: int):
        item = self.db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with the id {id} is not available")
        return item
