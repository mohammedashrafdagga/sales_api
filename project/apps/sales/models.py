from project.db.database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    DECIMAL,
    DateTime,
)
from sqlalchemy.orm import relationship
from datetime import datetime

"""
    Sales Model
    - id: integer
    - product: FK(product)
    - quantity:integer
    - total_price: DECIMAL
    - date_of_create
    - user: charfield (Buyer)
    - create_by => superuser seller
    
"""


class Sales(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    buyer = Column(String, nullable=True)
    created_by = Column(Integer, ForeignKey("users.id"))
    product_id = Column(Integer, ForeignKey("products.id"))
    quantity = Column(Integer, default=1)
    total_price = Column(DECIMAL)
    date = Column(DateTime, default=datetime.utcnow)

    seller = relationship("User", back_populates="user_sales")
    product = relationship("Product", back_populates="sales")

    def __repr__(self) -> str:
        return f"Sales Number: {self.id}"
