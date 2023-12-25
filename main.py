from fastapi import FastAPI, HTTPException, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Annotated, List, Optional
import models
from database import engine, sessionlocal
from sqlalchemy.orm import Session, joinedload, relationship
from datetime import date, datetime


app = FastAPI()
models.Base.metadata.create_all(bind=engine)

# CORS (Cross-Origin Resource Sharing) middleware configuration
origins = [
    # "http://localhost:5173",
    # "http://localhost:5174",  # Update this with the origin of your React app
]

app.add_middleware(
    CORSMiddleware,
    # allow_origins=origins,
    allow_origins=["*"],
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


class TruckWithTransporter(BaseModel):
    truck_number: str
    transporter_name: str
    transport_id: int
    truck_id: Optional[int] = None


class SocietyBase(BaseModel):
    society_name: str
    distance_from_mill: int
    google_distance: int
    transporting_rate: int
    actual_distance: int
    society_id: Optional[int] = None


class AgreementBase(BaseModel):
    rice_mill_id: int
    agreement_number: str
    type_of_agreement: str
    lot_from: int
    lot_to: int
    agremennt_id: Optional[int] = None


class RiceMillWithAgreement(BaseModel):
    rice_mill_id: int
    agreement_number: str
    type_of_agreement: str
    lot_from: int
    lot_to: int
    rice_mill_name: str
    agremennt_id: Optional[int] = None


class WareHouseTransporting(BaseModel):
    ware_houes_name: str
    ware_house_transporting_rate: int
    hamalirate: int
    ware_houes_id: Optional[int] = None


# ___________________________________________________________


class RiceMillData(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    agreement_data: List[AgreementBase]
    truck_data: List[TruckBase]
    society_data: List[SocietyBase]


class AddDoData(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    agreement_data: List[AgreementBase]


class KochiaBase(BaseModel):
    rice_mill_name_id: int
    kochia_name: str
    kochia_phone_number: int
    kochia_id: Optional[int] = None


class KochiaWithRiceMill(BaseModel):
    rice_mill_name_id: int
    kochia_name: str
    kochia_phone_number: int
    rice_mill_name: str
    kochia_id: Optional[int] = None


class partyBase(BaseModel):
    party_name: str
    party_phone_number: int
    party_id: Optional[int] = None


class brokenBase(BaseModel):
    broker_name: str
    broker_phone_number: int
    broker_id: Optional[int] = None


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


class AddDoWithAddRiceMillAgreementSocietyTruck(BaseModel):
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
    rice_mill_name: str
    agreement_number: str
    society_name: str
    truck_number: str
    do_id: Optional[int] = None
    created_at: Optional[datetime] = None


# ___________________________________________________________
class DhanAwakRiceDoNumber(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    do_number_data: List[AdddoBase]


class DhanAwakRiceDoSocietyTruckTransporter(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    do_number_data: List[AdddoBase]
    society_data: List[SocietyBase]
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


class DhanAwakTruckTransporter(BaseModel):
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


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


class RiceMillTruckNumberPartyBrokers(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    truck_data: List[TruckBase]
    party_data: List[partyBase]
    brokers_data: List[brokenBase]


class OtherAwakBase(BaseModel):
    rst_number: int
    date: date
    rice_mill_name_id: int
    party_id: int
    truck_number_id: int
    material: str
    nos: int
    reason: str
    weight: float
    other_awak_id: Optional[int] = None


class OtherAwakWithPartyRiceTruck(BaseModel):
    rst_number: int
    date: date
    rice_mill_name_id: int
    party_id: int
    truck_number_id: int
    material: str
    nos: int
    reason: str
    weight: float
    party_name: str
    rice_mill_name: str
    truck_number: str
    other_awak_id: Optional[int] = None


# ___________________________________________________________
class wareHousetrasportingrate(BaseModel):
    ware_house_transporting_rate: int
    hamalirate: int


class RiceDepostiRiceTruckTransport(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]
    ware_house_data: List[WareHouseTransporting]


class RiceDepositeBase(BaseModel):
    rst_number: int
    date: date
    lot_number: int
    ware_house_id: int
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
    hamali: int
    rice_depostie_id: Optional[int] = None


class RiceDepositWithRiceWareTruckTransporter(BaseModel):
    rst_number: int
    date: date
    lot_number: int
    ware_house_id: int
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
    hamali: int
    rice_mill_name: str
    truck_number: str
    ware_houes_name: str
    transporter_name: str
    rice_depostie_id: Optional[int] = None


# ___________________________________________________________


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
    sambha_new_bags: int
    sambha_new_weight: int
    paddy_type: str
    total_bags: int
    total_weight: int
    hamali: int
    plastic_bag: int
    jute_bag: int
    weight_less_kata_difference: float
    net_weight: float
    rate: int
    ammount: float
    dalali_dhaan_id: Optional[int] = None


class DalaliDhaanWithKochia(BaseModel):
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
    sambha_new_bags: int
    sambha_new_weight: int
    paddy_type: str
    total_bags: int
    total_weight: int
    hamali: int
    plastic_bag: int
    jute_bag: int
    weight_less_kata_difference: float
    net_weight: float
    rate: int
    ammount: float
    kochia_name: str
    truck_number: str
    dalali_dhaan_id: Optional[int] = None


# ___________________________________________________________


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


class FrkWithRiceTruck(BaseModel):
    date: date
    party: str
    bags: int
    weight: int
    truck_number_id: int
    rice_mill_name_id: int
    bill_number: int
    rate: float
    batch_number: int
    rice_mill_name: str
    truck_number: str
    frk_id: Optional[int] = None


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


class SaudaPatrakWithTruckNumber(BaseModel):
    name: str
    address: str
    vechicle_number_id: int
    paddy: str
    bags: int
    weight: int
    rate: int
    amount: int
    truck_number: str
    sauda_patrak_id: Optional[int] = None


# ___________________________________________________________


class DoPandingBase(BaseModel):
    rice_mill_id: int
    do_number_id: int
    date: date
    mota: str
    patla: str
    sarna: str
    Total: int
    do_panding_id: Optional[int] = None


class DoPandingWithRiceAddDo(BaseModel):
    rice_mill_id: int
    do_number_id: int
    date: date
    mota: str
    patla: str
    sarna: str
    Total: int
    rice_mill_name: str
    do_number: str
    do_panding_id: Optional[int] = None


# ___________________________________________________________
class RiceRstSocietyDoTruckTransporter(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    rst_data: List[DhanAwakBase]
    society_data: List[SocietyBase]
    do_number_data: List[AdddoBase]
    truck_data: List[TruckBase]
    transporter_data: List[TransporterBase]


class RiceMillRstNumber(BaseModel):
    rice_mill_data: List[AddRiceMillBase]
    do_number_data: List[AdddoBase]
    rst_data: List[DhanAwakBase]


class DhanTransportingBase(BaseModel):
    rst_number_id: int
    date: date
    do_number_id: int
    society_name_id: int
    rice_mill_name_id: int
    dm_weight: int
    truck_number_id: int
    transporting_rate: int
    numbers_of_bags: int
    transporting_total: int
    transporter_name_id: int
    status: str
    total_pending: int
    total_paid: int
    Dhan_transporting_id: Optional[int] = None


class DhanTransportingWithRiceDoTruckTransport(BaseModel):
    rst_number_id: int
    date: date
    do_number_id: int
    society_name_id: int
    rice_mill_name_id: int
    dm_weight: int
    truck_number_id: int
    transporting_rate: int
    numbers_of_bags: int
    transporting_total: int
    transporter_name_id: int
    status: str
    total_pending: int
    total_paid: int
    rst_number: int
    rice_mill_name: str
    society_name: str
    do_number: str
    truck_number: str
    transporter_name: str
    Dhan_transporting_id: Optional[int] = None


# ___________________________________________________________
class OtherJawakBase(BaseModel):
    rst_number: int
    date: date
    party_id: int
    truck_number_id: int
    material: str
    nos: int
    reason: str
    weight: float
    rice_mill_name_id: int
    other_jawak_id: Optional[int] = None


class OtherJawakWithPatyTrucksRice(BaseModel):
    rst_number: int
    date: date
    party_id: int
    truck_number_id: int
    material: str
    nos: int
    reason: str
    weight: float
    rice_mill_name_id: int
    party_name: str
    rice_mill_name: str
    truck_number: str
    other_jawak_id: Optional[int] = None


class BrokenJawak(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    broker: int
    brokerage_percentage: float
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    total: int
    brokerage: float
    net_recievable: float
    loading_date: date
    recieved_date: date
    payment_recieved: int
    number_of_days: int
    payment_difference: float
    remarks: str
    broken_jawak_id: Optional[int] = None


class BrokernJawakWithRicePartyBrokerTruck(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    broker: int
    brokerage_percentage: float
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    total: int
    brokerage: float
    net_recievable: float
    loading_date: date
    recieved_date: date
    payment_recieved: int
    number_of_days: int
    payment_difference: float
    remarks: str
    party_name: str
    rice_mill_name: str
    broker_name: str
    truck_number: str
    broken_jawak_id: Optional[int] = None


class HuskJawakBase(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    remarks: str
    broker: int
    brokerage_percentage: float
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    total: int
    brokerage: float
    net_receivable: float
    received_date: date
    loading_date: date
    payment_received: int
    number_of_days: int
    payment_difference: float
    husk_jawak_id: Optional[int] = None


class HuskJawakWithPartyRiceBrokerTruck(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    remarks: str
    broker: int
    brokerage_percentage: float
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    total: int
    brokerage: float
    net_receivable: float
    received_date: date
    loading_date: date
    payment_received: int
    number_of_days: int
    payment_difference: float
    party_name: str
    rice_mill_name: str
    broker_name: str
    truck_number: str
    husk_jawak_id: Optional[int] = None


class NakkhiJawakBase(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    broker: int
    brokerage_percent: int
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    brokerage: float
    total: int
    net_recievable: float
    loading_date: date
    recieved_date: date
    payment_recieved: int
    number_of_days: int
    payment_difference: int
    remarks: str
    nakkhi_jawak_id: Optional[int] = None


class NakkhiWithRicePartyBrokerTruck(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    broker: int
    brokerage_percent: int
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    brokerage: float
    total: int
    net_recievable: float
    loading_date: date
    recieved_date: date
    payment_recieved: int
    number_of_days: int
    payment_difference: int
    remarks: str
    nakkhi_jawak_id: Optional[int] = None
    party_name: str
    rice_mill_name: str
    broker_name: str
    truck_number: str


class BranJawakBase(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    broker: int
    brokerage_percentage: float
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    total: int
    brokerage: float
    net_receivable: float
    payment_received: int
    payment_difference: int
    remarks: str
    oil: int
    bran_jawak_id: Optional[int] = None


class BranJawakWithRicePatryBrokerTruck(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    broker: int
    brokerage_percentage: float
    weight: float
    rate: int
    number_of_bags: int
    truck_number_id: int
    total: int
    brokerage: float
    net_receivable: float
    payment_received: int
    payment_difference: int
    remarks: str
    oil: int
    bran_jawak_id: Optional[int] = None
    party_name: str
    rice_mill_name: str
    broker_name: str
    truck_number: str


class BhushiBase(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    number_of_bags: int
    weight: float
    truck_number_id: int
    rate: int
    amount: int
    bhushi_id: Optional[int] = None


class BhushiWithPartyRiceTruck(BaseModel):
    rst_number: int
    date: date
    party_id: int
    rice_mill_name_id: int
    number_of_bags: int
    weight: float
    truck_number_id: int
    rate: int
    amount: int
    bhushi_id: Optional[int] = None
    party_name: str
    rice_mill_name: str
    truck_number: str


class PaddySaleBase(BaseModel):
    rst_number_id: int
    rice_mill_name_id: int
    date: date
    party_id: int
    broker: int
    loading_form_address: str
    truck_number_id: int
    paddy_name: str
    weight: int
    party_weight: int
    bags: int
    rate: int
    ammount: int
    plastic: int
    joot_old: int
    joot_23_24: int
    joot_22_23: int
    average_bag_wt: float
    paddy_sale_id: Optional[int] = None


class PaddySalesWithDhanawakPartyBrokerTruck(BaseModel):
    rst_number_id: int
    rice_mill_name_id: int
    date: date
    party_id: int
    broker: int
    loading_form_address: str
    truck_number_id: int
    paddy_name: str
    weight: int
    party_weight: int
    bags: int
    rate: int
    ammount: int
    plastic: int
    joot_old: int
    joot_23_24: int
    joot_22_23: int
    average_bag_wt: float
    paddy_sale_id: Optional[int] = None
    rst_number: int
    party_name: str
    broker_name: str
    truck_number: str
    rice_mill_name: str


class DhanAwakDalaliDhan(BaseModel):
    total_weight: List[int]  # Dalali Dhan
    Dhan_data: List[DhanAwakBase]  # Dhan Awak
    Paddy_sale_data: List[PaddySaleBase]  # paddy sale


# class SocietyBase(BaseModel):
#     society_name: str
#     society_id: Optional[int] = None


# # class DhanRiceSocietiesRateBase(BaseModel):
# #     society_name_id: int
# #     distance: float
# #     new: int
# #     dhan_rice_societies_rate_id: Optional[int] = None


# class LotNumberMasterBase(BaseModel):
#     rice_mill_name_id: int
#     lot_number: int
#     lot_number_master_id: Optional[int] = None


# class MohanFoodPaddyBase(BaseModel):
#     date: date
#     do_number_id: int
#     samiti: str
#     rice_mill_name_id: int
#     weight: int
#     vehicle_number_id: int
#     bags: int
#     transporting_total: int
#     transporter_name_id: int
#     transporter_type: str
#     transporter_status: str
#     rate: int
#     type_1: str
#     years_22_23: int
#     years_21_22: int
#     hdpe_one: int
#     hdpe_new: int
#     purana: int
#     pds: int
#     mohan_food_paddy_id: Optional[int] = None


# class TransporterMasterBase(BaseModel):
#     vehicle_number_id: int
#     name: str
#     phone_number: int
#     date: date
#     transporter_name_id: int
#     advance_payment: int
#     transporter_master_id: Optional[int] = None


# # class wareHousetrasportingrate(BaseModel):
# #     ware_house_transporting_rate: int


# class SocietyDistanceRate(BaseModel):
#     transporting_rate: int


def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


# Add Rice Mill
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


# Get Rice Mill Data
@app.get(
    "/rice-mill/",
    response_model=List[AddRiceMillBase],
    status_code=status.HTTP_200_OK,
)
async def rice_mill_data(db: db_dependency):
    db_rice_mill_data = db.query(models.Add_Rice_Mill).distinct().all()
    return db_rice_mill_data


# Add Transporter
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


# Get Transporter Data
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
    existing_truck = (
        db.query(models.Truck)
        .filter(models.Truck.truck_number == truck.truck_number)
        .first()
    )
    if existing_truck:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Truck with this Number already exists",
        )
    db_truck = models.Truck(**truck.dict())
    db.add(db_truck)
    db.commit()


# Get Truck Data
# @app.get("/trucks/", response_model=List[TruckBase], status_code=status.HTTP_200_OK)
# async def get_all_truck_data(db: db_dependency):
#     trucks = db.query(models.Truck).distinct().all()
#     return trucks


@app.get(
    "/trucks/",
    response_model=List[TruckWithTransporter],
    status_code=status.HTTP_200_OK,
)
async def get_all_truck_data(db: Session = Depends(get_db)):
    trucks = db.query(models.Truck).options(joinedload(models.Truck.transporter)).all()

    result = []
    for truck in trucks:
        result.append(
            TruckWithTransporter(
                truck_number=truck.truck_number,
                transporter_name=truck.transporter.transporter_name,
                transport_id=truck.transport_id,
                truck_id=truck.truck_id,
            )
        )

    return result


# Get all truck numbers for dropdown options
@app.get("/truck-numbers/", response_model=List[str], status_code=status.HTTP_200_OK)
async def get_truck_numbers(db: db_dependency):
    db_truck_numbers = db.query(models.Truck.truck_number).distinct().all()
    return [truck_number[0] for truck_number in db_truck_numbers]


# Add Society
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


# Get Society Data
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


# Add Agreement
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


# Get Agreement Data
# @app.get(
#     "/agreements/", response_model=List[AgreementBase], status_code=status.HTTP_200_OK
# )
# async def get_all_agreement_data(db: db_dependency):
#     agreements = db.query(models.Agreement).distinct().all()
#     return agreements


@app.get(
    "/agreements/",
    response_model=List[RiceMillWithAgreement],
    status_code=status.HTTP_200_OK,
)
async def get_all_agreements_data(db: Session = Depends(get_db)):
    agreements = (
        db.query(models.Agreement)
        .options(joinedload(models.Agreement.addricemill))
        .all()
    )

    result = []
    for agreement in agreements:
        result.append(
            RiceMillWithAgreement(
                rice_mill_id=agreement.rice_mill_id,
                agreement_number=agreement.agreement_number,
                type_of_agreement=agreement.type_of_agreement,
                lot_from=agreement.lot_from,
                lot_to=agreement.lot_to,
                agremennt_id=agreement.agremennt_id,
                rice_mill_name=agreement.addricemill.rice_mill_name,
            )
        )

    return result


# Get all agreements number for dropdown options
@app.get(
    "/agreements-number/", response_model=List[int], status_code=status.HTTP_200_OK
)
async def get_all_agreements_number(db: db_dependency):
    db_agreements_number = db.query(models.Agreement.agreement_number).distinct().all()
    return [agreement_number[0] for agreement_number in db_agreements_number]


# Whare House
@app.post("/ware-house-transporting/", status_code=status.HTTP_201_CREATED)
async def add_whare_house(warehouse: WareHouseTransporting, db: db_dependency):
    db_add_ware_house = models.ware_house_transporting(**warehouse.dict())
    db.add(db_add_ware_house)
    db.commit()


@app.get(
    "/get-ware-house-data/",
    response_model=List[WareHouseTransporting],
    status_code=status.HTTP_200_OK,
)
async def get_all_ware_house_data(db: db_dependency):
    ware_house_db = db.query(models.ware_house_transporting).distinct().all()
    return ware_house_db


# Kochia
@app.post("/kochia/", status_code=status.HTTP_201_CREATED)
async def add_kochia(addkochia: KochiaBase, db: db_dependency):
    db_kochia = models.Kochia(**addkochia.dict())
    db.add(db_kochia)
    db.commit()


# @app.get(
#     "/kochia-data/", response_model=List[KochiaBase], status_code=status.HTTP_200_OK
# )
# async def kochia_data(db: db_dependency):
#     db_kochia_data = db.query(models.Kochia).distinct().all()
#     return db_kochia_data


@app.get(
    "/kochia-data/",
    response_model=List[KochiaWithRiceMill],
    status_code=status.HTTP_200_OK,
)
async def get_all_kochia_data(db: Session = Depends(get_db)):
    kochias = (
        db.query(models.Kochia).options(joinedload(models.Kochia.addricemill)).all()
    )

    result = []
    for kochia in kochias:
        result.append(
            KochiaWithRiceMill(
                rice_mill_name_id=kochia.rice_mill_name_id,
                kochia_name=kochia.kochia_name,
                kochia_phone_number=kochia.kochia_phone_number,
                kochia_id=kochia.kochia_id,
                rice_mill_name=kochia.addricemill.rice_mill_name,
            )
        )

    return result


# Party
@app.post("/party/", status_code=status.HTTP_201_CREATED)
async def add_party(party: partyBase, db: db_dependency):
    db_add_party = models.Party(**party.dict())
    db.add(db_add_party)
    db.commit()


@app.get(
    "/party-data/",
    response_model=List[partyBase],
    status_code=status.HTTP_200_OK,
)
async def get_party_data(db: db_dependency):
    db_party_data = db.query(models.Party).distinct().all()
    return db_party_data


# broker
@app.post("/broker/", status_code=status.HTTP_201_CREATED)
async def add_broker(broker: brokenBase, db: db_dependency):
    db_add_broker = models.brokers(**broker.dict())
    db.add(db_add_broker)
    db.commit()


@app.get(
    "/broker-data/",
    response_model=List[brokenBase],
    status_code=status.HTTP_200_OK,
)
async def get_broker_data(db: db_dependency):
    db_broker_data = db.query(models.brokers).distinct().all()
    return db_broker_data


# _______________________________________________________
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


# ADD DO Agreement Number
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


# Add Do
@app.post("/add-do/", status_code=status.HTTP_201_CREATED)
async def add_do(adddo: AdddoBase, db: db_dependency):
    db_add_do = models.Add_Do(**adddo.dict())
    db.add(db_add_do)
    db.commit()


# @app.get(
#     "/add-do-data/", response_model=List[AdddoBase], status_code=status.HTTP_200_OK
# )
# async def get_all_add_do_data(db: db_dependency):
#     add_do = db.query(models.Add_Do).distinct().all()
#     return add_do


@app.get(
    "/add-do-data/",
    response_model=List[AddDoWithAddRiceMillAgreementSocietyTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_add_do_data(db: Session = Depends(get_db)):
    Add_Dos = (
        db.query(models.Add_Do)
        .options(
            joinedload(models.Add_Do.addricemill),
            joinedload(models.Add_Do.agreement),
            joinedload(models.Add_Do.society),
            joinedload(models.Add_Do.trucks),
        )
        .all()
    )

    result = []
    for Add_Do in Add_Dos:
        result.append(
            AddDoWithAddRiceMillAgreementSocietyTruck(
                select_mill_id=Add_Do.select_mill_id,
                date=Add_Do.date,
                do_number=Add_Do.do_number,
                select_argeement_id=Add_Do.select_argeement_id,
                moto_weight=Add_Do.moto_weight,
                mota_Bardana=Add_Do.mota_Bardana,
                patla_weight=Add_Do.patla_weight,
                patla_bardana=Add_Do.patla_bardana,
                sarna_weight=Add_Do.sarna_weight,
                sarna_bardana=Add_Do.sarna_bardana,
                total_weight=Add_Do.total_weight,
                total_bardana=Add_Do.total_bardana,
                society_name_id=Add_Do.society_name_id,
                truck_number_id=Add_Do.truck_number_id,
                created_at=Add_Do.created_at,
                rice_mill_name=Add_Do.addricemill.rice_mill_name,
                agreement_number=Add_Do.agreement.agreement_number,
                society_name=Add_Do.society.society_name,
                truck_number=Add_Do.trucks.truck_number,
                do_id=Add_Do.do_id,
            )
        )

    return result


# ________________________________________________________


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


# ________________________________________________________
@app.get(
    "/rice-truck-party-brokers/",
    response_model=RiceMillTruckNumberPartyBrokers,
    status_code=status.HTTP_200_OK,
)
async def broken_data(db: db_dependency):
    rice_mill_data = db.query(models.Add_Rice_Mill).all()
    truck_data = db.query(models.Truck).all()
    party_data = db.query(models.Party).all()
    brokers_data = db.query(models.brokers).all()

    broken_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "party_data": [partyBase(**row.__dict__) for row in party_data],
        "brokers_data": [brokenBase(**row.__dict__) for row in brokers_data],
    }
    return broken_data


# Other Awak
@app.post("/other-awak/", status_code=status.HTTP_201_CREATED)
async def add_other_awak(otherawak: OtherAwakBase, db: db_dependency):
    db_add_other_awak = models.Other_awak(**otherawak.dict())
    db.add(db_add_other_awak)
    db.commit()


# @app.get(
#     "/other-awak-data/",
#     response_model=List[OtherAwakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_awak_data(db: db_dependency):
#     db_get_other_awak_data = db.query(models.other_awak).distinct().all()
#     return db_get_other_awak_data


@app.get(
    "/other-awak-data/",
    response_model=List[OtherAwakWithPartyRiceTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_other_awak_data(db: Session = Depends(get_db)):
    other_awaks = (
        db.query(models.Other_awak)
        .options(
            joinedload(models.Other_awak.addricemill),
            joinedload(models.Other_awak.trucks),
            joinedload(models.Other_awak.party),
        )
        .all()
    )

    result = []
    for other_awak in other_awaks:
        result.append(
            OtherAwakWithPartyRiceTruck(
                rst_number=other_awak.rst_number,
                date=other_awak.date,
                rice_mill_name_id=other_awak.rice_mill_name_id,
                party_id=other_awak.party_id,
                truck_number_id=other_awak.truck_number_id,
                material=other_awak.material,
                nos=other_awak.nos,
                reason=other_awak.reason,
                weight=other_awak.weight,
                party_name=other_awak.party.party_name,
                rice_mill_name=other_awak.addricemill.rice_mill_name,
                truck_number=other_awak.trucks.truck_number,
                other_awak_id=other_awak.other_awak_id,
            )
        )

    return result


# ________________________________________________________
@app.get(
    "/ware-house-data/{warehouse_id}",  # Corrected the path parameter name
    response_model=wareHousetrasportingrate,
    status_code=status.HTTP_200_OK,
)
async def warehouse_data(warehouse_id: int, db: db_dependency):
    warehouse_data = (
        db.query(models.ware_house_transporting)
        .filter_by(ware_houes_id=warehouse_id)
        .first()
    )

    if warehouse_data is None:
        raise HTTPException(status_code=404, detail="Ware House not found")

    response_data = {
        "ware_house_transporting_rate": warehouse_data.ware_house_transporting_rate,
        "hamalirate": warehouse_data.hamalirate,
    }  #
    return response_data


# Rice Deposti
@app.get(
    "/rice-truck-transporter-ware-house/",
    response_model=RiceDepostiRiceTruckTransport,
    status_code=status.HTTP_200_OK,
)
async def rice_deposit_data(db: db_dependency):
    rice_mill_data = db.query(models.Add_Rice_Mill).all()
    truck_data = db.query(models.Truck).all()
    transporter_data = db.query(models.Transporter).all()
    ware_house_data = db.query(models.ware_house_transporting).all()

    rice_deposit_data = {
        "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
        "truck_data": [TruckBase(**row.__dict__) for row in truck_data],
        "transporter_data": [
            TransporterBase(**row.__dict__) for row in transporter_data
        ],
        "ware_house_data": [
            WareHouseTransporting(**row.__dict__) for row in ware_house_data
        ],
    }
    return rice_deposit_data


# Rice Deposite
@app.post("/rice-deposite/", status_code=status.HTTP_201_CREATED)
async def rice_deposite(ricedeposite: RiceDepositeBase, db: db_dependency):
    db_rice_depostie = models.Rice_deposite(**ricedeposite.dict())
    db.add(db_rice_depostie)
    db.commit()


# @app.get(
#     "/rice-deposite-data/",
#     response_model=List[RiceDepositeBase],
#     status_code=status.HTTP_200_OK,
# )
# async def rice_deposite_data(db: db_dependency):
#     db_rice_deposite_data = db.query(models.Rice_deposite).distinct().all()
#     return db_rice_deposite_data


@app.get(
    "/rice-deposite-data/",
    response_model=List[RiceDepositWithRiceWareTruckTransporter],
    status_code=status.HTTP_200_OK,
)
async def get_all_rice_deposite_data(db: Session = Depends(get_db)):
    rices_deposite = (
        db.query(models.Rice_deposite)
        .options(
            joinedload(models.Rice_deposite.addricemill),
            joinedload(models.Rice_deposite.warehousetransporting),
            joinedload(models.Rice_deposite.trucks),
            joinedload(models.Rice_deposite.transporter),
        )
        .all()
    )

    result = []
    for rice_deposite in rices_deposite:
        result.append(
            RiceDepositWithRiceWareTruckTransporter(
                rst_number=rice_deposite.rst_number,
                date=rice_deposite.date,
                lot_number=rice_deposite.lot_number,
                ware_house_id=rice_deposite.ware_house_id,
                rice_mill_name_id=rice_deposite.rice_mill_name_id,
                weight=rice_deposite.weight,
                truck_number_id=rice_deposite.truck_number_id,
                bags=rice_deposite.bags,
                transporting_total=rice_deposite.transporting_total,
                transporter_name_id=rice_deposite.transporter_name_id,
                transporting_type=rice_deposite.transporting_type,
                transporting_status=rice_deposite.transporting_status,
                rate=rice_deposite.rate,
                variety=rice_deposite.variety,
                halting=rice_deposite.halting,
                rrga_wt=rice_deposite.rrga_wt,
                data_2022_23=rice_deposite.data_2022_23,
                data_2021_22=rice_deposite.data_2021_22,
                pds=rice_deposite.pds,
                old=rice_deposite.old,
                amount=rice_deposite.amount,
                status=rice_deposite.status,
                hamali=rice_deposite.hamali,
                rice_mill_name=rice_deposite.addricemill.rice_mill_name,
                truck_number=rice_deposite.trucks.truck_number,
                ware_houes_name=rice_deposite.warehousetransporting.ware_houes_name,
                transporter_name=rice_deposite.transporter.transporter_name,
                rice_depostie_id=rice_deposite.rice_depostie_id,
            )
        )

    return result


# ________________________________________________________
# Dalali dhaan
@app.post("/dalali-dhaan/", status_code=status.HTTP_201_CREATED)
async def dalali_dhaan(dalalidhaan: DalaliDhaanBase, db: db_dependency):
    db_dalali_dhaan = models.Dalali_dhaan(**dalalidhaan.dict())
    db.add(db_dalali_dhaan)
    db.commit()


# @app.get(
#     "/dalali-dhaan-data/",
#     response_model=List[DalaliDhaanBase],
#     status_code=status.HTTP_200_OK,
# )
# async def dalali_dhaan_data_data(db: db_dependency):
#     db_dalali_dhaan_data_data = db.query(models.Dalali_dhaan).distinct().all()
#     return db_dalali_dhaan_data_data


@app.get(
    "/dalali-dhaan-data/",
    response_model=List[DalaliDhaanWithKochia],
    status_code=status.HTTP_200_OK,
)
async def get_all_dalali_dhaan_data(db: Session = Depends(get_db)):
    Dalali_dhaans = (
        db.query(models.Dalali_dhaan)
        .options(
            joinedload(models.Dalali_dhaan.kochia),
            joinedload(models.Dalali_dhaan.trucks),
        )
        .all()
    )

    result = []
    for Dalali_dhaan in Dalali_dhaans:
        result.append(
            DalaliDhaanWithKochia(
                rst_number=Dalali_dhaan.rst_number,
                date=Dalali_dhaan.date,
                kochia_id=Dalali_dhaan.kochia_id,
                vehicale_number_id=Dalali_dhaan.vehicale_number_id,
                white_sarna_bags=Dalali_dhaan.white_sarna_bags,
                white_sarna_weight=Dalali_dhaan.white_sarna_weight,
                ir_bags=Dalali_dhaan.ir_bags,
                ir_weight=Dalali_dhaan.ir_weight,
                rb_gold_bags=Dalali_dhaan.rb_gold_bags,
                rb_gold_weight=Dalali_dhaan.rb_gold_weight,
                sarna_bags=Dalali_dhaan.sarna_bags,
                sarna_weight=Dalali_dhaan.sarna_weight,
                sambha_new_bags=Dalali_dhaan.sambha_new_bags,
                sambha_new_weight=Dalali_dhaan.sambha_new_weight,
                paddy_type=Dalali_dhaan.paddy_type,
                total_bags=Dalali_dhaan.total_bags,
                total_weight=Dalali_dhaan.total_weight,
                hamali=Dalali_dhaan.hamali,
                plastic_bag=Dalali_dhaan.plastic_bag,
                jute_bag=Dalali_dhaan.jute_bag,
                weight_less_kata_difference=Dalali_dhaan.weight_less_kata_difference,
                net_weight=Dalali_dhaan.net_weight,
                rate=Dalali_dhaan.rate,
                ammount=Dalali_dhaan.ammount,
                kochia_name=Dalali_dhaan.kochia.kochia_name,
                truck_number=Dalali_dhaan.trucks.truck_number,
                dalali_dhaan_id=Dalali_dhaan.dalali_dhaan_id,
            )
        )

    return result


# ________________________________________________________


# FRk
@app.post("/frk/", status_code=status.HTTP_201_CREATED)
async def frk(frk: FrkBase, db: db_dependency):
    db_frk = models.Frk(**frk.dict())
    db.add(db_frk)
    db.commit()


# @app.get("/frk-data/", response_model=List[FrkBase], status_code=status.HTTP_200_OK)
# async def frk_data(db: db_dependency):
#     db_frk_data = db.query(models.Frk).distinct().all()
#     return db_frk_data


@app.get(
    "/frk-data/",
    response_model=List[FrkWithRiceTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_add_do_data(db: Session = Depends(get_db)):
    frks = (
        db.query(models.Frk)
        .options(
            joinedload(models.Frk.addricemill),
            joinedload(models.Frk.trucks),
        )
        .all()
    )

    result = []
    for frk in frks:
        result.append(
            FrkWithRiceTruck(
                date=frk.date,
                party=frk.party,
                bags=frk.bags,
                weight=frk.weight,
                truck_number_id=frk.truck_number_id,
                rice_mill_name_id=frk.rice_mill_name_id,
                bill_number=frk.bill_number,
                rate=frk.rate,
                batch_number=frk.batch_number,
                rice_mill_name=frk.addricemill.rice_mill_name,
                truck_number=frk.trucks.truck_number,
                frk_id=frk.frk_id,
            )
        )

    return result


# ________________________________________________________


# Sauda patrak
@app.post("/sauda-patrak/", status_code=status.HTTP_201_CREATED)
async def sauda_patrak(saudapatrak: SaudaPatrakBase, db: db_dependency):
    db_sauda_patrak = models.Sauda_patrak(**saudapatrak.dict())
    db.add(db_sauda_patrak)
    db.commit()


# @app.get(
#     "/sauda-patrak-data/",
#     response_model=List[SaudaPatrakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def sauda_patrak_data(db: db_dependency):
#     db_sauda_patrak_data = db.query(models.Sauda_patrak).distinct().all()
#     return db_sauda_patrak_data


@app.get(
    "/sauda-patrak-data/",
    response_model=List[SaudaPatrakWithTruckNumber],
    status_code=status.HTTP_200_OK,
)
async def get_all_sauda_patrak_data(db: Session = Depends(get_db)):
    saudas_patrak = (
        db.query(models.Sauda_patrak)
        .options(
            joinedload(models.Sauda_patrak.trucks),
        )
        .all()
    )

    result = []
    for sauda_patrak in saudas_patrak:
        result.append(
            SaudaPatrakWithTruckNumber(
                name=sauda_patrak.name,
                address=sauda_patrak.address,
                vechicle_number_id=sauda_patrak.vechicle_number_id,
                paddy=sauda_patrak.paddy,
                bags=sauda_patrak.bags,
                weight=sauda_patrak.weight,
                rate=sauda_patrak.rate,
                amount=sauda_patrak.amount,
                truck_number=sauda_patrak.trucks.truck_number,
                sauda_patrak_id=sauda_patrak.sauda_patrak_id,
            )
        )

    return result


# ________________________________________________________
# Do Panding
@app.post("/do-panding/", status_code=status.HTTP_201_CREATED)
async def do_panding(dopanding: DoPandingBase, db: db_dependency):
    db_do_panding = models.Do_panding(**dopanding.dict())
    db.add(db_do_panding)
    db.commit()


# @app.get(
#     "/do-panding-data/",
#     response_model=List[DoPandingBase],
#     status_code=status.HTTP_200_OK,
# )
# async def do_panding_data(db: db_dependency):
#     db_do_panding_data = db.query(models.Do_panding).distinct().all()
#     return db_do_panding_data


@app.get(
    "/do-panding-data/",
    response_model=List[DoPandingWithRiceAddDo],
    status_code=status.HTTP_200_OK,
)
async def get_all_sauda_patrak_data(db: Session = Depends(get_db)):
    dos_pending = (
        db.query(models.Do_panding)
        .options(
            joinedload(models.Do_panding.addricemill),
            joinedload(models.Do_panding.add_do),
        )
        .all()
    )

    result = []
    for do_pending in dos_pending:
        result.append(
            DoPandingWithRiceAddDo(
                rice_mill_id=do_pending.rice_mill_id,
                do_number_id=do_pending.do_number_id,
                date=do_pending.date,
                mota=do_pending.mota,
                patla=do_pending.patla,
                sarna=do_pending.sarna,
                Total=do_pending.Total,
                rice_mill_name=do_pending.addricemill.rice_mill_name,
                do_number=do_pending.add_do.do_number,
                do_panding_id=do_pending.do_panding_id,
            )
        )

    return result


# ________________________________________________________
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


# Dhan Transporting
@app.post("/dhan-transporting/", status_code=status.HTTP_201_CREATED)
async def dhan_transporting(dhantransporting: DhanTransportingBase, db: db_dependency):
    db_dhan_transporting = models.Dhan_transporting(**dhantransporting.dict())
    db.add(db_dhan_transporting)
    db.commit()


# @app.get(
#     "/dhan-transporting-data/",
#     response_model=List[DhanTransportingBase],
#     status_code=status.HTTP_200_OK,
# )
# async def dhan_transporting_data(db: db_dependency):
#     db_dhan_transporting_data = db.query(models.Dhan_transporting).distinct().all()
#     return db_dhan_transporting_data


@app.get(
    "/dhan-transporting-data/",
    response_model=List[DhanTransportingWithRiceDoTruckTransport],
    status_code=status.HTTP_200_OK,
)
async def get_all_sauda_patrak_data(db: Session = Depends(get_db)):
    dhans_transporting = (
        db.query(models.Dhan_transporting)
        .options(
            joinedload(models.Dhan_transporting.addricemill),
            joinedload(models.Dhan_transporting.society),
            joinedload(models.Dhan_transporting.add_do),
            joinedload(models.Dhan_transporting.trucks),
            joinedload(models.Dhan_transporting.transporter),
            joinedload(models.Dhan_transporting.dhanawak),
        )
        .all()
    )

    result = []
    for dhan_transporting in dhans_transporting:
        result.append(
            DhanTransportingWithRiceDoTruckTransport(
                rst_number_id=dhan_transporting.rst_number_id,
                date=dhan_transporting.date,
                do_number_id=dhan_transporting.do_number_id,
                society_name_id=dhan_transporting.society_name_id,
                rice_mill_name_id=dhan_transporting.rice_mill_name_id,
                dm_weight=dhan_transporting.dm_weight,
                truck_number_id=dhan_transporting.truck_number_id,
                transporting_rate=dhan_transporting.transporting_rate,
                numbers_of_bags=dhan_transporting.numbers_of_bags,
                transporting_total=dhan_transporting.transporting_total,
                transporter_name_id=dhan_transporting.transporter_name_id,
                status=dhan_transporting.status,
                total_pending=dhan_transporting.total_pending,
                total_paid=dhan_transporting.total_paid,
                rst_number=dhan_transporting.dhanawak.rst_number,
                rice_mill_name=dhan_transporting.addricemill.rice_mill_name,
                society_name=dhan_transporting.society.society_name,
                do_number=dhan_transporting.add_do.do_number,
                truck_number=dhan_transporting.trucks.truck_number,
                transporter_name=dhan_transporting.transporter.transporter_name,
                Dhan_transporting_id=dhan_transporting.Dhan_transporting_id,
            )
        )

    return result


# ________________________________________________________
# Other Jawak
@app.post("/other-jawak/", status_code=status.HTTP_201_CREATED)
async def add_other_jawak(otherjawak: OtherJawakBase, db: db_dependency):
    db_add_other_jawak = models.Other_jawak(**otherjawak.dict())
    db.add(db_add_other_jawak)
    db.commit()


# @app.get(
#     "/other-jawak-data/",
#     response_model=List[OtherJawakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_jawak_data(db: db_dependency):
#     db_get_other_jawak_data = db.query(models.Other_jawak).distinct().all()
#     return db_get_other_jawak_data


@app.get(
    "/other-jawak-data/",
    response_model=List[OtherJawakWithPatyTrucksRice],
    status_code=status.HTTP_200_OK,
)
async def get_all_other_jawak_data(db: Session = Depends(get_db)):
    other_jawaks = (
        db.query(models.Other_jawak)
        .options(
            joinedload(models.Other_jawak.addricemill),
            joinedload(models.Other_jawak.trucks),
            joinedload(models.Other_jawak.party),
        )
        .all()
    )

    result = []
    for other_jawak in other_jawaks:
        result.append(
            OtherJawakWithPatyTrucksRice(
                rst_number=other_jawak.rst_number,
                date=other_jawak.date,
                rice_mill_name_id=other_jawak.rice_mill_name_id,
                party_id=other_jawak.party_id,
                truck_number_id=other_jawak.truck_number_id,
                material=other_jawak.material,
                nos=other_jawak.nos,
                reason=other_jawak.reason,
                weight=other_jawak.weight,
                party_name=other_jawak.party.party_name,
                rice_mill_name=other_jawak.addricemill.rice_mill_name,
                truck_number=other_jawak.trucks.truck_number,
                other_jawak_id=other_jawak.other_jawak_id,
            )
        )

    return result


# ________________________________________________________
# Broken Jawak
@app.post("/broken-jawak/", status_code=status.HTTP_201_CREATED)
async def add_broken_jawak(brokenjawak: BrokenJawak, db: db_dependency):
    db_add_broken_jawak = models.broken_jawak(**brokenjawak.dict())
    db.add(db_add_broken_jawak)
    db.commit()


# @app.get(
#     "/other-broken-jawak-data/",
#     response_model=List[BrokenJawak],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_broken_jawak_data(db: db_dependency):
#     db_get_other_broken_jawak_data = db.query(models.broken_jawak).distinct().all()
#     return db_get_other_broken_jawak_data


@app.get(
    "/other-broken-jawak-data/",
    response_model=List[BrokernJawakWithRicePartyBrokerTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_other_jawak_data(db: Session = Depends(get_db)):
    brokens_jawak = (
        db.query(models.broken_jawak)
        .options(
            joinedload(models.broken_jawak.addricemill),
            joinedload(models.broken_jawak.trucks),
            joinedload(models.broken_jawak.party),
            joinedload(models.broken_jawak.brokers),
        )
        .all()
    )

    result = []
    for broken_jawak in brokens_jawak:
        result.append(
            BrokernJawakWithRicePartyBrokerTruck(
                rst_number=broken_jawak.rst_number,
                date=broken_jawak.date,
                party_id=broken_jawak.party_id,
                rice_mill_name_id=broken_jawak.rice_mill_name_id,
                broker=broken_jawak.broker,
                brokerage_percentage=broken_jawak.brokerage_percentage,
                weight=broken_jawak.weight,
                rate=broken_jawak.rate,
                number_of_bags=broken_jawak.number_of_bags,
                truck_number_id=broken_jawak.truck_number_id,
                total=broken_jawak.total,
                brokerage=broken_jawak.brokerage,
                net_recievable=broken_jawak.net_recievable,
                loading_date=broken_jawak.loading_date,
                recieved_date=broken_jawak.recieved_date,
                payment_recieved=broken_jawak.payment_recieved,
                number_of_days=broken_jawak.number_of_days,
                payment_difference=broken_jawak.payment_difference,
                remarks=broken_jawak.remarks,
                broken_jawak_id=broken_jawak.broken_jawak_id,
                party_name=broken_jawak.party.party_name,
                rice_mill_name=broken_jawak.addricemill.rice_mill_name,
                broker_name=broken_jawak.brokers.broker_name,
                truck_number=broken_jawak.trucks.truck_number,
            )
        )

    return result


# ________________________________________________________


# Husk Jawak
@app.post("/husk-jawak/", status_code=status.HTTP_201_CREATED)
async def add_husk_jawak(huskjawak: HuskJawakBase, db: db_dependency):
    db_add_husk_jawak = models.husk_jawak(**huskjawak.dict())
    db.add(db_add_husk_jawak)
    db.commit()


# @app.get(
#     "/other-husk-jawak-data/",
#     response_model=List[HuskJawakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_husk_jawak_data(db: db_dependency):
#     db_get_other_husk_jawak_data = db.query(models.husk_jawak).distinct().all()
#     return db_get_other_husk_jawak_data


@app.get(
    "/other-husk-jawak-data/",
    response_model=List[HuskJawakWithPartyRiceBrokerTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_husk_jawak_data(db: Session = Depends(get_db)):
    husks_jawak = (
        db.query(models.husk_jawak)
        .options(
            joinedload(models.husk_jawak.addricemill),
            joinedload(models.husk_jawak.trucks),
            joinedload(models.husk_jawak.party),
            joinedload(models.husk_jawak.brokers),
        )
        .all()
    )

    result = []
    for husk_jawak in husks_jawak:
        result.append(
            HuskJawakWithPartyRiceBrokerTruck(
                rst_number=husk_jawak.rst_number,
                date=husk_jawak.date,
                party_id=husk_jawak.party_id,
                rice_mill_name_id=husk_jawak.rice_mill_name_id,
                remarks=husk_jawak.remarks,
                broker=husk_jawak.broker,
                brokerage_percentage=husk_jawak.brokerage_percentage,
                weight=husk_jawak.weight,
                rate=husk_jawak.rate,
                number_of_bags=husk_jawak.number_of_bags,
                truck_number_id=husk_jawak.truck_number_id,
                total=husk_jawak.total,
                brokerage=husk_jawak.brokerage,
                net_receivable=husk_jawak.net_receivable,
                received_date=husk_jawak.received_date,
                loading_date=husk_jawak.loading_date,
                payment_received=husk_jawak.payment_received,
                number_of_days=husk_jawak.number_of_days,
                payment_difference=husk_jawak.payment_difference,
                party_name=husk_jawak.party.party_name,
                rice_mill_name=husk_jawak.addricemill.rice_mill_name,
                broker_name=husk_jawak.brokers.broker_name,
                truck_number=husk_jawak.trucks.truck_number,
                husk_jawak_id=husk_jawak.husk_jawak_id,
            )
        )

    return result


# ________________________________________________________


# nakkhi_jawak
@app.post("/nakkhi-jawak/", status_code=status.HTTP_201_CREATED)
async def add_nakkhi_jawak(nakkhijawak: NakkhiJawakBase, db: db_dependency):
    db_add_nakkhi_jawak = models.nakkhi_jawak(**nakkhijawak.dict())
    db.add(db_add_nakkhi_jawak)
    db.commit()


# @app.get(
#     "/other-nakkhi-jawak-data/",
#     response_model=List[NakkhiJawakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_nakkhi_jawak_data(db: db_dependency):
#     db_get_other_nakkhi_jawak_data = db.query(models.nakkhi_jawak).distinct().all()
#     return db_get_other_nakkhi_jawak_data


@app.get(
    "/other-nakkhi-jawak-data/",
    response_model=List[NakkhiWithRicePartyBrokerTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_nakkhi_jawak_data(db: Session = Depends(get_db)):
    nakkhis_jawak = (
        db.query(models.nakkhi_jawak)
        .options(
            joinedload(models.nakkhi_jawak.addricemill),
            joinedload(models.nakkhi_jawak.trucks),
            joinedload(models.nakkhi_jawak.party),
            joinedload(models.nakkhi_jawak.brokers),
        )
        .all()
    )

    result = []
    for nakkhi_jawak in nakkhis_jawak:
        result.append(
            NakkhiWithRicePartyBrokerTruck(
                rst_number=nakkhi_jawak.rst_number,
                date=nakkhi_jawak.date,
                party_id=nakkhi_jawak.party_id,
                rice_mill_name_id=nakkhi_jawak.rice_mill_name_id,
                broker=nakkhi_jawak.broker,
                brokerage_percent=nakkhi_jawak.brokerage_percent,
                weight=nakkhi_jawak.weight,
                rate=nakkhi_jawak.rate,
                number_of_bags=nakkhi_jawak.number_of_bags,
                truck_number_id=nakkhi_jawak.truck_number_id,
                brokerage=nakkhi_jawak.brokerage,
                total=nakkhi_jawak.total,
                net_recievable=nakkhi_jawak.net_recievable,
                loading_date=nakkhi_jawak.loading_date,
                recieved_date=nakkhi_jawak.recieved_date,
                payment_recieved=nakkhi_jawak.payment_recieved,
                number_of_days=nakkhi_jawak.number_of_days,
                payment_difference=nakkhi_jawak.payment_difference,
                remarks=nakkhi_jawak.remarks,
                nakkhi_jawak_id=nakkhi_jawak.nakkhi_jawak_id,
                party_name=nakkhi_jawak.party.party_name,
                rice_mill_name=nakkhi_jawak.addricemill.rice_mill_name,
                broker_name=nakkhi_jawak.brokers.broker_name,
                truck_number=nakkhi_jawak.trucks.truck_number,
            )
        )

    return result


# ________________________________________________________


# bran jawak
@app.post("/bran-jawak/", status_code=status.HTTP_201_CREATED)
async def add_bran_jawak(branjawak: BranJawakBase, db: db_dependency):
    db_add_bran_jawak = models.bran_jawak(**branjawak.dict())
    db.add(db_add_bran_jawak)
    db.commit()


# @app.get(
#     "/other-bran-jawak-data/",
#     response_model=List[BranJawakBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_bran_jawak_data(db: db_dependency):
#     db_get_other_bran_jawak_data = db.query(models.bran_jawak).distinct().all()
#     return db_get_other_bran_jawak_data


@app.get(
    "/other-bran-jawak-data/",
    response_model=List[BranJawakWithRicePatryBrokerTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_bran_jawak_data(db: Session = Depends(get_db)):
    brans_jawak = (
        db.query(models.bran_jawak)
        .options(
            joinedload(models.bran_jawak.addricemill),
            joinedload(models.bran_jawak.trucks),
            joinedload(models.bran_jawak.party),
            joinedload(models.bran_jawak.brokers),
        )
        .all()
    )

    result = []
    for bran_jawak in brans_jawak:
        result.append(
            BranJawakWithRicePatryBrokerTruck(
                rst_number=bran_jawak.rst_number,
                date=bran_jawak.date,
                party_id=bran_jawak.party_id,
                rice_mill_name_id=bran_jawak.rice_mill_name_id,
                broker=bran_jawak.broker,
                brokerage_percentage=bran_jawak.brokerage_percentage,
                weight=bran_jawak.weight,
                rate=bran_jawak.rate,
                number_of_bags=bran_jawak.number_of_bags,
                truck_number_id=bran_jawak.truck_number_id,
                total=bran_jawak.total,
                brokerage=bran_jawak.brokerage,
                net_receivable=bran_jawak.net_receivable,
                payment_received=bran_jawak.payment_received,
                payment_difference=bran_jawak.payment_difference,
                remarks=bran_jawak.remarks,
                oil=bran_jawak.oil,
                bran_jawak_id=bran_jawak.bran_jawak_id,
                party_name=bran_jawak.party.party_name,
                rice_mill_name=bran_jawak.addricemill.rice_mill_name,
                broker_name=bran_jawak.brokers.broker_name,
                truck_number=bran_jawak.trucks.truck_number,
            )
        )

    return result


# ________________________________________________________


# Bhushi
@app.post("/bhushi/", status_code=status.HTTP_201_CREATED)
async def add_bhushi(bhushi: BhushiBase, db: db_dependency):
    db_add_bhushi = models.bhushi(**bhushi.dict())
    db.add(db_add_bhushi)
    db.commit()


# @app.get(
#     "/other-bhushi-data/",
#     response_model=List[BhushiBase],
#     status_code=status.HTTP_200_OK,
# )
# async def get_other_bhushi_data(db: db_dependency):
#     db_get_other_bhushi_data = db.query(models.bhushi).distinct().all()
#     return db_get_other_bhushi_data


@app.get(
    "/other-bhushi-data/",
    response_model=List[BhushiWithPartyRiceTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_bhushi_jawak_data(db: Session = Depends(get_db)):
    bhushiii = (
        db.query(models.bhushi)
        .options(
            joinedload(models.bhushi.addricemill),
            joinedload(models.bhushi.trucks),
            joinedload(models.bhushi.party),
        )
        .all()
    )

    result = []
    for bhushi in bhushiii:
        result.append(
            BhushiWithPartyRiceTruck(
                rst_number=bhushi.rst_number,
                date=bhushi.date,
                party_id=bhushi.party_id,
                rice_mill_name_id=bhushi.rice_mill_name_id,
                number_of_bags=bhushi.number_of_bags,
                weight=bhushi.weight,
                truck_number_id=bhushi.truck_number_id,
                rate=bhushi.rate,
                amount=bhushi.amount,
                bhushi_id=bhushi.bhushi_id,
                party_name=bhushi.party.party_name,
                rice_mill_name=bhushi.addricemill.rice_mill_name,
                truck_number=bhushi.trucks.truck_number,
            )
        )

    return result


# ________________________________________________________


# paddy sale
@app.post("/paddy-sale/", status_code=status.HTTP_201_CREATED)
async def paddy_sale(paddysale: PaddySaleBase, db: db_dependency):
    db_paddy_sale = models.Paddy_sale(**paddysale.dict())
    db.add(db_paddy_sale)
    db.commit()


# @app.get(
#     "/paddy-sale-data/",
#     response_model=List[PaddySaleBase],
#     status_code=status.HTTP_200_OK,
# )
# async def paddy_sale_data(db: db_dependency):
#     db_paddy_sale_data = db.query(models.Paddy_sale).distinct().all()
#     return db_paddy_sale_data


@app.get(
    "/paddy-sale-data/",
    response_model=List[PaddySalesWithDhanawakPartyBrokerTruck],
    status_code=status.HTTP_200_OK,
)
async def get_all_paddy_sale_data(db: Session = Depends(get_db)):
    paddy_sales = (
        db.query(models.Paddy_sale)
        .options(
            joinedload(models.Paddy_sale.dhanawak),
            joinedload(models.Paddy_sale.brokers),
            joinedload(models.Paddy_sale.trucks),
            joinedload(models.Paddy_sale.party),
            joinedload(models.Paddy_sale.addricemill),
        )
        .all()
    )

    result = []
    for paddy_sale in paddy_sales:
        result.append(
            PaddySalesWithDhanawakPartyBrokerTruck(
                rst_number_id=paddy_sale.rst_number_id,
                rice_mill_name_id=paddy_sale.rice_mill_name_id,
                date=paddy_sale.date,
                party_id=paddy_sale.party_id,
                broker=paddy_sale.broker,
                loading_form_address=paddy_sale.loading_form_address,
                truck_number_id=paddy_sale.truck_number_id,
                paddy_name=paddy_sale.paddy_name,
                weight=paddy_sale.weight,
                party_weight=paddy_sale.party_weight,
                bags=paddy_sale.bags,
                rate=paddy_sale.rate,
                ammount=paddy_sale.ammount,
                plastic=paddy_sale.plastic,
                joot_old=paddy_sale.joot_old,
                joot_23_24=paddy_sale.joot_23_24,
                joot_22_23=paddy_sale.joot_22_23,
                average_bag_wt=paddy_sale.average_bag_wt,
                paddy_sale_id=paddy_sale.paddy_sale_id,
                rst_number=paddy_sale.dhanawak.rst_number,
                party_name=paddy_sale.party.party_name,
                broker_name=paddy_sale.brokers.broker_name,
                truck_number=paddy_sale.trucks.truck_number,
                rice_mill_name=paddy_sale.addricemill.rice_mill_name,
            )
        )

    return result


# ________________________________________________________


# # Society
# # @app.get(
# #     "/society-data/{society_id}",
# #     response_model=SocietyDistanceRate,
# #     status_code=status.HTTP_200_OK,
# # )
# # async def society_data(society_id: int, db: db_dependency):
# #     society_data = db.query(models.Society).filter_by(society_id=society_id).all()
# #     society_db = {
# #         "society_data": [SocietyBase(**row.__dict__) for row in society_data],
# #     }
# #     return society_db


# @app.get(
#     "/society-data/{society_id}",
#     response_model=SocietyDistanceRate,
#     status_code=status.HTTP_200_OK,
# )
# async def society_data(society_id: int, db: db_dependency):
#     society_data = db.query(models.Society).filter_by(society_id=society_id).first()

#     if society_data is None:
#         raise HTTPException(status_code=404, detail="Society not found")

#     response_data = {"transporting_rate": society_data.transporting_rate}
#     return response_data


#     # Dhan rice societies rate
#     # @app.post("/dhan-rice-societies-rate/", status_code=status.HTTP_201_CREATED)
#     # async def dhan_rice_societies_rate(
#     #     dhansocietiesrate: DhanRiceSocietiesRateBase, db: db_dependency
#     # ):
#     #     db_dhan_rice_societies_rate = models.Dhan_rice_societies_rate(
#     #         **dhansocietiesrate.dict()
#     #     )
#     #     db.add(db_dhan_rice_societies_rate)
#     #     db.commit()

#     # @app.get(
#     #     "/dhan-rice-societies-rate-data/",
#     #     response_model=List[DhanRiceSocietiesRateBase],
#     #     status_code=status.HTTP_200_OK,
#     # )
#     # async def dhan_rice_societies_rate_data(db: db_dependency):
#     #     db_dhan_rice_societies_rate = (
#     #         db.query(models.Dhan_rice_societies_rate).distinct().all()
#     #     )
#     return db_dhan_rice_societies_rate


# # lot number master
# @app.post("/lot-number-master/", status_code=status.HTTP_201_CREATED)
# async def lot_number_master(lotnumbermaster: LotNumberMasterBase, db: db_dependency):
#     db_lot_number_master = models.Lot_number_master(**lotnumbermaster.dict())
#     db.add(db_lot_number_master)
#     db.commit()


# @app.get(
#     "/lot-number-master-data/",
#     response_model=List[LotNumberMasterBase],
#     status_code=status.HTTP_200_OK,
# )
# async def lot_number_master_data(db: db_dependency):
#     db_lot_number_master = db.query(models.Lot_number_master).distinct().all()
#     return db_lot_number_master


# # Mohan food paddy
# @app.post("/mohan-food-paddy/", status_code=status.HTTP_201_CREATED)
# async def mohan_food_paddy(mohanfoodpaddy: MohanFoodPaddyBase, db: db_dependency):
#     db_mohan_food_paddy = models.Mohan_food_paddy(**mohanfoodpaddy.dict())
#     db.add(db_mohan_food_paddy)
#     db.commit()


# @app.get(
#     "/mohan-food-paddy-data/",
#     response_model=List[MohanFoodPaddyBase],
#     status_code=status.HTTP_200_OK,
# )
# async def mohan_food_paddy_data(db: db_dependency):
#     db_mohan_food_paddy_data = db.query(models.Mohan_food_paddy).distinct().all()
#     return db_mohan_food_paddy_data


# # Transporter master
# @app.post("/transporter-master/", status_code=status.HTTP_201_CREATED)
# async def transporter_master(
#     transportermaster: TransporterMasterBase, db: db_dependency
# ):
#     db_transporter_master = models.Transporter_master(**transportermaster.dict())
#     db.add(db_transporter_master)
#     db.commit()


# @app.get(
#     "/transporter-master-data/",
#     response_model=List[TransporterMasterBase],
#     status_code=status.HTTP_200_OK,
# )
# async def transporter_master_data(db: db_dependency):
#     db_transporter_master_data = db.query(models.Transporter_master).distinct().all()
#     return db_transporter_master_data


# # About Rice Mill
# # @app.post("/add-rice-mill/", status_code=status.HTTP_201_CREATED)
# # async def add_rice_mill(addricemill: AddRiceMillBase, db: db_dependency):
# #     db_about_rice_mill = models.Add_Rice_Mill(**addricemill.dict())
# #     db.add(db_about_rice_mill)
# #     db.commit()


# # Add New Transporters
# # @app.post("/transporter/", status_code=status.HTTP_201_CREATED)
# # async def add_new_trasporter(transporters: TransporterBase, db: db_dependency):
# #     db_transporter = models.Transporter(**transporters.dict())
# #     db.add(db_transporter)
# #     db.commit()


# # Add New Society
# # @app.post("/society/", status_code=status.HTTP_201_CREATED)
# # async def add_new_society(society: SocietyBase, db: db_dependency):
# #     db_society = models.Society(**society.dict())
# #     db.add(db_society)
# #     db.commit()


# # Add New Agreement
# # @app.post("/agreement/", status_code=status.HTTP_201_CREATED)
# # async def add_agreement(agreement: AgreementBase, db: db_dependency):
# #     db_agreement = models.Agreement(**agreement.dict())
# #     db.add(db_agreement)
# #     db.commit()


# class DhanAwakDalaliDhan(BaseModel):
#     total_weight: List[int]
#     dm_weight: List[int]
#     weight: List[int]
#     miller_purana: List[int]


# @app.get(
#     "/rice-rst-number-do-number/{rice_mill_id}",
#     response_model=RiceMillRstNumber,
#     status_code=status.HTTP_200_OK,
# )
# async def rice_mill_rst_number(rice_mill_id: int, db: db_dependency):
#     rice_mill_data = (
#         db.query(models.Add_Rice_Mill).filter_by(rice_mill_id=rice_mill_id).all()
#     )
#     rst_data = db.query(models.Dhan_Awak).filter_by(rice_mill_id=rice_mill_id).all()
#     do_number_data = (
#         db.query(models.Add_Do).filter_by(select_mill_id=rice_mill_id).all()
#     )
#     rice_mill_rst_number = {
#         "rice_mill_data": [AddRiceMillBase(**row.__dict__) for row in rice_mill_data],
#         "do_number_data": [AdddoBase(**row.__dict__) for row in do_number_data],
#         "rst_data": [DhanAwakBase(**row.__dict__) for row in rst_data],
#     }
#     return rice_mill_rst_number


# @app.get(
#     "/paddy-data/{rice_mill_id}",
#     response_model=DhanAwakDalaliDhan,
#     status_code=status.HTTP_200_OK,
# )
# async def get_data(rice_mill_id: int, db: db_dependency):
#     # Fetch data from different tables
#     total_weight = (
#         db.query(models.Dalali_dhaan).filter_by(rice_mill_id=rice_mill_id).all()
#     )
#     dm_weight = db.query(models.Dhan_Awak).filter_by(rice_mill_id=rice_mill_id).all()
#     weight = db.query(models.Paddy_sale).filter_by(rice_mill_id=rice_mill_id).all()
#     miller_purana = (
#         db.query(models.Dhan_Awak).filter_by(rice_mill_id=rice_mill_id).all()
#     )

#     # Return the result as a custom response model
#     response_data = {
#         "total_weight": [row.total_weight for row in total_weight],
#         "dm_weight": [row.dm_weight for row in dm_weight],
#         "weight": [row.weight for row in weight],
#         "miller_purana": [row.miller_purana for row in miller_purana],
#     }

#     return response_data


@app.get(
    "/paddy-data/{rice_mill_id}",
    response_model=DhanAwakDalaliDhan,
    status_code=status.HTTP_200_OK,
)
async def get_data(rice_mill_id: int, db: db_dependency):
    # Fetch data from different tables
    total_weight = db.query(models.Dalali_dhaan).all()
    dm_weight = db.query(models.Dhan_Awak).filter_by(rice_mill_id=rice_mill_id).all()
    weight = db.query(models.Paddy_sale).filter_by(rice_mill_name_id=rice_mill_id).all()
    miller_purana = (
        db.query(models.Dhan_Awak).filter_by(rice_mill_id=rice_mill_id).all()
    )
    Paddy_deposite_data = (
        db.query(models.Rice_deposite).filter_by(rice_mill_name_id=rice_mill_id).all()
    )

    # Return the result as a custom response model
    response_data = {
        "total_weight": [row.total_weight for row in total_weight],
        "Dhan_data": [DhanAwakBase(**row.__dict__) for row in dm_weight],
        "Paddy_sale_data": [PaddySaleBase(**row.__dict__) for row in weight],
        "miller_purana": [DhanAwakBase(**row.__dict__) for row in miller_purana],
        "Paddy_deposite_data": [
            RiceDepositeBase(**row.__dict__) for row in Paddy_deposite_data
        ],
    }

    return DhanAwakDalaliDhan(**response_data)
