from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, List, Optional
import models
from database import engine, sessionlocal
from sqlalchemy.orm import Session


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# CORS (Cross-Origin Resource Sharing) middleware configuration
origins = [
    "http://localhost:5173",
    "http://localhost:5174",  # Update this with the origin of your React app
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class AboutRiceMillBase(BaseModel):
    rice_mill_name: str
    gst_number: int
    mill_address: str
    phone_number: int
    rice_mill_capacity: float
    about_rice_mill_id: Optional[int] = None


class TransporterBase(BaseModel):
    transporter_name: str
    transporter_phone_number: int
    transporter_id: Optional[
        int
    ] = None  # This id will help me in add truck for relative data base


class TruckBase(BaseModel):
    truck_number: int
    transporter_name: str
    truck_transport_id: int
    truck_id: Optional[int] = None


class SocietyBase(BaseModel):
    society_name: str
    distance_from_mill: int
    transporting_rate: int
    society_id: Optional[int] = None


class AgreementBase(BaseModel):
    mill: str
    # Create Add rice mill form
    agreement_number: int
    mota: int
    patla: int
    sarna: int
    lot_from: int
    lot_to: int
    total: int
    agremennt_id: Optional[int] = None


class AdddoBase(BaseModel):
    select_mill: str
    date: str
    do_number: int
    select_agreement: str
    select_argeement_id: int
    moto_weight: str
    mota_Bardana: int
    patla_weight: str
    patla_bardana: int
    sarna_weight: str
    sarna_bardana: int
    total_weight: int
    total_bardana: int
    society: str
    society_id: int
    truck_number: int
    truck_number_id: int
    do_id: Optional[int] = None


class DhanAwakBase(BaseModel):
    rst_number: int
    select_mill: str
    rice_mill_id: int
    date: int
    do_number: int
    do_id: int
    society: str
    society_id: int
    society_hidden_name: int
    dm_weight: str
    number_of_bags: int
    truck_number: int
    truck_id: int
    transporter: str
    transporter_id: int
    transporting_rate: int
    transporting_rate_society_id: int
    transporting_total: int
    jama_jute_22_23: int
    ek_bharti_21_22: int
    pds: int
    miller_purana: int
    kisan: int
    bardana_society: int
    hdpe_22_23: int
    hdpe_21_22: int
    hdpe_21_22_one_use: int
    total_bag_weight: str
    type_of_paddy: str
    actual_paddy: str
    mill_weight_quintals: str
    shortage: int
    bags_put_in_hopper: int
    total_hopper_weight: str


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# About Rice Mill
@app.post("/about-rice-mill/", status_code=status.HTTP_201_CREATED)
async def add_rice_mill(aboutricemill: AboutRiceMillBase, db: db_dependency):
    db_about_rice_mill = models.About_Rice_Mill(**aboutricemill.dict())
    db.add(db_about_rice_mill)
    db.commit()


@app.get(
    "/rice-mill/",
    response_model=List[AboutRiceMillBase],
    status_code=status.HTTP_200_OK,
)
async def rice_mill_data(db: db_dependency):
    db_rice_mill_data = db.query(models.About_Rice_Mill).distinct().all()
    return db_rice_mill_data


# Dhan Awak
@app.post("/dhan-awak/", status_code=status.HTTP_201_CREATED)
async def add_dhan_awak(dhanawak: DhanAwakBase, db: db_dependency):
    db_dhan_awak = models.Dhan_Awak(**dhanawak.dict())
    db.add(db_dhan_awak)
    db.commit()


@app.get(
    "/dhan-awak-data/",
    response_model=List[DhanAwakBase],
    status_code=status.HTTP_200_OK,
)
async def get_dhan_awak(db: db_dependency):
    db_dhan_awak_data = db.query(models.Dhan_Awak).distinct().all()
    return db_dhan_awak_data


# Add New Agreement
@app.post("/agreement/", status_code=status.HTTP_201_CREATED)
async def add_agreement(agreement: AgreementBase, db: db_dependency):
    db_agreement = models.Agreement(**agreement.dict())
    db.add(db_agreement)
    db.commit()


@app.get(
    "/agreements/", response_model=List[AgreementBase], status_code=status.HTTP_200_OK
)
async def get_all_agreement_data(db: db_dependency):
    agreements = db.query(models.Agreement).distinct().all()
    return agreements


# Get all agreements number for dropdown options
@app.get(
    "/agreements-number/", response_model=List[int], status_code=status.HTTP_200_OK
)
async def get_all_agreements_number(db: db_dependency):
    db_agreements_number = db.query(models.Agreement.agreement_number).distinct().all()
    return [agreement_number[0] for agreement_number in db_agreements_number]


# Add New Society
@app.post("/society/", status_code=status.HTTP_201_CREATED)
async def add_new_society(society: SocietyBase, db: db_dependency):
    db_society = models.Society(**society.dict())
    db.add(db_society)
    db.commit()


@app.get(
    "/societies/", response_model=List[SocietyBase], status_code=status.HTTP_200_OK
)
async def get_all_society_data(db: db_dependency):
    societys = db.query(models.Society).distinct().all()
    return societys


# Get all society name for dropdown options
@app.get("/societies-names/", response_model=List[str], status_code=status.HTTP_200_OK)
async def get_all_societyes_names(db: db_dependency):
    db_get_all_societyes_names = db.query(models.Society.society_name).distinct().all()
    return [all_society_name[0] for all_society_name in db_get_all_societyes_names]


# Add New Truck
@app.post("/truck/", status_code=status.HTTP_201_CREATED)
async def add_new_truck(truck: TruckBase, db: db_dependency):
    db_truck = models.Truck(**truck.dict())
    db.add(db_truck)
    db.commit()


@app.get("/trucks/", response_model=List[TruckBase], status_code=status.HTTP_200_OK)
async def get_all_truck_data(db: db_dependency):
    trucks = db.query(models.Truck).distinct().all()
    return trucks


# Get all truck numbers for dropdown options
@app.get("/truck-numbers/", response_model=List[int], status_code=status.HTTP_200_OK)
async def get_truck_numbers(db: db_dependency):
    db_truck_numbers = db.query(models.Truck.truck_number).distinct().all()
    return [truck_number[0] for truck_number in db_truck_numbers]


# Add New Transporters
@app.post("/transporter/", status_code=status.HTTP_201_CREATED)
async def add_new_trasporter(transporters: TransporterBase, db: db_dependency):
    db_transporter = models.Transporter(**transporters.dict())
    db.add(db_transporter)
    db.commit()


@app.get(
    "/transporters-name/", response_model=List[str], status_code=status.HTTP_200_OK
)
async def get_all_transporters(db: db_dependency):
    transporters_names = db.query(models.Transporter.transporter_name).distinct().all()
    return [transporter[0] for transporter in transporters_names]


@app.get(
    "/transporters/",
    response_model=List[TransporterBase],
    status_code=status.HTTP_200_OK,
)
async def get_all_transporters(db: db_dependency):
    transporters = db.query(models.Transporter).distinct().all()
    return transporters


# Add Do
@app.post("/add-do/", status_code=status.HTTP_201_CREATED)
async def add_do(adddo: AdddoBase, db: db_dependency):
    db_add_do = models.Add_Do(**adddo.dict())
    db.add(db_add_do)
    db.commit()


@app.get(
    "/add-do-data/", response_model=List[AdddoBase], status_code=status.HTTP_200_OK
)
async def get_all_add_do_data(db: db_dependency):
    add_do = db.query(models.Add_Do).distinct().all()
    return add_do
