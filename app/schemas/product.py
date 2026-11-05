from pydantic import BaseModel, Field
from typing import Optional
from decimal import Decimal
from app.schemas.stock_movement import MovementType
from datetime import datetime

class RequestModelCreateProduct(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(default=Decimal("0.0"), ge=Decimal("0.0"), description="Price must be Nonnegative.")
    quantity: int = Field(default=0, ge=0, description="Quantity must be nonnegative.")
    movement_type: MovementType = MovementType.OPENING_BALANCE

class ResponseModelCreateProduct(BaseModel):
    name: str
    description: Optional[str] = "NULL"
    price: Decimal = Field(default=Decimal("0.0"), ge=Decimal("0.0"), description="Price must be Nonnegative.")
    quantity: int = Field(default=0, ge=0, description="Quantity must be nonnegative.")
    created_at: datetime
    message: str = "Product added sucessfully"