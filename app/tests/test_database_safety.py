from psycopg.conninfo import conninfo_to_dict
import pytest
from app.exceptions.database import UnsafeTestDatabaseError
from app.testing.database_safety import get_database_name


def test_get_database_name_rejects_wrong_database():
    with pytest.raises(UnsafeTestDatabaseError) as exc_info:
        get_database_name(
            "postgresql://postgres:PASSWORD@localhost:5432/inventory_db"
        )

    assert str(exc_info.value) == "Database name must be 'inventory_test'"

def test_get_database_name_accepts_test_database():
    result = get_database_name(
        "postgresql://postgres:PASSWORD@localhost:5432/inventory_test"
        )

    assert result == "inventory_test"