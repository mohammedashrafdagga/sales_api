from database import Base
from sqlalchemy import (
    Column,
    Integer,
    String,
    ForeignKey,
    Text,
    Boolean,
    DECIMAL,
    DateTime,
)
from sqlalchemy.orm import relationship
import uuid
from datetime import datetime

"""
    User Model
    - id: int
    - name: str
    - email: str
    - username: str
    - password: str
    - is_superuser: bool
    - is_active: bool
"""


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    name = Column(String)
    password = Column(Text)
    is_superuser = Column(Boolean, default=False)
    is_active = Column(Boolean, default=False)

    # relationship
    products = relationship("Product", back_populates="user")
    user_sales = relationship("Sales", back_populates="seller")

    def __repr__(self) -> str:
        return f"{self.username}"


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
