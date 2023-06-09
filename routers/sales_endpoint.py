from fastapi import APIRouter, Depends, HTTPException
from app.models import User
from app.schemas import SalesModel
from app.jwt import get_current_active_user
from crud.product import get_product_by_id
from crud.sales import create_sale, get_all_sales, get_sales_by_product, get_sales_in_date_range, get_sales_by_date, get_sale_by_id
from typing import List
from datetime import date
'''
endpoint for sales 
- adding sales for product
- get all sales (for all product)
- get all sales depend in day date
- get all sales from date to date
- get all sales for specific product 
'''

router = APIRouter(
    prefix='/api/sales',
    tags= ['sales']
)

@router.post("/create/<product_id:int>", response_model=SalesModel)
def create_sale_view(
    product_id:int,
    sale_create: SalesModel,
    current_user: User = Depends(get_current_active_user),
):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    total_price = product.price * sale_create.quantity

    sale = create_sale(
        buyer=sale_create.buyer,
        created_by=current_user.id,
        product_id=product_id,
        quantity=sale_create.quantity,
        total_price=total_price,
    )
    return sale

@router.get("/", response_model=List[SalesModel])
def get_all_sales_view( current_user: User = Depends(get_current_active_user),):
    sales = get_all_sales()
    return sales

@router.get("/{sale_id}", response_model=SalesModel)
def get_sale_view(sale_id: int,  current_user: User = Depends(get_current_active_user),):
    sale = get_sale_by_id(sale_id)
    if not sale:
        raise HTTPException(status_code=404, detail="Sale not found")
    return sale

@router.get("/date/{sale_date}", response_model=List[SalesModel])
def get_sales_by_date_view(sale_date: date,  current_user: User = Depends(get_current_active_user),):
    sales = get_sales_by_date(sale_date)
    return sales

@router.get("/date-range", response_model=List[SalesModel])
def get_sales_in_date_range_view(start_date: date, end_date: date,  current_user: User = Depends(get_current_active_user),):
    sales = get_sales_in_date_range(start_date, end_date)
    return sales

@router.get("/product/{product_id}", response_model=List[SalesModel])
def get_sales_by_product_view(product_id: int,  current_user: User = Depends(get_current_active_user),):
    sales = get_sales_by_product(product_id)
    return sales
