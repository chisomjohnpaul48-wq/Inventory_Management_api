from fastapi import FastAPI
from routers import router
from setup import init_setup

app = FastAPI()
app.include_router(router)

init_setup() #initialize on application startup.