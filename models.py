from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    VARCHAR,
    ForeignKey,
    Float,
    BigInteger,
    DATE,
)
from database import Base


class Add_Rice_Mill(Base):
    __tablename__ = "addricemill"

    rice_mill_id = Column(Integer, primary_key=True, index=True)
    rice_mill_name = Column(String(50), index=True)
    gst_number = Column(VARCHAR(50))
    mill_address = Column(String(200))
    phone_number = Column(BigInteger)
    rice_mill_capacity = Column(Float)
    created_at = Column(DateTime, default=func.now())


class Transporter(Base):
    __tablename__ = "transporter"

    transporter_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    # rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    transporter_name = Column(String(50))
    transporter_phone_number = Column(BigInteger)
    created_at = Column(DateTime, default=func.now())


class Truck(Base):
    __tablename__ = "trucks"

    truck_id = Column(Integer, primary_key=True, index=True)
    truck_number = Column(VARCHAR(50))
    transport_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    created_at = Column(DateTime, default=func.now())


class Society(Base):
    __tablename__ = "society"

    society_id = Column(Integer, primary_key=True, index=True)
    society_name = Column(String(50))
    distance_from_mill = Column(Integer)
    google_distance = Column(Integer)
    transporting_rate = Column(Integer)
    actual_distance = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Society_Name(Base):
    __tablename__ = "societyName"

    society_id = Column(Integer, primary_key=True, index=True)
    society_name = Column(String(50))


class Agreement(Base):
    __tablename__ = "agreement"

    agremennt_id = Column(Integer, primary_key=True, index=True)
    rice_mill_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    agreement_number = Column(VARCHAR(15))
    mota = Column(Integer)
    patla = Column(Integer)
    sarna = Column(Integer)
    lot_from = Column(Integer)
    lot_to = Column(Integer)
    total = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Lot_number_master(Base):
    __tablename__ = "lotnumbermaster"

    lot_number_master_id = Column(Integer, primary_key=True, index=True)
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    lot_number = Column(Integer)
    created_at = Column(DateTime, default=func.now())


# class Dhan_rice_societies_rate(Base):
#     __tablename__ = "dhanricesocietiesrate"

#     dhan_rice_societies_rate_id = Column(Integer, primary_key=True, index=True)
#     society_name_id = Column(Integer, ForeignKey("society.society_id"))
#     distance = Column(Float)
#     new = Column(Integer)
#     created_at = Column(DateTime, default=func.now())


class Frk(Base):
    __tablename__ = "frk"

    frk_id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE)
    party = Column(String(50))
    bags = Column(Integer)
    weight = Column(Integer)
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    bill_number = Column(Integer)
    rate = Column(Float)
    batch_number = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Sauda_patrak(Base):
    __tablename__ = "saudapatrak"

    sauda_patrak_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    address = Column(String(150))
    vechicle_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    paddy = Column(String(50))
    bags = Column(Integer)
    weight = Column(Integer)
    rate = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Add_Do(Base):
    __tablename__ = "addDo"

    do_id = Column(Integer, primary_key=True, index=True)
    select_mill_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    date = Column(DATE)
    do_number = Column(String(15))
    select_argeement_id = Column(Integer, ForeignKey("agreement.agremennt_id"))
    moto_weight = Column(Float)
    mota_Bardana = Column(Float)
    patla_weight = Column(Float)
    patla_bardana = Column(Float)
    sarna_weight = Column(Float)
    sarna_bardana = Column(Float)
    total_weight = Column(Float)
    total_bardana = Column(Float)
    society_name_id = Column(Integer, ForeignKey("society.society_id"))
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    created_at = Column(DateTime, default=func.now())


class Dhan_Awak(Base):
    __tablename__ = "dhanawak"

    dhan_awak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    rice_mill_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    date = Column(DATE)
    do_id = Column(Integer, ForeignKey("addDo.do_id"))
    society_id = Column(Integer, ForeignKey("society.society_id"))
    dm_weight = Column(Integer)
    number_of_bags = Column(Integer)
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
    created_at = Column(DateTime, default=func.now())


class Do_panding(Base):
    __tablename__ = "dopanding"

    do_panding_id = Column(Integer, primary_key=True, index=True)
    rice_mill_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    do_number_id = Column(Integer, ForeignKey("addDo.do_id"))
    date = Column(DATE)  # Jis Din Jari hua Hai Us Din ka Date Ho Ga
    mota = Column(VARCHAR(50))
    patla = Column(VARCHAR(50))
    sarna = Column(VARCHAR(50))
    Total = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Paddy_sale(Base):
    __tablename__ = "paddysale"

    paddy_sale_id = Column(Integer, primary_key=True, index=True)
    rst_number_id = Column(Integer, ForeignKey("dhanawak.dhan_awak_id"))
    date = Column(DATE)
    party = Column(String(50))
    broker = Column(String(50))
    loading_form_address = Column(String(50))
    vehicle_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    paddy_name = Column(String(50))
    weight = Column(Integer)
    party_weight = Column(Integer)
    rate = Column(Integer)
    ammount = Column(Integer)
    plastic = Column(Integer)
    joot_old = Column(Integer)
    joot_23_24 = Column(Integer)
    joot_22_23 = Column(Integer)
    average_bag_wt = Column(Float)
    created_at = Column(DateTime, default=func.now())


class Kochia(Base):
    __tablename__ = "kochia"

    kochia_id = Column(Integer, primary_key=True, index=True)
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    kochia_name = Column(String(50))
    kochia_phone_number = Column(Integer)


class Dalali_dhaan(Base):
    __tablename__ = "dalalidhaan"

    dalali_dhaan_id = Column(Integer, primary_key=True, index=True)
    # rst_number_id = Column(Integer, ForeignKey("dhanawak.dhan_awak_id"))
    rst_number = Column(Integer)
    date = Column(DATE)
    kochia_id = Column(Integer, ForeignKey("kochia.kochia_id"))
    vehicale_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    white_sarna_bags = Column(Integer)
    white_sarna_weight = Column(Integer)
    ir_bags = Column(Integer)
    ir_weight = Column(Integer)
    rb_gold_bags = Column(Integer)
    rb_gold_weight = Column(Integer)
    sarna_bags = Column(Integer)
    sarna_weight = Column(Integer)
    sambha_new_bag = Column(Integer)
    sambha_new_weight = Column(Integer)
    paddy_type = Column(String(50))
    total_bags = Column(Integer)
    total_weight = Column(Integer)
    hamali = Column(Integer)
    weight_less_plastic = Column(Integer)
    weight_less_jute = Column(Integer)
    weight_less_kata_difference = Column(Integer)
    net_weight = Column(Integer)
    rate = Column(Integer)
    ammount = Column(Float)
    created_at = Column(DateTime, default=func.now())


class Mohan_food_paddy(Base):
    __tablename__ = "mohanfoodpaddy"

    mohan_food_paddy_id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE)
    do_number_id = Column(Integer, ForeignKey("addDo.do_id"))
    samiti = Column(String(50))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    weight = Column(Integer)
    vehicle_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    bags = Column(Integer)
    transporting_total = Column(Integer)
    transporter_name_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    transporter_type = Column(String(50))
    transporter_status = Column(String(50))
    rate = Column(Integer)
    type_1 = Column(String(50))
    years_22_23 = Column(Integer)
    years_21_22 = Column(Integer)
    hdpe_one = Column(Integer)
    hdpe_new = Column(Integer)
    purana = Column(Integer)
    pds = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Dhan_transporting(Base):
    __tablename__ = "dhantransporting"

    Dhan_transporting_id = Column(Integer, primary_key=True, index=True)
    rst_number_id = Column(Integer, ForeignKey("dhanawak.dhan_awak_id"))
    date = Column(DATE)
    do_number_id = Column(Integer, ForeignKey("addDo.do_id"))
    society_name_id = Column(Integer, ForeignKey("society.society_id"))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    dm_weight = Column(Integer)
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    numbers_of_bags = Column(Integer)
    transporting_total = Column(Integer)
    transporter_name_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    status = Column(String(50))
    total_pending = Column(Integer)
    total_paid = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Transporter_master(Base):
    __tablename__ = "transportermaster"

    transporter_master_id = Column(Integer, primary_key=True, index=True)
    vehicle_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    name = Column(String(50))
    phone_number = Column(BigInteger)
    date = Column(DATE)
    transporter_name_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    advance_payment = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Rice_deposite(Base):
    __tablename__ = "ricedeposite"

    rice_depostie_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    lot_number = Column(Integer)
    ware_house_id = Column(Integer)
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    weight = Column(Integer)
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    bags = Column(Integer)
    transporting_total = Column(Integer)
    transporter_name_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    transporting_type = Column(String(50))
    transporting_status = Column(String(50))
    rate = Column(Integer)
    hamali = Column(Integer)
    variety = Column(String(50))
    halting = Column(Integer)
    variety_weight = Column(Integer)
    data_2022_23 = Column(Integer)
    data_2021_22 = Column(Integer)
    pds = Column(Integer)
    old = Column(Integer)
    amount = Column(Integer)
    status = Column(String(50))
    created_at = Column(DateTime, default=func.now())


class ware_house_transporting(Base):
    __tablename__ = "warehousetransporting"

    ware_houes_id = Column(Integer, primary_key=True, index=True)
    ware_houes_name = Column(String(50))
    ware_house_transporting_rate = Column(Integer)
    hamalirate = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class party(Base):
    __tablename__ = "party"

    party_id = Column(Integer, primary_key=True, index=True)
    party_name = Column(String(50))


class brokers(Base):
    __tablename__ = "brokers"

    broker_id = Column(Integer, primary_key=True, index=True)
    broker_name = Column(String(50))


class broken_jawak(Base):
    __tablename__ = "brokenjawak"

    broken_jawak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    broker = Column(String(50))
    brokerage_percentage = Column(Float)
    weight = Column(Float)
    rate = Column(Integer)
    number_of_bags = Column(Integer)
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    total = Column(Integer)
    brokerage = Column(Float)
    net_recievable = Column(Float)
    loading_date = Column(DATE)
    recieved_date = Column(DATE)
    payment_recieved = Column(Integer)
    number_of_days = Column(Integer)
    payment_difference = Column(Integer)
    remarks = Column(String(100))
    created_at = Column(DateTime, default=func.now())


class nakkhi_jawak(Base):
    __tablename__ = "nakkhijawak"

    nakkhi_jawak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    broker = Column(String(50))
    weight = Column(Float)
    rate = Column(Integer)
    number_of_bags = Column(Integer)
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    brokerage = Column(Float)
    total = Column(Integer)
    CD_1_percent = Column(Float)
    net_recievable = Column(Float)
    payment_recieved = Column(Integer)
    remarks = Column(String(100))
    created_at = Column(DateTime, default=func.now())


class bran_jawak(Base):
    __tablename__ = "branjawak"

    bran_jawak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    broker = Column(String(50))
    brokerage_percentage = Column(Float)
    weight = Column(Float)
    rate = Column(Integer)
    number_of_bags = Column(Integer)
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    total = Column(Integer)
    brokerage = Column(Float)
    net_recievable = Column(Float)
    payment_recieved = Column(Integer)
    difference = Column(Integer)
    remarks = Column(String(100))
    created_at = Column(DateTime, default=func.now())


class husk_jawak(Base):
    __tablename__ = "huskjawak"

    husk_jawak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    remarks = Column(String(100))
    broker = Column(String(50))
    brokerage_percentage = Column(Float)
    weight = Column(Float)
    rate = Column(Integer)
    number_of_bags = Column(Integer)
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    total = Column(Integer)
    brokerage = Column(Float)
    net_recievable = Column(Float)
    payment_recieved = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class bhushi(Base):
    __tablename__ = "bhushi"

    bhushi_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    number_of_bags = Column(Integer)
    weight = Column(Float)
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    rate = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class other_awak(Base):
    __tablename__ = "otherawak"

    other_awak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    material = Column(String(50))
    nos = Column(Integer)
    reason = Column(String(50))
    weight = Column(Float)
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    created_at = Column(DateTime, default=func.now())


class other_jawak(Base):
    __tablename__ = "other_jawak"

    other_jawak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer)
    date = Column(DATE)
    party = Column(String(50))
    truck_number = Column(Integer, ForeignKey("trucks.truck_id"))
    material = Column(String(50))
    nos = Column(Integer)
    reason = Column(String(50))
    weight = Column(Float)
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    created_at = Column(DateTime, default=func.now())
