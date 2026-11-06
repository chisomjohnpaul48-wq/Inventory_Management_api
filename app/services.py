from app.repositories.product_repo import create_initial_product
from app.repositories.stock_movement_repo import add_stock_movement
from app.schemas.stock_movement import MovementType


def new_product(connection, name, description, price, quantity):
    with connection.transaction():
        product = create_initial_product(
            connection,
            name,
            description,
            price,
            quantity
        )
        
        add_stock_movement(
            connection,
            product["id"],
            MovementType.OPENING_BALANCE,
            product["quantity"],
            product["quantity"],
            "Initial product entry"
        )
        
        return product