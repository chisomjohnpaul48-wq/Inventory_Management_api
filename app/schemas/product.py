from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal

class RequestModelCreateProduct(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(default=Decimal("0.0"), ge=Decimal("0.0"), description="Price must be Nonnegative.")
    quantity: int = Field(default=0, ge=0, description="Quantity must be nonnegative.")
