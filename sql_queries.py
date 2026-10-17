from psycopg.rows import dict_row

def add_new_stock(conn, name, description, price, quantity):
    with conn.cursor() as cur:
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
            SELECT * FROM stocks;
""")
        stocks = cur.fetchall()
        return stocks

def get_one_stock(conn, id):
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT * FROM stocks
            WHERE id = %s;
""", (id,))
        stock = cur.fetchone()
        return stock

def delete_stock_by_id(conn, id):
    with conn.cursor() as cur:
        cur.execute("""
            DELETE FROM stocks
            WHERE id = %s;
""", (id,))

def update_stock(conn, values, set_clause):
    query = f"""
            UPDATE stocks
            SET {set_clause}, updated_at = NOW()
            WHERE id = %s
            RETURNING * ;
"""
    with conn.cursor() as cur:
        cur.execute(query, values)
        result = cur.fetchone()
        return result