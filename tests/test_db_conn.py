from app.database import pool

## database connection has open set to false. 
## For the test, we manually open and close it.

def test_conn():
    pool.open(wait=True)
    try:
        with pool.connection() as conn:
            with conn.cursor() as cur:
                result = cur.execute(
                    "SELECT 1"
                ).fetchone()

        assert result == (1,)

    finally:
        pool.close()