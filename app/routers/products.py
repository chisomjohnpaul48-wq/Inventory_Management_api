from fastapi import APIRouter, Depends, HTTPException
from app.database import get_connection
from app.services import new_product
from app.schemas.product import RequestModelCreateProduct, ResponseModelCreateProduct

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", status_code=201, response_model=ResponseModelCreateProduct)
def create_product_endpoint(product: RequestModelCreateProduct, connection=Depends(get_connection)):
    result = new_product(connection, product.name, product.description, product.price, product.quantity, product.movement_type)
    if not result:
        raise HTTPException(status_code=422, detail="missing fields")
    return result