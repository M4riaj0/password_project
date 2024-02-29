from typing import List, Annotated
from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from config.database import Session
from schemas.password import Password
from middlewares.auth import get_current_user
from middlewares.password import password_generator
from models.password import Password as PasswordModel

user_dependency = Annotated[dict, Depends(get_current_user)]
from schemas.password import Password
password_router = APIRouter(prefix="/password", tags=['password'])


@password_router.get("/get-password", tags=['password'], response_model=List[Password], status_code=200)
def getPasswords(current_user: user_dependency) -> List[Password]:
    db = Session()
    result = db.query(PasswordModel).filter(PasswordModel.id_user == current_user["current_id_user"]).all()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

@password_router.post("/create-password", tags=['password'], response_model=List[Password], status_code=201)
def createPassword(password: Password, current_user: user_dependency):
    db = Session()
    password = password_generator(password)
    if not password:
        return JSONResponse(content={"message": "Could not generate the password"}, status_code=404)
    new_password = {"password": password, "id_user": current_user["current_id_user"]}
    new_password = PasswordModel(**   new_password)
    db.add(new_password)
    db.commit()
    return JSONResponse(content={"message": f"password created, password: {password}"}, status_code=201)

@password_router.put("/edit", tags=['password'])
def updatePassword(id_password: int, password: Password, current_user: user_dependency)-> dict:
    print("Entraaaa:::", id_password, password, current_user)
    db = Session()
    result = db.query(PasswordModel).filter((PasswordModel.id_password == id_password) & (PasswordModel.id_user == current_user["current_id_user"])).first()
    print("result:::", result)
    if not result:
        return JSONResponse(content={"message": "Password not found"}, status_code=404)
    password = password_generator(password)
    if not password:
        return JSONResponse(content={"message": "Could not generate the password"}, status_code=404)
    result.password = password
    db.add(result)
    db.commit()
    return JSONResponse(content={"message": f"Password updated, new_password: {password}"}, status_code=200)

@password_router.delete("/delete", tags=['password'], response_model=dict)
def deletePassword(id_password: int, current_user: user_dependency) -> dict:
    db = Session()
    password = db.query(PasswordModel).filter((PasswordModel.id_password == id_password) & (PasswordModel.id_user == current_user["current_id_user"])).first()
    if not password: 
        return JSONResponse(content={"message": "Password not found" }, status_code=404)
    db.delete(password)
    db.commit()
    return JSONResponse(content={"message": "Password deleted"}, status_code=200)