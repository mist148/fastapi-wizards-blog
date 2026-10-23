from decimal import Decimal

from pydantic import BaseModel, ConfigDict, Field

class ProductCreate(BaseModel):
    name : str
    price : Decimal = Field(gt=0, decimal_places=2)


