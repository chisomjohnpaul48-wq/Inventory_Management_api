from app.database import pool

def test_conn():
    with pool.connection() as conn:
        with conn.cursor() as cur:
            result = cur.execute(
                "SELECT 1"
            ).fetchone()

    assert result == (1,)