from app.database import pool
import app.services

subject = {
    "name": "Wireless Mouse",
    "price": 12500,
    "quantity": 20
}

subject1 = {}

subject2 = {
    "name": "  Syringe   ",
    "price": 21.2345,
    "quantity": -21
}

def test_create_initial_product_returns_201_and_id(client):
    response = client.post("/products", json=subject)
    assert response.status_code == 201
    body = response.json()
    assert body["id"] == 1001
    assert body["name"] == "Wireless Mouse"
    assert body["price"] == "12500.00"
    assert body["quantity"] == 20

def test_empty_description_returns_None(client):
    response = client.post("/products", json=subject)
    assert response.status_code == 201
    assert response.json()["description"] is None

def test_missing_required_fields(client):
    response = client.post("/products", json=subject1)
    assert response.status_code == 422
    body = response.json()
    assert body.get("name") is None
    assert body.get("price") is None
    assert body.get("quantity") is None

def test_invalid_inputs(client):
    response = client.post("/products", json=subject2)
    assert response.status_code == 422
    body = response.json()
    assert body.get("name") is None
    assert body.get("price") is None
    assert body.get("description") is None

def test_opening_balance_was_added(client):
    response = client.post("/products", json=subject)
    assert response.status_code == 201
    with pool.connection() as conn:
        row = conn.execute(
            "SELECT movement_type FROM stock_movements;"
        ).fetchone()
        result = row[0] # type: ignore
        assert result == "opening balance"


def failing_movement(*args, **kwargs):
    raise RuntimeError("Simulated database failure")

def test_transaction_rolls_back(client, monkeypatch):
    monkeypatch.setattr(
        app.services,
        "add_stock_movement",
        failing_movement
    )
    response = client.post("/products", json=subject)
    assert response.status_code == 500
    with pool.connection() as conn:
        row1 = conn.execute(
            "SELECT * FROM products;"
        ).fetchone()
        assert row1 is None
        row2 = conn.execute(
            "SELECT * FROM stock_movements;"
        ).fetchone()
        assert row2 is None