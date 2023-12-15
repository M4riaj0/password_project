from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from typing import Annotated

from routers.auth import auth_router
from middlewares.auth import get_current_user

app = FastAPI()
app.title = "Password Generator"
app.version = "0.0.1"

app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

user_dependency = Annotated[dict, Depends(get_current_user)]

@app.get("/", tags=["Home"])
def user(user: user_dependency):
    if user is None:
        raise HTTPException(status_code=401, detail="Not authenticated")
    return HTMLResponse(f"<h1>Welcome {user['current_username']} id: {user['current_id_user']}</h1>")