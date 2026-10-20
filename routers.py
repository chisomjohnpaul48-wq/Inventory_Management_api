from fastapi import APIRouter, Depends, HTTPException
from schemas import RequestModelStockCreate, ResponseModelStockGet, RequestModelUpdateStock, ResponseModelMovementsGet, Deleted
from services import new_stock, get_stocks, get_one_stock_service, delete_stock, update_stock_service
from services import get_movements_history_by_id, get_all_movements_history
from database import get_conn

router =  APIRouter()

@router.post("/stocks", status_code=201)
def new_stock_endpoint(stock: RequestModelStockCreate, conn=Depends(get_conn)):
    result = new_stock(conn, stock.name, stock.description, stock.price, stock.quantity)
    if not result:
        raise HTTPException(status_code=422, detail="Missing fields")
    return {"message": "Stock added successfully", "Stock info": result}

@router.get("/stocks", status_code=200, response_model=ResponseModelStockGet)
def get_stock_endpoint(conn=Depends(get_conn)):
    result = get_stocks(conn)
    if not result:
        raise HTTPException(status_code=401, detail="Not found.")
    return {"Inventory": result}

@router.get("/stocks/{id}", status_code=200)
def get_one_stock_endpoint(id: int, conn=Depends(get_conn)):
    result = get_one_stock_service(conn, id)
    if not result:
        raise HTTPException(status_code=404, detail="Stock not found.")
    return result

@router.delete("/stocks/{id}", status_code=200, response_model=Deleted)
def delete_stock_endpoint(id: int, conn=Depends(get_conn)):
    result = delete_stock(conn, id)
    if not result:
        raise HTTPException(status_code=404, detail="Stock not found.")
    return {"message": "Stock deleted successfully.", "Deleted_info": result}

@router.patch("/stocks/{id}", status_code=200)
def update_stock_endpoint(id: int, update: RequestModelUpdateStock, conn=Depends(get_conn)):
    update_info = update.model_dump(exclude_unset=True)
    result = update_stock_service(conn, id, update_info)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"message": "Stock updated successfully", "Updated info": result}

@router.get("/stocks/{id}/movements", status_code=200)
def get_movements_history_endpoint(id: int, conn=Depends(get_conn)):
    result =  get_movements_history_by_id(conn, stock_id=id)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"Movements": result}

@router.get("/movements", status_code=200, response_model=ResponseModelMovementsGet)
def get_all_movements_history_endpoint(conn=Depends(get_conn)):
    result = get_all_movements_history(conn)
    if not result:
        raise HTTPException(status_code=404, detail="Not found")
    return {"Movements": result}