from psycopg.rows import dict_row

def create_initial_product (connection, name, description, price, quantity):
    with connection.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            INSERT INTO products (name, description, price, quantiry)
            VALUES (%s, %s, %s, %s)
            RETURNING *;
""", (name, description, price, quantity))
        return cur.fetchone()