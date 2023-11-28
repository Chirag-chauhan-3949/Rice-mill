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


class AddRiceMillBase(BaseModel):
    rice_mill_name: str
    gst_number: str
    mill_address: str
    phone_number: int
    rice_mill_capacity: float
    rice_mill_id: Optional[int] = None


class TransporterBase(BaseModel):
    transporter_name: str
    transporter_phone_number: int
    transporter_id: Optional[int] = None


class TruckBase(BaseModel):
    truck_number: str
    transport_id: int
    truck_id: Optional[int] = None


class SocietyBase(BaseModel):
    society_name: str
    distance_from_mill: int
    transporting_rate: int
    society_id: Optional[int] = None


class AgreementBase(BaseModel):
    rice_mill_id: int
    agreement_number: str
    mota: int
    patla: int
    sarna: int
    lot_from: int
    lot_to: int
    total: int
    agremennt_id: Optional[int] = None


class AdddoBase(BaseModel):
    select_mill_id: int
    date: str
    do_number: int
    select_argeement_id: int
    moto_weight: str
    mota_Bardana: int
    patla_weight: str
    patla_bardana: int
    sarna_weight: str
    sarna_bardana: int
    total_weight: int
    total_bardana: int
    society_id: int
    truck_number_id: int
    do_id: Optional[int] = None


class DhanAwakBase(BaseModel):
    rst_number: int
    rice_mill_id: int
    date: int
    do_id: int
    society_id: int
    society_hidden_name: int
    dm_weight: str
    number_of_bags: int
    truck_id: int
    transporter_id: int
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


class DoPandingBase(BaseModel):
    date = int
    mota = str
    patla = str
    Total : int
    do_panding_id : Optional[int] = None

class SaudaPatrakBase(BaseModel):
    name : str
    address : str
    vechicle_number: str
    paddy : str
    bags : int
    weight : str
    Rate   : int
    amount : int    
    sauda_patrak_id : Optional[int] = None

class PaddySaleBase(BaseModel):
    rst_number : int
    party : str
    broker : str
    loading_form = Column("Excel")
    vehicle_number : str
    paddy_name : str
    weight : str
    party_weight : str
    rate : int
    ammount : int
    plastic : int
    joot_old : int
    joot_23_24 : int
    joot_22_23 : int    
    average_bag_wt : float
    paddy_sale_id : Optional[int] = None

class FrkBase(BaseModel):
    date : int
    party : str
    bags : int
    weight : str
    truck_number : str
    mill_name : str
    bill_number : int
    rate : float
    frk_id : Optional[int]= None

class DhanRiceSocietiesRateBase(BaseModel):
    distance = float
    new : int
    dhan_rice_societies_rate_id : Optional[int]=None

class LotNumberMasterBase(BaseModel):
    mill_name = str
    lot_number = int
    lot_number_master_id : Optional[int]= None

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Do Panding
@app.post("/do-panding/",status_code=status.HTTP_201_CREATED)
async def do_panding(dopanding: DoPandingBase, db: db_dependency):
    db_do_panding = models.Do_panding(**dopanding.dict())
    db.add(db_do_panding)
    db.commit()

@app.get("/do-panding-data/",response_model=List[DoPandingBase],status_code=status.HTTP_200_OK)
async def do_panding_data(db: db_dependency):
    db_do_panding_data = db.query(models.Do_panding).distinct().all()
    return db_do_panding_data


#Sauda patrak
@app.post("/sauda-patrak/",status_code=status.HTTP_201_CREATED)
async def sauda_patrak(saudapatrak: SaudaPatrakBase, db: db_dependency):
    db_sauda_patrak = models.Do_panding(**saudapatrak.dict())
    db.add(db_sauda_patrak)
    db.commit()

@app.get("/sauda-patrak-data/",response_model=List[SaudaPatrakBase],status_code=status.HTTP_200_OK)
async def sauda_patrak_data(db: db_dependency):
    db_sauda_patrak_data = db.query(models.Sauda_patrak).distinct().all()
    return db_sauda_patrak_data

#paddy sale
@app.post("/paddy-sale/",status_code=status.HTTP_201_CREATED)
async def paddy_sale(paddysale: PaddySaleBase, db: db_dependency):
    db_paddy_sale = models.Do_panding(**paddysale.dict())
    db.add(db_paddy_sale)
    db.commit()

@app.get("/paddy-sale-data/",response_model=List[PaddySaleBase],status_code=status.HTTP_200_OK)
async def paddy_sale_data(db: db_dependency):
    db_paddy_sale_data = db.query(models.Paddy_sale).distinct().all()
    return db_paddy_sale_data

# FRk
@app.post("/frk/",status_code=status.HTTP_201_CREATED)
async def frk(frk: FrkBase, db: db_dependency):
    db_frk = models.Do_panding(**frk.dict())
    db.add(db_frk)
    db.commit()

@app.get("/frk-data/",response_model=List[FrkBase],status_code=status.HTTP_200_OK)
async def frk_data(db: db_dependency):
    db_frk_data = db.query(models.Frk).distinct().all()
    return db_frk_data


# Dhan rice societies rate
@app.post("/dhan-rice-societies-rate/",status_code=status.HTTP_201_CREATED)
async def dhan_rice_societies_rate(dhansocietiesrate: DhanRiceSocietiesRateBase, db: db_dependency):
    db_dhan_rice_societies_rate = models.Dhan_rice_societies_rate(**frk.dict())
    db.add(db_dhan_rice_societies_rate)
    db.commit()

@app.get("/dhan-rice-societies-rate-data/",response_model=List[DhanRiceSocietiesRateBase],status_code=status.HTTP_200_OK)
async def dhan_rice_societies_rate_data(db: db_dependency):
    db_dhan_rice_societies_rate = db.query(models.Dhan_rice_societies_rate).distinct().all()
    return db_dhan_rice_societies_rate


# lot number master
@app.post("/lot-number-master/",status_code=status.HTTP_201_CREATED)
async def lot_number_master(lotnumbermaster: LotNumberMasterBase, db: db_dependency):
    db_lot_number_master = models.Lot_number_master(**lotnumbermaster.dict())
    db.add(db_lot_number_master)
    db.commit()

@app.get("/lot-number-master-data/",response_model=List[LotNumberMasterBase],status_code=status.HTTP_200_OK)
async def lot_number_master_data(db: db_dependency):
    db_lot_number_master = db.query(models.Lot_number_master).distinct().all()
    return db_lot_number_master



# About Rice Mill
@app.post("/add-rice-mill/", status_code=status.HTTP_201_CREATED)
async def add_rice_mill(addricemill: AddRiceMillBase, db: db_dependency):
    db_about_rice_mill = models.Add_Rice_Mill(**addricemill.dict())
    db.add(db_about_rice_mill)
    db.commit()


@app.get(
    "/rice-mill/",
    response_model=List[AddRiceMillBase],
    status_code=status.HTTP_200_OK,
)
async def rice_mill_data(db: db_dependency):
    db_rice_mill_data = db.query(models.Add_Rice_Mill).distinct().all()
    return db_rice_mill_data


# Add New Transporters
@app.post("/transporter/", status_code=status.HTTP_201_CREATED)
async def add_new_trasporter(transporters: TransporterBase, db: db_dependency):
    db_transporter = models.Transporter(**transporters.dict())
    db.add(db_transporter)
    db.commit()


@app.get(
    "/transporters/",
    response_model=List[TransporterBase],
    status_code=status.HTTP_200_OK,
)
async def get_all_transporters(db: db_dependency):
    transporters = db.query(models.Transporter).distinct().all()
    return transporters


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
@app.get("/truck-numbers/", response_model=List[str], status_code=status.HTTP_200_OK)
async def get_truck_numbers(db: db_dependency):
    db_truck_numbers = db.query(models.Truck.truck_number).distinct().all()
    return [truck_number[0] for truck_number in db_truck_numbers]


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


# # Dhan Awak
# @app.post("/dhan-awak/", status_code=status.HTTP_201_CREATED)
# async def add_dhan_awak(dhanawak: DhanAwakBase, db: db_dependency):
#     db_dhan_awak = models.Dhan_Awak(**dhanawak.dict())
#     db.add(db_dhan_awak)
#     db.commit()


# @app.get(
#     "/dhan-awak-data/",
#     response_model=List[DhanAwakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_dhan_awak(db: db_dependency):
#     db_dhan_awak_data = db.query(models.Dhan_Awak).distinct().all()
#     return db_dhan_awak_data


# # Add Do
# @app.post("/add-do/", status_code=status.HTTP_201_CREATED)
# async def add_do(adddo: AdddoBase, db: db_dependency):
#     db_add_do = models.Add_Do(**adddo.dict())
#     db.add(db_add_do)
#     db.commit()


# @app.get(
#     "/add-do-data/", response_model=List[AdddoBase], status_code=status.HTTP_200_OK
# )
# async def get_all_add_do_data(db: db_dependency):
#     add_do = db.query(models.Add_Do).distinct().all()
#     return add_do
