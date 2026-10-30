from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.config import settings
from app.database import pool

@asynccontextmanager
async def lifespan(app: FastAPI):
    # ---- ON STARTUP ----
    print(f"Starting {settings.APP_NAME} app ...")
    try:
        pool.open(wait=True)
        print("DB connection pool opened")

        yield ## app runs here

    finally:
        # ---- ON SHUTDOWN ----
        print("Commencing shut down ...")
        pool.close()
        print("DB connection pool closed")


app = FastAPI(
    title=settings.APP_NAME,
    debug=settings.DEBUG,
    lifespan=lifespan
)