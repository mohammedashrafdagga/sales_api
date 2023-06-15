from project.db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL
from sqlalchemy.orm import relationship
import uuid


"""
    Product Model
    - id: integer
    - created_by: FK(User)
    - name:str
    - slug:uuid.UUID
    - price: decimal
    
"""


def generate_uuid():
    return str(uuid.uuid4())


class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True)
    slug = Column(String, name="uuid", unique=True, default=generate_uuid)
    price = Column(DECIMAL)
    created_by = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="products")
    sales = relationship("Sales", back_populates="product")

    def __repr__(self) -> str:
        return f"{self.name}"
