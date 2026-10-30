from app.config import Settings

def test_config():
    settings = Settings(DATABASE_URL="postgresql://user:password@localhost:5432/test_db")
    assert settings.APP_NAME == "Inventory Management API"
    assert settings.DEBUG == False
    assert isinstance(settings.DATABASE_URL, str)