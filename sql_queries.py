from psycopg.rows import dict_row

## Stock Queries
def add_new_stock(conn, name, description, price, quantity):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            INSERT INTO stocks (name, description, price, quantity)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
""", (name, description, price, quantity))
        new_stock = cur.fetchone()
        return new_stock

def get_current_stocks(conn):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT * FROM stocks
            WHERE is_deleted = FALSE;
""")
        stocks = cur.fetchall()
        return stocks

def get_one_stock(conn, id):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT * FROM stocks
            WHERE id = %s and is_deleted = FALSE;
""", (id,))
        stock = cur.fetchone()
        return stock

def delete_stock_by_id(conn, id):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            UPDATE stocks
            SET is_deleted = TRUE,
            updated_at = NOW()
            WHERE id = %s
            RETURNING *;
""", (id,))
        result = cur.fetchone()
        return result



def update_stock(conn, values, set_clause):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute(
            f"""
            UPDATE stocks
            SET {set_clause}, updated_at = NOW()
            WHERE id = %s
            RETURNING *
            """,
            values
        )
        return cur.fetchone()

## Stock Movement Queries
def add_stock_movement(conn, stock_id, movement_type, quantity_change, new_quantity, reason):
    with conn.cursor() as cur:
        cur.execute("""
            INSERT INTO stock_movement (stock_id, movement_type, quantity_change, new_quantity, reason)
            VALUES (%s, %s, %s, %s, %s);
""", (stock_id, movement_type, quantity_change, new_quantity, reason))

def get_stock_movements(conn, stock_id):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT * FROM stock_movement
            WHERE stock_id = %s
            ORDER BY created_at DESC;
""", (stock_id,))
        movements = cur.fetchall()
        return movements

def get_all_stock_movements(conn):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT * FROM stock_movement
            ORDER BY created_at DESC;
""")
        movements = cur.fetchall()
        return movements