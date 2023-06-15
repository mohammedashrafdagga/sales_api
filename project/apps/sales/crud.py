from project.db.database import SessionLocal
from .models import Sales
from typing import List, Optional
from datetime import date
from sqlalchemy.sql import func


def create_sale(
    buyer: str, created_by: int, product_id: int, quantity: int, total_price: float
) -> Sales:
    db = SessionLocal()
    sale = Sales(
        buyer=buyer,
        created_by=created_by,
        product_id=product_id,
        quantity=quantity,
        total_price=total_price,
    )
    db.add(sale)
    db.commit()
    db.refresh(sale)
    db.close()
    return sale


def get_all_sales() -> List[Sales]:
    db = SessionLocal()
    sales = db.query(Sales).all()
    db.close()
    return sales


def get_sale_by_id(sale_id: int) -> Optional[Sales]:
    db = SessionLocal()
    sale = db.query(Sales).filter(Sales.id == sale_id).first()
    db.close()
    return sale


def get_sales_by_date(sale_date: date) -> List[Sales]:
    db = SessionLocal()
    sales = db.query(Sales).filter(func.date(Sales.date) == sale_date).all()
    db.close()
    return sales


def get_sales_in_date_range(start_date: date, end_date: date) -> List[Sales]:
    db = SessionLocal()
    sales = (
        db.query(Sales)
        .filter(func.date(Sales.date).between(start_date, end_date))
        .all()
    )
    db.close()
    return sales


def get_sales_by_product(product_id: int) -> List[Sales]:
    db = SessionLocal()
    sales = db.query(Sales).filter(Sales.product_id == product_id).all()
    db.close()
    return sales
