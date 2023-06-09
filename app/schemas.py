from pydantic import BaseModel


# Token Model
class Token(BaseModel):
    access_token :str
    token_type: str
    
# Token Data Model
class TokenData(BaseModel):
    username: str or None = None
    
    
# For User
class UserLogin(BaseModel):
    username: str
    password: str
    
    class Config:
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    username: str
    class Config:
        orm_mode = True
    
    
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
   