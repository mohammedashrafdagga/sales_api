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

class UserModel(BaseModel):
    name: str
    email: str
    username: str
    class Config:
        orm_mode = True
    
class UserCreateSuperuser(UserModel):
    password: str
    is_superuser: bool or None = True
    is_active: bool or None = True
    class Config:
        orm_mode = True

# For Product
class ProductModel(BaseModel):
    created_by: int or None = None # with User
    name: str
    price: str
    class Config:
        orm_mode = True
   
   
class ProductUpdateModel(BaseModel):
    name: str or None = None
    price: str or None = None
    class Config:
        orm_mode = True
# Sales 
class SalesModel(BaseModel):
    created_by: int # with User
    product_id: int # with Product
    buyer: str or None = None
    quantity: int

    class Config:
        orm_mode = True
   