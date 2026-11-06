from app.config import settings
from app.testing.database_safety import get_database_name, validate_connected_database

test_database_url = settings.TEST_DATABASE_URL

get_database_name(test_database_url)

settings.DATABASE_URL = settings.TEST_DATABASE_URL

from app.main import app
from fastapi.testclient import TestClient
import pytest
from app.database import pool

@pytest.fixture(scope="session")
def client():
    with TestClient(app, raise_server_exceptions=False) as client:
        yield client

@pytest.fixture(autouse=True, scope="function")
def clean_tables(client):
    with pool.connection() as connection:
        validate_connected_database(connection)
        with connection.transaction():
            connection.execute(
                "TRUNCATE stock_movements, products RESTART IDENTITY;"
            )