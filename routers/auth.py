from typing import List, Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.security import OAuth2PasswordRequestForm

from schemas.users import User
from schemas.token import Token
from config.database import Session
from models.user import User as UserModel
from utils.jwt_manager import create_token
from middlewares.auth import authenticate_user
from middlewares.password import password_generator

auth_router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)

@auth_router.post("/register", tags=['auth'],response_model=List[User], status_code=201)
def register_user(user: User):
    print('user: ', user)
    password = password_generator(user)
    new_user = authenticate_user(user.username, None, False)
    if new_user:
        return JSONResponse(content={"message": "User already exists"}, status_code=400)
    db = Session()
    new_user = {"username": user.username, "password": password }
    new_user = UserModel(** new_user)
    db.add(new_user)
    db.commit()
    message = f"User registered, your password is: {password}"
    return JSONResponse(content={"message": message, "password": password}, status_code=201)

@auth_router.post("/login", tags=['auth'], response_model=Token, status_code=200)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    user_auth = authenticate_user(form_data.username, form_data.password, True)
    if not user_auth:
        return JSONResponse(content={"message": "Incorrect username or password"}, status_code=401)
    token = create_token(data=user_auth)
    return JSONResponse(content={"access_token": token, "token_type": "bearer"}, status_code=200)

