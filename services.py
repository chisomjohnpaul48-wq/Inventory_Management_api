from decimal import Decimal
from sql_queries import add_new_stock, get_current_stocks, get_one_stock, delete_stock_by_id, update_stock

def new_stock(conn, name: str, description: str|None, price: Decimal, quantity: int):
    return add_new_stock(conn, name, description, price, quantity)

def get_stocks(conn):
    return get_current_stocks(conn)

def get_one_stock_service(conn, id: int):
    return get_one_stock(conn, id)

def delete_stock(conn, id: int):
    delete_stock_by_id(conn, id)
    conn.commit()

def update_stock_service(conn, id: int, dictionary: dict):
    allowed_input = {"name", "description", "price", "quantity"}
    dictionary = {k: v for k, v in dictionary.items() if k in allowed_input and v is not None}

    if not dictionary:
        return None

    set_clause = ", ".join([f"{k} = %s" for k in dictionary.keys()])
    values = list(dictionary.values()) + [id]

    result = update_stock(conn, values, set_clause)
    conn.commit()
    return result