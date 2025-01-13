#pylint: disable = no-value-for-parameter
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session 
from app.controllers.auth_controller import AuthController
from app.config.database import get_db
from app.helpers.helper import Helper
router = APIRouter()

 
@router.post("/token")
def post(auth_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    try:
        result = AuthController.login(auth_data, db)
        return Helper.generate_response("login", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
 