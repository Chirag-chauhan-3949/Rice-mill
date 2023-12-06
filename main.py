from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, List, Optional
import models
from database import engine, sessionlocal
from sqlalchemy.orm import Session,joinedload, relationship
from datetime import date


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
    # rice_mill_name_id: int
    transporter_phone_number: int
    transporter_name: str
    transporter_id: Optional[int] = None


class TruckBase(BaseModel):
    truck_number: str
    transport_id: int
    truck_id: Optional[int] = None


class SocietyBase(BaseModel):
    society_name: str
    distance_from_mill: int
    google_distance: int
    transporting_rate: int
    actual_distance: int
    society_id: Optional[int] = None


# class SocietyBase(BaseModel):
#     society_name: str
#     society_id: Optional[int] = None


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
    date: date
    do_number: str
    select_argeement_id: int
    moto_weight: float
    mota_Bardana: float
    patla_weight: float
    patla_bardana: float
    sarna_weight: float
    sarna_bardana: float
    total_weight: float
    total_bardana: float
    society_name_id: int
    truck_number_id: int
    do_id: Optional[int] = None


class DhanAwakBase(BaseModel):
    rst_number: int
    rice_mill_id: int
    date: date
    do_id: int
    society_id: int
    dm_weight: int
    number_of_bags: int
    truck_number_id: int
    transporter_name_id: int
    transporting_rate: int
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
    total_bag_weight: float
    type_of_paddy: str
    actual_paddy: str
    mill_weight_quintals: int
    shortage: float
    bags_put_in_hopper: int
    bags_put_in_stack: int
    hopper_rice_mill_id: int
    stack_location: str
    dhan_awak_id: Optional[int] = None


class DoPandingBase(BaseModel):
    do_number_id: int
    date: date
    mota: str
    patla: str
    sarna: str
    Total: int
    do_panding_id: Optional[int] = None


class SaudaPatrakBase(BaseModel):
    name: str
    address: str
    vechicle_number_id: int
    paddy: str
    bags: int
    weight: int
    rate: int
    amount: int
    sauda_patrak_id: Optional[int] = None


class PaddySaleBase(BaseModel):
    rst_number_id: int
    date: date
    party: str
    broker: str
    loading_form_address: str
    vehicle_number_id: int
    paddy_name: str
    weight: int
    party_weight: int
    rate: int
    ammount: int
    plastic: int
    joot_old: int
    joot_23_24: int
    joot_22_23: int
    average_bag_wt: float
    paddy_sale_id: Optional[int] = None


class FrkBase(BaseModel):
    date: date
    party: str
    bags: int
    weight: int
    truck_number_id: int
    rice_mill_name_id: int
    bill_number: int
    rate: float
    batch_number: int
    frk_id: Optional[int] = None


class DhanRiceSocietiesRateBase(BaseModel):
    society_name_id: int
    distance: float
    new: int
    dhan_rice_societies_rate_id: Optional[int] = None


class LotNumberMasterBase(BaseModel):
    rice_mill_name_id: int
    lot_number: int
    lot_number_master_id: Optional[int] = None

class KochiaBase(BaseModel):
    rice_mill_name_id: int
    kochia_name: str
    kochia_phone_number: int
    kochia_id: Optional[int] = None



class DalaliDhaanBase(BaseModel):
    rst_number: int
    date: date
    kochia_id: int
    vehicale_number_id: int
    white_sarna_bags: int
    white_sarna_weight: int
    ir_bags: int
    ir_weight: int
    rb_gold_bags: int
    rb_gold_weight: int
    sarna_bags: int
    sarna_weight: int
    sambha_new_bag: int
    sambha_new_weight: int
    paddy_type: str
    total_bags: int
    total_weight: int
    hamali: int
    weight_less_plastic: int
    weight_less_jute: int
    weight_less_kata_difference: int
    net_weight: int
    rate: int
    ammount: float
    dalali_dhaan_id: Optional[int] = None


class MohanFoodPaddyBase(BaseModel):
    date: date
    do_number_id: int
    samiti: str
    rice_mill_name_id: int
    weight: int
    vehicle_number_id: int
    bags: int
    transporting_total: int
    transporter_name_id: int
    transporter_type: str
    transporter_status: str
    rate: int
    type_1: str
    years_22_23: int
    years_21_22: int
    hdpe_one: int
    hdpe_new: int
    purana: int
    pds: int
    mohan_food_paddy_id: Optional[int] = None


class DhanTransportingBase(BaseModel):
    rst_number_id: int
    date: date
    do_number_id: int
    society_name_id: int
    rice_mill_name_id: int
    dm_weight: int
    truck_number_id: int
    numbers_of_bags: int
    transporting_total: int
    transporter_name_id: int
    status: str
    total_pending: int
    total_paid: int
    Dhan_transporting_id: Optional[int] = None


class TransporterMasterBase(BaseModel):
    vehicle_number_id: int
    name: str
    phone_number: int
    date: date
    transporter_name_id: int
    advance_payment: int
    transporter_master_id: Optional[int] = None




class RiceDepositeBase(BaseModel):
    rst_number: int
    date: date
    lot_number: int
    ware_house: str
    rice_mill_name_id: int
    weight: int
    truck_number_id: int
    bags: int
    transporting_total: int
    transporter_name_id: int
    transporting_type: str
    transporting_status: str
    rate: int
    variety: str
    halting: int
    rrga_wt: int
    data_2022_23: int
    data_2021_22: int
    pds: int
    old: int
    amount: int
    status: str
    rice_depostie_id: Optional[int] = None


class RiceMillData(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    agreement_data: List[AgreementBase]
    truck_data: List[TruckBase]
    society_data: List[SocietyBase]


class AddDoData(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    agreement_data: List[AgreementBase]


class DhanAwakRiceDoSocietyTruckTransporter(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    do_number_data: List[AdddoBase]
    society_data: List[SocietyBase]
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


class DhanAwakRiceDoNumber(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    do_number_data: List[AdddoBase]


class DhanAwakTruckTransporter(BaseModel):
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


class RiceRstSocietyDoTruckTransporter(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    rst_data: List[DhanAwakBase]
    society_data: List[SocietyBase]
    do_number_data: List[AdddoBase]
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


class RiceDepostiRiceTruckTransport(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


class RiceMillRstNumber(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    do_number_data: List[AdddoBase]
    rst_data: List[DhanAwakBase]

class SocietyDistanceRate(BaseModel):
    transporting_rate: int

class WareHouseTransporting(BaseModel):
    ware_houes_name: str
    ware_house_transporting_rate: int
    ware_houes_id: Optional[int] = None

class wareHousetrasportingrate(BaseModel):
    ware_house_transporting_rate: int

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Rice Deposti
@app.get(
    "/rice-truck-transporter/",
    response_model=RiceDepostiRiceTruckTransport,
    status_code=status.HTTP_200_OK,
)
async def rice_deposit_data(db: db_dependency):
    rice_mill_data = db.query(models.Add_Rice_Mill).all()
    truck_data = db.query(models.Truck).all()
    transporter_data = db.query(models.Transporter).all()

    rice_deposit_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "transporter_data": [
            TransporterBase(**row.__dict__) for row in transporter_data
        ],
    }
    return rice_deposit_data


# Dhan Transporting
@app.get(
    "/rice-rst-society-do-truck-transporter/",
    response_model=RiceRstSocietyDoTruckTransporter,
    status_code=status.HTTP_200_OK,
)
async def dhan_transporting_data(db: db_dependency):
    rice_mill_data = db.query(models.Add_Rice_Mill).all()
    rst_data = db.query(models.Dhan_Awak).all()
    do_number_data = db.query(models.Add_Do).all()
    society_data = db.query(models.Society).all()
    truck_data = db.query(models.Truck).all()
    transporter_data = db.query(models.Transporter).all()

    dhan_transporting_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "rst_data": [DhanAwakBase(**row.__dict__) for row in rst_data],
        "do_number_data": [AdddoBase(**row.__dict__) for row in do_number_data],
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "society_data": [SocietyBase(**row.__dict__) for row in society_data],
        "transporter_data": [
            TransporterBase(**row.__dict__) for row in transporter_data
        ],
    }
    return dhan_transporting_data

# Society
# @app.get(
#     "/society-data/{society_id}",
#     response_model=SocietyDistanceRate,
#     status_code=status.HTTP_200_OK,
# )
# async def society_data(society_id: int, db: db_dependency):
#     society_data = db.query(models.Society).filter_by(society_id=society_id).all()
#     society_db = {
#         "society_data": [SocietyBase(**row.__dict__) for row in society_data],
#     }
#     return society_db

@app.get(
    "/society-data/{society_id}",
    response_model=SocietyDistanceRate,
    status_code=status.HTTP_200_OK,
)
async def society_data(society_id: int, db: db_dependency):
    society_data = db.query(models.Society).filter_by(society_id=society_id).first()

    if society_data is None:
        raise HTTPException(status_code=404, detail="Society not found")

    response_data = {"transporting_rate": society_data.transporting_rate}
    return response_data



# Dhan Awak
@app.get(
    "/truck-transporter/{transport_id}",  # Here will go my truck ID
    response_model=DhanAwakTruckTransporter,
    status_code=status.HTTP_200_OK,
)
async def truck_transporter_data(transport_id: int, db: db_dependency):
    truck_data = db.query(models.Truck).filter_by(transport_id=transport_id).all()
    transporter_data = (
        db.query(models.Transporter).filter_by(transporter_id=transport_id).all()
    )
    dhan_awak_truck_transporter = {
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "transporter_data": [
            TransporterBase(**row.__dict__) for row in transporter_data
        ],
    }
    return dhan_awak_truck_transporter


@app.get(
    "/rice-rst-number-do-number/{rice_mill_id}",
    response_model=RiceMillRstNumber,
    status_code=status.HTTP_200_OK,
)
async def rice_mill_rst_number(rice_mill_id: int, db: db_dependency):
    rice_mill_data = (
        db.query(models.Add_Rice_Mill).filter_by(rice_mill_id=rice_mill_id).all()
    )
    rst_data = db.query(models.Dhan_Awak).filter_by(rice_mill_id=rice_mill_id).all()
    do_number_data = (
        db.query(models.Add_Do).filter_by(select_mill_id=rice_mill_id).all()
    )
    rice_mill_rst_number = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "do_number_data": [AdddoBase(**row.__dict__) for row in do_number_data],
        "rst_data": [DhanAwakBase(**row.__dict__) for row in rst_data],
    }
    return rice_mill_rst_number


@app.get(
    "/rice-do-number/{rice_mill_id}",
    response_model=DhanAwakRiceDoNumber,
    status_code=status.HTTP_200_OK,
)
async def rice_do_number_data(rice_mill_id: int, db: db_dependency):
    rice_mill_data = (
        db.query(models.Add_Rice_Mill).filter_by(rice_mill_id=rice_mill_id).all()
    )
    do_number_data = (
        db.query(models.Add_Do).filter_by(select_mill_id=rice_mill_id).all()
    )
    dhan_awak = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "do_number_data": [AdddoBase(**row.__dict__) for row in do_number_data],
    }
    return dhan_awak


@app.get(
    "/rice-do-society-truck-transporter/",
    response_model=DhanAwakRiceDoSocietyTruckTransporter,
    status_code=status.HTTP_200_OK,
)
async def Dhan_awak_data(db: db_dependency):
    rice_mill_data = db.query(models.Add_Rice_Mill).all()
    do_number_data = db.query(models.Add_Do).all()
    society_data = db.query(models.Society).all()
    truck_data = db.query(models.Truck).all()
    transporter_data = db.query(models.Transporter).all()

    dhan_awak_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "do_number_data": [AdddoBase(**row.__dict__) for row in do_number_data],
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "society_data": [SocietyBase(**row.__dict__) for row in society_data],
        "transporter_data": [
            TransporterBase(**row.__dict__) for row in transporter_data
        ],
    }
    return dhan_awak_data


# ADD DO
@app.get(
    "/rice-agreement-data/{rice_mill_id}",
    response_model=AddDoData,
    status_code=status.HTTP_200_OK,
)
async def adddodata(rice_mill_id: int, db: db_dependency):
    rice_mill_data = (
        db.query(models.Add_Rice_Mill).filter_by(rice_mill_id=rice_mill_id).all()
    )

    agreement_data = (
        db.query(models.Agreement).filter_by(rice_mill_id=rice_mill_id).all()
    )

    adddo_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "agreement_data": [AgreementBase(**row.__dict__) for row in agreement_data],
    }

    return adddo_data


@app.get(
    "/rice-agreement-transporter-truck-society-data/",
    response_model=RiceMillData,
    status_code=status.HTTP_200_OK,
)
async def get_data(db: db_dependency):
    # Fetch data from different tables
    rice_mill_data = db.query(models.Add_Rice_Mill).all()
    agreement_data = db.query(models.Agreement).all()
    truck_data = db.query(models.Truck).all()
    society_data = db.query(models.Society).all()

    # Return the result as a custom response model
    response_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "agreement_data": [AgreementBase(**row.__dict__) for row in agreement_data],
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "society_data": [SocietyBase(**row.__dict__) for row in society_data],
    }

    return response_data


# Rice Deposite
@app.post("/rice-deposite/", status_code=status.HTTP_201_CREATED)
async def rice_deposite(ricedeposite: RiceDepositeBase, db: db_dependency):
    db_rice_depostie = models.Rice_deposite(**ricedeposite.dict())
    db.add(db_rice_depostie)
    db.commit()


@app.get(
    "/rice-deposite-data/",
    response_model=List[RiceDepositeBase],
    status_code=status.HTTP_200_OK,
)
async def rice_deposite_data(db: db_dependency):
    db_rice_deposite_data = db.query(models.Rice_deposite).distinct().all()
    return db_rice_deposite_data


# Kochia
@app.post("/kochia/", status_code=status.HTTP_201_CREATED)
async def add_kochia(addkochia: KochiaBase, db: db_dependency):
    db_kochia = models.Kochia(**addkochia.dict())
    db.add(db_kochia)
    db.commit()


@app.get(
    "/kochia-data/", response_model=List[KochiaBase], status_code=status.HTTP_200_OK
)
async def kochia_data(db: db_dependency):
    db_kochia_data = db.query(models.Kochia).distinct().all()
    return db_kochia_data


# Do Panding
@app.post("/do-panding/", status_code=status.HTTP_201_CREATED)
async def do_panding(dopanding: DoPandingBase, db: db_dependency):
    db_do_panding = models.Do_panding(**dopanding.dict())
    db.add(db_do_panding)
    db.commit()


@app.get(
    "/do-panding-data/",
    response_model=List[DoPandingBase],
    status_code=status.HTTP_200_OK,
)
async def do_panding_data(db: db_dependency):
    db_do_panding_data = db.query(models.Do_panding).distinct().all()
    return db_do_panding_data


# Sauda patrak
@app.post("/sauda-patrak/", status_code=status.HTTP_201_CREATED)
async def sauda_patrak(saudapatrak: SaudaPatrakBase, db: db_dependency):
    db_sauda_patrak = models.Sauda_patrak(**saudapatrak.dict())
    db.add(db_sauda_patrak)
    db.commit()


@app.get(
    "/sauda-patrak-data/",
    response_model=List[SaudaPatrakBase],
    status_code=status.HTTP_200_OK,
)
async def sauda_patrak_data(db: db_dependency):
    db_sauda_patrak_data = db.query(models.Sauda_patrak).distinct().all()
    return db_sauda_patrak_data


# paddy sale
@app.post("/paddy-sale/", status_code=status.HTTP_201_CREATED)
async def paddy_sale(paddysale: PaddySaleBase, db: db_dependency):
    db_paddy_sale = models.Paddy_sale(**paddysale.dict())
    db.add(db_paddy_sale)
    db.commit()


@app.get(
    "/paddy-sale-data/",
    response_model=List[PaddySaleBase],
    status_code=status.HTTP_200_OK,
)
async def paddy_sale_data(db: db_dependency):
    db_paddy_sale_data = db.query(models.Paddy_sale).distinct().all()
    return db_paddy_sale_data


# FRk
@app.post("/frk/", status_code=status.HTTP_201_CREATED)
async def frk(frk: FrkBase, db: db_dependency):
    db_frk = models.Frk(**frk.dict())
    db.add(db_frk)
    db.commit()


@app.get("/frk-data/", response_model=List[FrkBase], status_code=status.HTTP_200_OK)
async def frk_data(db: db_dependency):
    db_frk_data = db.query(models.Frk).distinct().all()
    return db_frk_data


# Dhan rice societies rate
@app.post("/dhan-rice-societies-rate/", status_code=status.HTTP_201_CREATED)
async def dhan_rice_societies_rate(
    dhansocietiesrate: DhanRiceSocietiesRateBase, db: db_dependency
):
    db_dhan_rice_societies_rate = models.Dhan_rice_societies_rate(
        **dhansocietiesrate.dict()
    )
    db.add(db_dhan_rice_societies_rate)
    db.commit()


@app.get(
    "/dhan-rice-societies-rate-data/",
    response_model=List[DhanRiceSocietiesRateBase],
    status_code=status.HTTP_200_OK,
)
async def dhan_rice_societies_rate_data(db: db_dependency):
    db_dhan_rice_societies_rate = (
        db.query(models.Dhan_rice_societies_rate).distinct().all()
    )
    return db_dhan_rice_societies_rate


# lot number master
@app.post("/lot-number-master/", status_code=status.HTTP_201_CREATED)
async def lot_number_master(lotnumbermaster: LotNumberMasterBase, db: db_dependency):
    db_lot_number_master = models.Lot_number_master(**lotnumbermaster.dict())
    db.add(db_lot_number_master)
    db.commit()


@app.get(
    "/lot-number-master-data/",
    response_model=List[LotNumberMasterBase],
    status_code=status.HTTP_200_OK,
)
async def lot_number_master_data(db: db_dependency):
    db_lot_number_master = db.query(models.Lot_number_master).distinct().all()
    return db_lot_number_master


# Dalali dhaan
@app.post("/dalali-dhaan/", status_code=status.HTTP_201_CREATED)
async def dalali_dhaan(dalalidhaan: DalaliDhaanBase, db: db_dependency):
    db_dalali_dhaan = models.Dalali_dhaan(**dalalidhaan.dict())
    db.add(db_dalali_dhaan)
    db.commit()


@app.get(
    "/dalali-dhaan-data/",
    response_model=List[DalaliDhaanBase],
    status_code=status.HTTP_200_OK,
)
async def dalali_dhaan_data_data(db: db_dependency):
    db_dalali_dhaan_data_data = db.query(models.Dalali_dhaan).distinct().all()
    return db_dalali_dhaan_data_data


# Mohan food paddy
@app.post("/mohan-food-paddy/", status_code=status.HTTP_201_CREATED)
async def mohan_food_paddy(mohanfoodpaddy: MohanFoodPaddyBase, db: db_dependency):
    db_mohan_food_paddy = models.Mohan_food_paddy(**mohanfoodpaddy.dict())
    db.add(db_mohan_food_paddy)
    db.commit()


@app.get(
    "/mohan-food-paddy-data/",
    response_model=List[MohanFoodPaddyBase],
    status_code=status.HTTP_200_OK,
)
async def mohan_food_paddy_data(db: db_dependency):
    db_mohan_food_paddy_data = db.query(models.Mohan_food_paddy).distinct().all()
    return db_mohan_food_paddy_data


# Dhan Transporting
@app.post("/dhan-transporting/", status_code=status.HTTP_201_CREATED)
async def dhan_transporting(dhantransporting: DhanTransportingBase, db: db_dependency):
    db_dhan_transporting = models.Dhan_transporting(**dhantransporting.dict())
    db.add(db_dhan_transporting)
    db.commit()


@app.get(
    "/dhan-transporting-data/",
    response_model=List[DhanTransportingBase],
    status_code=status.HTTP_200_OK,
)
async def dhan_transporting_data(db: db_dependency):
    db_dhan_transporting_data = db.query(models.Dhan_transporting).distinct().all()
    return db_dhan_transporting_data


# Transporter master
@app.post("/transporter-master/", status_code=status.HTTP_201_CREATED)
async def transporter_master(
    transportermaster: TransporterMasterBase, db: db_dependency
):
    db_transporter_master = models.Transporter_master(**transportermaster.dict())
    db.add(db_transporter_master)
    db.commit()


@app.get(
    "/transporter-master-data/",
    response_model=List[TransporterMasterBase],
    status_code=status.HTTP_200_OK,
)
async def transporter_master_data(db: db_dependency):
    db_transporter_master_data = db.query(models.Transporter_master).distinct().all()
    return db_transporter_master_data


# About Rice Mill
# @app.post("/add-rice-mill/", status_code=status.HTTP_201_CREATED)
# async def add_rice_mill(addricemill: AddRiceMillBase, db: db_dependency):
#     db_about_rice_mill = models.Add_Rice_Mill(**addricemill.dict())
#     db.add(db_about_rice_mill)
#     db.commit()


@app.post("/add-rice-mill/", status_code=status.HTTP_201_CREATED)
async def add_rice_mill(addricemill: AddRiceMillBase, db: db_dependency):
    existing_rice_mill = (
        db.query(models.Add_Rice_Mill)
        .filter(models.Add_Rice_Mill.rice_mill_name == addricemill.rice_mill_name)
        .first()
    )
    if existing_rice_mill:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Rice Mill with this name already exists",
        )
    db_about_rice_mill = models.Add_Rice_Mill(**addricemill.dict())
    db.add(db_about_rice_mill)
    db.commit()
    db.refresh(db_about_rice_mill)

    return db_about_rice_mill


@app.get(
    "/rice-mill/",
    response_model=List[AddRiceMillBase],
    status_code=status.HTTP_200_OK,
)
async def rice_mill_data(db: db_dependency):
    db_rice_mill_data = db.query(models.Add_Rice_Mill).distinct().all()
    return db_rice_mill_data


# Add New Transporters
# @app.post("/transporter/", status_code=status.HTTP_201_CREATED)
# async def add_new_trasporter(transporters: TransporterBase, db: db_dependency):
#     db_transporter = models.Transporter(**transporters.dict())
#     db.add(db_transporter)
#     db.commit()


@app.post(
    "/transporter/",
    status_code=status.HTTP_201_CREATED,
)
async def add_new_trasporter(transporters: TransporterBase, db: db_dependency):
    existing_transporter = (
        db.query(models.Transporter)
        .filter(models.Transporter.transporter_name == transporters.transporter_name)
        .first()
    )
    if existing_transporter:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Transporter with this name already exists",
        )
    db_transporter = models.Transporter(**transporters.dict())
    db.add(db_transporter)
    db.commit()
    db.refresh(db_transporter)

    return db_transporter


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
# @app.post("/society/", status_code=status.HTTP_201_CREATED)
# async def add_new_society(society: SocietyBase, db: db_dependency):
#     db_society = models.Society(**society.dict())
#     db.add(db_society)
#     db.commit()


@app.post("/society/", status_code=status.HTTP_201_CREATED)
async def add_society(addsociety: SocietyBase, db: db_dependency):
    existing_society = (
        db.query(models.Society)
        .filter(models.Society.society_name == addsociety.society_name)
        .first()
    )
    if existing_society:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Society with this name already exists",
        )
    db_society = models.Society(**addsociety.dict())
    db.add(db_society)
    db.commit()
    db.refresh(db_society)

    return db_society


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
# @app.post("/agreement/", status_code=status.HTTP_201_CREATED)
# async def add_agreement(agreement: AgreementBase, db: db_dependency):
#     db_agreement = models.Agreement(**agreement.dict())
#     db.add(db_agreement)
#     db.commit()


@app.post("/agreement/", status_code=status.HTTP_201_CREATED)
async def add_agreement(addagreement: AgreementBase, db: db_dependency):
    existing_agreement = (
        db.query(models.Agreement)
        .filter(models.Agreement.agreement_number == addagreement.agreement_number)
        .first()
    )
    if existing_agreement:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Society with this name already exists",
        )
    db_agreement = models.Agreement(**addagreement.dict())
    db.add(db_agreement)
    db.commit()
    db.refresh(db_agreement)

    return db_agreement


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


# Whare House
@app.post("/ware-house-transporting/", status_code=status.HTTP_201_CREATED)
async def add_whare_house(warehouse:WareHouseTransporting, db: db_dependency):
    db_add_ware_house = models.ware_house_transporting(**warehouse.dict())
    db.add(db_add_ware_house)
    db.commit()

@app.get("/get-ware-house-data/",response_model=List[WareHouseTransporting],status_code=status.HTTP_200_OK)
async def get_all_ware_house_data(db:db_dependency):
    ware_house_db = db.query(models.ware_house_transporting).distinct().all()
    return ware_house_db


@app.get(
    "/ware-house-data/{warehouse_id}",  # Corrected the path parameter name
    response_model=wareHousetrasportingrate,
    status_code=status.HTTP_200_OK,
)
async def warehouse_data(warehouse_id: int, db: db_dependency):
    warehouse_data = db.query(models.ware_house_transporting).filter_by(ware_houes_id=warehouse_id).first()

    if warehouse_data is None:
        raise HTTPException(status_code=404, detail="Ware House not found")

    response_data = {"ware_house_transporting_rate": warehouse_data.ware_house_transporting_rate}  # Corrected the field name
    return response_data



 