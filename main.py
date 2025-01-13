from fastapi import FastAPI
from fastapi import status
from fastapi import HTTPException
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError

from app.routes import content_route

app = FastAPI()

app.include_router(content_route.router)


@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI"}

@app.exception_handler(HTTPException)
async def custom_http_exception_handler(exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content = {
            "message": exc.detail,
            "status_code": exc.status_code,
            "success": False,
            "data": None,
        }
    ) 
    
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(exc: RequestValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, 
        content = {
            "message": {"detail": exc.errors(), "body": exc.body},
            "status_code": 400,
            "success": False,
            "data": None,
        }
    ) 
