from fastapi import FastAPI
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi.responses import HTMLResponse
from config.database import engine, Base

from routers.auth import auth_router

app = FastAPI()
app.title = "Password Generator"
app.version = "0.0.1"

app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

@app.get("/", tags=["Home"])
def message():
    return HTMLResponse(content="<h1>contraseñas</h1>", status_code=200)