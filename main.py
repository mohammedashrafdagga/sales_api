from fastapi import FastAPI
from routers.authenticate_endpoint import router as authenticate_router
from routers.products_endpoint import router as product_router
from routers.sales_endpoint import router as sales_router
# app instance from fastapi
app = FastAPI()


# index home
@app.get('/')
def index():
    return "Hello into Mini Sales  System"


# connect router here
app.include_router(authenticate_router)
app.include_router(product_router)
app.include_router(sales_router)