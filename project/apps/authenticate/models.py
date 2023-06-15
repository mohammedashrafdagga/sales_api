from project.db.database import Base
from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import relationship


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
