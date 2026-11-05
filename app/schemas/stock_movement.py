from enum import Enum

class MovementType(str, Enum):
    RECEIPT = "receipt"
    SALE = "sale"
    ADJUSTMENT = "adjustment"
    RETURN = "return"
    DAMAGE = "damage"
    OPENING_BALANCE = "opening balance"