from pydantic import BaseModel


# For Product
class ProductModel(BaseModel):
    name: str
    price: float

    class Config:
        orm_mode = True


class ProductUpdateModel(BaseModel):
    name: str or None = None
    price: float or None = None

    class Config:
        orm_mode = True
