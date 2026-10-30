from psycopg_pool import ConnectionPool
from app.config import settings

db_url = settings.DATABASE_URL
if not db_url:
    raise RuntimeError("DATABASE_URL is likely not set.")


pool = ConnectionPool(
    conninfo=db_url,
    min_size=1,
    max_size=5,
    open=False # don't connect on import, connect on app startup
    )

def get_connection():
    return pool.connection()

def get_pool():
    return pool