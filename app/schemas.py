from pydantic import BaseModel


# For User
class UserLogin(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True

class User(UserLogin):
    name: str
    email: str
    
    
# For Product
class Product(BaseModel):
    created_by: int # with User
    name: str
    price: str
    class Config:
        orm_mode = True
   
   
# Sales 
class Product(BaseModel):
    created_by: int # with User
    product_id: int # with Product
    buyer: str or None = None
    quantity: int

    class Config:
        orm_mode = True
   