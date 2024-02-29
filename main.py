from fastapi import FastAPI, Depends
from fastapi.exceptions import HTTPException
from fastapi.responses import HTMLResponse, JSONResponse
from config.database import engine, Base
from typing import Annotated

from routers.auth import auth_router
from routers.passwords import password_router
from middlewares.auth import get_current_user
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from config.database import Base, engine
from routers.auth import auth_router
import logging




app = FastAPI()


app.title = "Password Generator"
app.version = "0.0.1"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(password_router)
app.include_router(auth_router)
Base.metadata.create_all(bind=engine)

user_dependency = Annotated[dict, Depends(get_current_user)]
logger = logging.getLogger(__name__)

@app.get("/", tags=["Home"])
def user(user: user_dependency):
    if user is None:
        # logger.warning("User is not authenticated.")
        return JSONResponse(content={"message": "Not authenticated"}, status_code=401)
    
    # logger.info("User authenticated successfully.")
    # logger.debug(f"Decoded user information: {user}")
    
    return JSONResponse(content={"username": user['current_username'], "id": user['current_id_user']}, status_code=200)
