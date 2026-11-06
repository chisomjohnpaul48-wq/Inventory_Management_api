from fastapi import APIRouter, Depends, HTTPException
from app.database import get_connection
from app.services import new_product
from app.schemas.product import RequestModelCreateProduct, ResponseModelCreateProduct

router = APIRouter(prefix="/products", tags=["Products"])

@router.post("/", status_code=201, response_model=ResponseModelCreateProduct)
def create_product_endpoint(product: RequestModelCreateProduct, connection=Depends(get_connection)):
    return new_product(connection, product.name, product.description, product.price, product.quantity)
    