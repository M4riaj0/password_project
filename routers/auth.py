from fastapi import APIRouter
from schemas.users import User
from fastapi.responses import JSONResponse
from typing import List

from utils.jwt_manager import create_token
from config.database import Session
from models.user import User as UserModel

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.post("/register", tags=['auth'],response_model=List[User], status_code=201)
def register_user(user: User):
    db = Session()
    new_user = UserModel(** user.model_dump())
    db.add(new_user)
    db.commit()
    return JSONResponse(content={"message": "User registered"}, status_code=201)

@auth_router.post("/login", tags=['auth'], response_model=dict, status_code=200)
def login(user: User):
    if ((user.email == "admin@mail.com") and (user.password == "admin")):
        token = create_token(data=user.model_dump())
        result = JSONResponse(content={"token": token}, status_code=200)

    else:
        result = JSONResponse(content={"message": "Inavlid credentials"}, status_code=401)
    
    return result