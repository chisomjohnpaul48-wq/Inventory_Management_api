from psycopg.conninfo import conninfo_to_dict
from app.exceptions.database import UnsafeTestDatabaseError

def get_database_name(database_url):
    payload = conninfo_to_dict(database_url)
    dbname = payload.get('dbname')
    if dbname != "inventory_test":
        raise UnsafeTestDatabaseError("Database name must be 'inventory_test'")
    return dbname

def validate_connected_database(connection):
    row = connection.execute("SELECT current_database()").fetchone()
    if row is None:
        raise UnsafeTestDatabaseError("No database connected")
    if row[0] != "inventory_test":
        raise UnsafeTestDatabaseError("Database name must be 'inventory_test'")
    return row[0]