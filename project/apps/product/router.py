from fastapi import APIRouter, HTTPException, Depends
from .schemas import ProductModel, ProductUpdateModel
from project.apps.authenticate.jwt import get_current_active_user
from project.apps.authenticate.models import User
from typing import List
from .crud import (
    get_product_by_id,
    get_all_products,
    create_product,
    update_product,
    delete_product_by_id,
)

"""
    endpoint descriptions
    CRUD for Product
    create project
    get all product (list project)
    get detail for product
    update project
    delete product

"""
router = APIRouter(prefix="/api/product", tags=["product"])


@router.get("/{product_id}", response_model=ProductModel)
def get_product_view(
    product_id: int, current_user: User = Depends(get_current_active_user)
):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product


@router.get("/", response_model=List[ProductModel])
def get_products_view(current_user: User = Depends(get_current_active_user)):
    products = get_all_products()
    return products


@router.post("/", response_model=ProductModel)
def create_product_view(
    product_create: ProductModel, current_user: User = Depends(get_current_active_user)
):
    product = create_product(user=current_user, **product_create.dict())
    return product


@router.put("/{product_id}", response_model=ProductModel)
def update_product_view(
    product_id: int,
    product_update: ProductUpdateModel,
    current_user: User = Depends(get_current_active_user),
):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="You are not allowed to update this product"
        )
    product = update_product(product, **product_update.dict())
    return product


@router.delete("/{product_id}")
def delete_product_view(
    product_id: int, current_user: User = Depends(get_current_active_user)
):
    product = get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    if product.user_id != current_user.id:
        raise HTTPException(
            status_code=403, detail="You are not allowed to delete this product"
        )
    delete_product_by_id(product_id)
    return {"message": "Product deleted successfully"}
