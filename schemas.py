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
    name: Optional[str] = None
    description: Optional[str] = None
    price: Optional[Decimal] = Field(default=None, ge=Decimal("0.0"), description="Price must be Nonnegative.")
    quantity: Optional[int] = Field(default=None, ge=0, description="Quantity must be Nonnegative.")

class MovementItem(BaseModel):
    id: int
    stock_id: int
    movement_type: str
    quantity_change: int
    new_quantity: int
    reason: Optional[str] = None
    created_at: datetime

class ResponseModelMovementsGet(BaseModel):
    Movements: List[MovementItem]

class Deleted(BaseModel):
    message: str
    Deleted_info: StockItem