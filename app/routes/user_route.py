#pylint: disable = no-value-for-parameter
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.helpers.jwt import JWTBearer
from app.models.user_model import UserSchema
from app.controllers.user_controller import UserController
from app.config.database import get_db
from app.helpers.helper import Helper
router = APIRouter()


@router.get('/user', dependencies=[Depends(JWTBearer())])
def get(db: Session = Depends(get_db)):
    try:
        result = UserController.get_all(db)
        return Helper.generate_response("get", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.get('/user/{ids}', dependencies=[Depends(JWTBearer())])
def get_by_id(ids: int = 0, db: Session = Depends(get_db)):
    try:
        result = UserController.get_by_id(ids, db)
        return Helper.generate_response("get", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.post("/user", dependencies=[Depends(JWTBearer())])
def post(data: UserSchema, db: Session = Depends(get_db)):
    try:
        hashed_pass = Helper.hashed_password(data.password)
        data.password = hashed_pass
        result = UserController.create(data, db)
        return Helper.generate_response("create", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.put("/user/{ids}", dependencies=[Depends(JWTBearer())])
def put(data: UserSchema, ids: int, db: Session = Depends(get_db)):
    try:
        result = UserController.update(data, ids, db)
        return Helper.generate_response("update", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete("/user/{ids}", dependencies=[Depends(JWTBearer())])
def delete(ids: int, db: Session = Depends(get_db)):
    try:
        result = UserController.delete(ids, db)
        return Helper.generate_response("delete", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
