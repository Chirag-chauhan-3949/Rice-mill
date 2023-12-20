# from datetime import timedelta  datetime
# from typing import Annotated
# from fastapi import APIRouter  Depends  HTTPException
# from pydantic import BaseModel
# from sqlalchemy.orm import Session
# from starlette import status
# from database import sessionlocal
# from models import Truck
# from passlib.context import CryptContext
# from fastapi.security import OAuth2PasswordRequestForm  OAuth2PasswordBearer
# from jose import jwt  JWTError


# router = APIRouter(prefix= /auth   tags=[ auth ])

# SECRET_KEY =  12345850TESTING
# ALGORITHM =  HS256

# bcrypt_context = CryptContext(schemes=[ bcrypt ]  deprecate= auto )
# oauth2_bearer = OAuth2PasswordBearer(tokenUrl= auth/token )


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


# db_dependency = Annotated[Session  Depends(get_db)]


# @router.post( /   status_code=status.HTTP_201_CREATED)
# async def create_truck(db: db_dependency  create_truck_request: CreateTruckREquest):
#     create_truck_model = Truck(
#         trucknumber=create_truck_request.truck_number
#         hashed_password=bcrypt_context.hash(create_truck_request.transporter_name)
#     )
#     db.add(create_truck_model)
#     db.commit()


def lot_number(x, y):
    for i in range(x, y):
        print(i)


lot_number(250, 300)


truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
transporter_name_id = Column(Integer, ForeignKey("transporter.transporter_id"))
transporting_rate = Column(Integer)
transporting_total = Column(Integer)
jama_jute_22_23 = Column(Integer)
ek_bharti_21_22 = Column(Integer)
pds = Column(Integer)
miller_purana = Column(Integer)
kisan = Column(Integer)
bardana_society = Column(Integer)
hdpe_22_23 = Column(Integer)
hdpe_21_22 = Column(Integer)
hdpe_21_22_one_use = Column(Integer)
total_bag_weight = Column(Float)
type_of_paddy = Column(String(50))
actual_paddy = Column(String(50))
mill_weight_quintals = Column(Integer)
shortage = Column(Float)
bags_put_in_hopper = Column(Integer)
bags_put_in_stack = Column(Integer)
hopper_rice_mill_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
stack_location = Column(String(50))
