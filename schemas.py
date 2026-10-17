from pydantic import BaseModel, Field
from datetime import datetime
from decimal import Decimal
from typing import Optional, List

class RequestModelStockCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: Decimal = Field(default=Decimal("0.0"), ge=Decimal("0.0"), description="Price must be Nonnegative.")
    quantity: int = Field(default=0, ge=0, description="Quantity must be Nonnegative.")

class StockItem(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    price: Decimal
    quantity: int
    created_at: datetime
    updated_at: datetime
    
class ResponseModelStockGet(BaseModel):
    Inventory: List[StockItem]

class RequestModelUpdateStock(BaseModel):
    name: Optional[str]
    description: Optional[str]
    price: Optional[int]
    quantity: Optional[int]