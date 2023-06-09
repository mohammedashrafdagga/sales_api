from fastapi import FastAPI
from routers.authenticate_endpoint import router as authenticate_router
# app instance from fastapi
app = FastAPI()


# index home
@app.get('/')
def index():
    return "Hello into Mini Sales  System"


# connect router here
app.include_router(authenticate_router)