from pydantic import BaseModel

class ItemSchemaResponse(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True

class ItemSchemaCreate(ItemSchemaResponse):
    pass

class ItemSchemaFull(ItemSchemaResponse):
    id: int
