from fastapi import Depends
from typing import Annotated
from fastapi.exceptions import HTTPException
from fastapi.security import OAuth2PasswordBearer

from config.database import Session
from utils.jwt_manager import validate_token
from models.user import User as UserModel

oauth2_bearer = OAuth2PasswordBearer(tokenUrl='/auth/login')

def authenticate_user(username: str, password: str, verify_password: bool):
    db = Session()
    user = db.query(UserModel).filter(UserModel.username == username).first()
    if not user:
        return False
    if (password != user.password) and verify_password:
        return False
    return {"id_user": user.id_user ,"username": user.username, "password": user.password}

def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    try:
        payload = validate_token(token)
        print("decoded_token: ", payload)
        current_username: str =  payload.get('username')
        current_id_user: int = payload.get('id_user')
        if current_username is None or current_id_user is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        return {"current_username": current_username, "current_id_user": current_id_user}
    except:
        raise HTTPException(status_code=401, detail="Invalid authentication credentials")