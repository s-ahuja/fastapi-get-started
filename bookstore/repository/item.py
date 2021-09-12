from sqlalchemy.orm import Session
from bookstore.models.item import ItemModel
from bookstore.schemas.item import ItemSchemaCreate
from fastapi import HTTPException, status


class ItemRepository:

    @staticmethod
    def get_all(db: Session):
        items = db.query(ItemModel).all()
        return items

    @staticmethod
    def create(request: ItemSchemaCreate, db: Session):
        new_item = ItemModel(title=request.title, description=request.description)
        db.add(new_item)
        db.commit()
        db.refresh(new_item)
        return new_item

    @staticmethod
    def delete(id: int, db: Session):
        item = db.query(ItemModel).filter(ItemModel.id == id)

        if not item.first():
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with id {id} not found")

        item.delete(synchronize_session=False)
        db.commit()
        return {"detail": f"Item with id {id} deleted successfully"}

    @staticmethod
    def update(id: int, request: ItemSchemaCreate, db: Session):
        item = db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with id {id} not found")

        update_data = request.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(item, key, value) if value else None
        db.commit()
        db.refresh(item)
        return item

    @staticmethod
    def get(id: int, db: Session):
        item = db.query(ItemModel).filter(ItemModel.id == id).first()
        if not item:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                                detail=f"Item with id {id} not found")
        return item
