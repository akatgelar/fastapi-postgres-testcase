#pylint: disable = no-value-for-parameter
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.models.content_model import ContentSchema
from app.controllers.content_controller import ContentController
from app.config.database import get_db
from app.helpers.helper import Helper
router = APIRouter()


@router.get('/content')
def get(db: Session = Depends(get_db)):
    try:
        result = ContentController.get_all(db)
        return Helper.generate_response("get", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.get('/content/{ids}')
def get_by_id(ids: int = 0, db: Session = Depends(get_db)):
    try:
        result = ContentController.get_by_id(ids, db)
        return Helper.generate_response("get", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.post("/content")
def post(data: ContentSchema, db: Session = Depends(get_db)):
    try:
        result = ContentController.create(data, db)
        return Helper.generate_response("create", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.put("/content/{ids}")
def put(data: ContentSchema, ids: int, db: Session = Depends(get_db)):
    try:
        result = ContentController.update(data, ids, db)
        return Helper.generate_response("update", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e

@router.delete("/content/{ids}")
def delete(ids: int, db: Session = Depends(get_db)):
    try:
        result = ContentController.delete(ids, db)
        return Helper.generate_response("delete", result, status.HTTP_200_OK, bool(result), None)
    except HTTPException as e:
        raise HTTPException(status_code=500, detail=str(e)) from e
