from sqlalchemy import Column, Integer, String, ForeignKey
from db import Base


# from sqlalchemy.orm import relationship

class ItemModel(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(length=20), nullable=False)
    description = Column(String(length=200), nullable=False)
    # tempcol = Column(String(length=20), nullable=False)
    # user_id = Column(Integer, ForeignKey('users.id'))
    # creator = relationship("User", back_populates="blogs")
