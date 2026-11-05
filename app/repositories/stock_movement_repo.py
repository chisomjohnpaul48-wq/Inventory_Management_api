def add_stock_movement(connection, product_id, movement_type, quantity_change, new_quantity, reason):
    with connection.cursor() as cur:
        cur.execute("""
            INSERT INTO stock_movements (product_id, movement_type, quantity_change, new_quantity, reason)
            VALUES (%s, %s, %s, %s, %s);
""", (product_id, movement_type, quantity_change, new_quantity, reason))