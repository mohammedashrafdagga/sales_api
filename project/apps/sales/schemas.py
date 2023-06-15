from pydantic import BaseModel


# Sales
class SalesModel(BaseModel):
    buyer: str or None = None
    quantity: int
    total_price: float or None = None

    class Config:
        orm_mode = True
