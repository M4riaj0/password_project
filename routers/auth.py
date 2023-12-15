from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from typing import List, Annotated
from fastapi.security import OAuth2PasswordRequestForm

from schemas.users import User
from schemas.token import Token
from utils.jwt_manager import create_token
from config.database import Session
from models.user import User as UserModel
from middlewares.auth import authenticate_user

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.post("/register", tags=['auth'],response_model=List[User], status_code=201)
def register_user(user: User):
    new_user = authenticate_user(user.username, user.password)
    if new_user:
        return JSONResponse(content={"message": "User already exists"}, status_code=400)
    db = Session()
    new_user = UserModel(** user.model_dump())
    db.add(new_user)
    db.commit()
    return JSONResponse(content={"message": "User registered"}, status_code=201)

@auth_router.post("/login", tags=['auth'], response_model=Token, status_code=200)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_auth = authenticate_user(form_data.username, form_data.password)
    if not user_auth:
        return JSONResponse(content={"message": "Incorrect username or password"}, status_code=401)
    token = create_token(data=user_auth)
    return JSONResponse(content={"access_token": token, "token_type": "bearer"}, status_code=200)

