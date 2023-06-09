from typing import Optional
from app.models import Product, User
from app.database import SessionLocal
from typing import List
from fastapi import Depends



# get specific product
def get_product_by_id(product_id: int) -> Optional[Product]:
    db = SessionLocal()
    product = db.query(Product).filter(Product.id == product_id).first()
    db.close()
    return product

# get all product
def get_all_products() -> List[Product]:
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

# create product
def create_product(user: User, name: str, price: float) -> Product:
    db = SessionLocal()
    product = Product(name=name, price=price, created_by=user.id)
    db.add(product)
    db.commit()
    db.refresh(product)
    db.close()
    return product

# update product
def update_product(product: Product, name: Optional[str] = None, price: Optional[float] = None) -> Product:
    db = SessionLocal()
    if name:
        product.name = name
    if price:
        product.price = price
    db.commit()
    db.refresh(product)
    db.close()
    return product

# delete product
def delete_product_by_id(product_id: int):
    db = SessionLocal()
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()
    db.close()
    