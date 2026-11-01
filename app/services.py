from app.repositories.product_repo import create_initial_product
from app.repositories.stock_movement_repo import add_stock_movement


def new_product(connection, name, description, price, quantity, movement_type):
    with connection.transaction():
        product = create_initial_product(connection, name, description, price, quantity)
        add_stock_movement(connection, product["id"], movement_type, product["quantity"], product["quantity"], "Initial product entry")
        return product