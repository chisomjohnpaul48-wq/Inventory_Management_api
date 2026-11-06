from pydantic import BaseModel, Field, StringConstraints, field_validator
from typing import Optional, Annotated
from decimal import Decimal
from datetime import datetime


NonEmptyStr = Annotated[str, StringConstraints(strip_whitespace=True, min_length=1, max_length=100)]

PriceConstraint = Annotated[Decimal, Field(ge=Decimal("0.00"), max_digits=10, decimal_places=2)]

DescriptionConstraint = Annotated[Optional[str], StringConstraints(strip_whitespace=True, min_length=1, max_length=500)]
class RequestModelCreateProduct(BaseModel):
    name: NonEmptyStr
    description: DescriptionConstraint = None
    price: PriceConstraint
    quantity: int = Field(default=0, ge=0, le=1_000_000, description="Quantity must be nonnegative.")

    @field_validator("description", mode="before")
    @classmethod
    def no_empty_str(cls, value: str | None):
        if value is None:
            return None
        
        if isinstance(value, str) and not value.strip():
            return None

        return value or None

class ResponseModelCreateProduct(BaseModel):
    id: int
    name: NonEmptyStr
    description: DescriptionConstraint
    price: Decimal
    quantity: int
    created_at: datetime
    message: str = "Product added successfully"