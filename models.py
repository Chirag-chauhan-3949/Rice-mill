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
    transporting_rate = Column(Integer)
    created_at = Column(DateTime, default=func.now())


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


class Dhan_rice_societies_rate(Base):
    __tablename__ = "dhanricesocietiesrate"

    dhan_rice_societies_rate_id = Column(Integer, primary_key=True, index=True)
    society_name_id = Column(Integer, ForeignKey("society.society_id"))
    distance = Column(Float)
    new = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Frk(Base):
    __tablename__ = "frk"

    frk_id = Column(Integer, primary_key=True, index=True)
    date = Column(DATE)
    party = Column(String(50))
    bags = Column(Integer)
    weight = Column(VARCHAR(50))
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    rice_mill_name_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    bill_number = Column(Integer)
    rate = Column(Float)
    created_at = Column(DateTime, default=func.now())


class Sauda_patrak(Base):
    __tablename__ = "saudapatrak"

    sauda_patrak_id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50))
    address = Column(String(150))
    vechicle_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    paddy = Column(String(50))
    bags = Column(Integer)
    weight = Column(VARCHAR(50))
    rate = Column(Integer)
    amount = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Add_Do(Base):
    __tablename__ = "addDo"

    do_id = Column(Integer, primary_key=True, index=True)
    select_mill_id = Column(Integer, ForeignKey("addricemill.rice_mill_id"))
    date = Column(DATE)
    do_number = Column(BigInteger)
    select_argeement_id = Column(Integer, ForeignKey("agreement.agremennt_id"))
    moto_weight = Column(VARCHAR(50))
    mota_Bardana = Column(Integer)
    patla_weight = Column(VARCHAR(50))
    patla_bardana = Column(Integer)
    sarna_weight = Column(VARCHAR(50))
    sarna_bardana = Column(Integer)
    total_weight = Column(Integer)
    total_bardana = Column(Integer)
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
    society_hidden_name = Column(Integer)
    dm_weight = Column(VARCHAR(50))
    number_of_bags = Column(Integer)
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    transporter_name_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    transporting_rate = Column(Integer)
    # transporting_rate_society_id = Column(Integer, ForeignKey("society.society_id"))
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
    total_bag_weight = Column(VARCHAR(50))
    type_of_paddy = Column(String(50))
    actual_paddy = Column(String(50))
    mill_weight_quintals = Column(VARCHAR(50))
    shortage = Column(Integer)
    bags_put_in_hopper = Column(Integer)
    total_hopper_weight = Column(VARCHAR(50))
    created_at = Column(DateTime, default=func.now())


class Do_panding(Base):
    __tablename__ = "dopanding"

    do_panding_id = Column(Integer, primary_key=True, index=True)
    do_number_id = Column(Integer, ForeignKey("addDo.do_id"))
    date = Column(DATE)
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
    weight = Column(VARCHAR(50))
    party_weight = Column(VARCHAR(50))
    rate = Column(Integer)
    ammount = Column(Integer)
    plastic = Column(Integer)
    joot_old = Column(Integer)
    joot_23_24 = Column(Integer)
    joot_22_23 = Column(Integer)
    average_bag_wt = Column(Float)
    created_at = Column(DateTime, default=func.now())


class Dalali_dhaan(Base):
    __tablename__ = "dalalidhaan"

    dalali_dhaan_id = Column(Integer, primary_key=True, index=True)
    rst_number_id = Column(Integer, ForeignKey("dhanawak.dhan_awak_id"))
    date = Column(DATE)
    kocia = Column(String(50))
    vehicale_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    white_sarna_bags = Column(Integer)
    white_sarna_weight = Column(VARCHAR(50))
    ir_bags = Column(Integer)
    ir_weight = Column(VARCHAR(50))
    rb_gold_bags = Column(Integer)
    rb_gold_weight = Column(VARCHAR(50))
    sarna_bags = Column(Integer)
    sarna_weight = Column(VARCHAR(50))
    sambha_new_bag = Column(Integer)
    sambha_new_weight = Column(VARCHAR(50))
    paddy_type = Column(String(50))
    total_bags = Column(Integer)
    total_weight = Column(VARCHAR(50))
    hamali = Column(Integer)
    weight_less_plastic = Column(VARCHAR(50))
    weight_less_jute = Column(VARCHAR(50))
    weight_less_kata_difference = Column(VARCHAR(50))
    net_weight = Column(VARCHAR(50))
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
