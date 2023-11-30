# from datetime import timedelta, datetime
# from typing import Annotated
# from fastapi import APIRouter, Depends, HTTPException
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from starlette import status
# from database import sessionlocal
# from models import Truck
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
# from jose import jwt, JWTError


# router = APIRouter(prefix="/auth", tags=["auth"])

# SECRET_KEY = "12345850TESTING"
# ALGORITHM = "HS256"

# bcrypt_context = CryptContext(schemes=["bcrypt"], deprecate="auto")
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


# class CreateTruckREquest(BaseModel):
#     truck_number: int
#     transporter_name: str


# class Token(BaseModel):
#     access_token: str
#     token_type: str


# def get_db():
#     db = sessionlocal()
#     try:
#         yield db
#     finally:
#         db.close()


# db_dependency = Annotated[Session, Depends(get_db)]


# @router.post("/", status_code=status.HTTP_201_CREATED)
# async def create_truck(db: db_dependency, create_truck_request: CreateTruckREquest):
#     create_truck_model = Truck(
#         trucknumber=create_truck_request.truck_number,
#         hashed_password=bcrypt_context.hash(create_truck_request.transporter_name),
#     )
#     db.add(create_truck_model)
#     db.commit()
