from typing import Optional
from app.models import Product, User
from app.init_db import get_db
from typing import List
from sqlalchemy.orm import Session


# db instance
db: Session = get_db()


# get specific product
def get_product_by_id(product_id: int) -> Optional[Product]:
    product = db.query(Product).filter(Product.id == product_id).first()
    return product

# get all product
def get_all_products() -> List[Product]:
    products = db.query(Product).all()
    return products

# create product
def create_product(user: User, name: str, price: float) -> Product:
    product = Product(name=name, price=price, created_by=user.id)
    db.add(product)
    db.commit()
    db.refresh(product)
    return product

# update product
def update_product(product: Product, name: Optional[str] = None, price: Optional[float] = None) -> Product:
    if name:
        product.name = name
    if price:
        product.price = price
    db.commit()
    db.refresh(product)
    return product

# delete product
def delete_product_by_id(product_id: int):
    db.query(Product).filter(Product.id == product_id).delete()
    db.commit()
    