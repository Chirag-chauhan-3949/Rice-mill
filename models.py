from sqlalchemy import (
    Column,
    Integer,
    String,
    DateTime,
    func,
    VARCHAR,
    ForeignKey,
    Float,
)
from database import Base
from sqlalchemy.orm import relationship


class About_Rice_Mill(Base):
    __tablename__ = "aboutricemill"

    about_rice_mill_id = Column(Integer, primary_key=True, index=True)
    rice_mill_name = Column(String(50), index=True)
    gst_number = Column(Integer, index=True)
    mill_address = Column(String(150))
    phone_number = Column(Integer)
    rice_mill_capacity = Column(Float)
    created_at = Column(DateTime, default=func.now())


class Transporter(Base):
    __tablename__ = "transporter"

    transporter_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    transporter_name = Column(String(50))
    transporter_phone_number = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Truck(Base):
    __tablename__ = "trucks"

    truck_id = Column(Integer, primary_key=True, index=True)
    truck_number = Column(Integer)
    transporter_name = Column(String(50))
    truck_transport_id = Column(Integer, ForeignKey("transporter.transporter_id"))
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
    mill = Column(VARCHAR(255))
    agreement_number = Column(Integer)
    mota = Column(Integer)
    patla = Column(Integer)
    sarna = Column(Integer)
    lot_from = Column(Integer)
    lot_to = Column(Integer)
    total = Column(Integer)
    created_at = Column(DateTime, default=func.now())


class Add_Do(Base):
    __tablename__ = "addDo"

    do_id = Column(Integer, primary_key=True, index=True)
    select_mill = Column(String(50))
    date = Column(String(50))
    do_number = Column(Integer)
    select_agreement = Column(String(50))
    select_argeement_id = Column(Integer, ForeignKey("agreement.agremennt_id"))
    moto_weight = Column(VARCHAR(50))
    mota_Bardana = Column(Integer)
    patla_weight = Column(VARCHAR(50))
    patla_bardana = Column(Integer)
    sarna_weight = Column(VARCHAR(50))
    sarna_bardana = Column(Integer)
    total_weight = Column(Integer)
    total_bardana = Column(Integer)
    society = Column(String(50))
    society_id = Column(Integer, ForeignKey("society.society_id"))
    truck_number = Column(Integer)
    truck_number_id = Column(Integer, ForeignKey("trucks.truck_id"))
    created_at = Column(DateTime, default=func.now())


class Dhan_Awak(Base):
    __tablename__ = "dhanawak"

    dhan_awak_id = Column(Integer, primary_key=True, index=True)
    rst_number = Column(Integer, index=True)
    select_mill = Column(String(50), index=True)
    rice_mill_id = Column(Integer, ForeignKey("aboutricemill.about_rice_mill_id"))
    date = Column(Integer)
    do_number = Column(Integer)
    do_id = Column(Integer, ForeignKey("addDo.do_id"))
    society = Column(String(50))
    society_id = Column(Integer, ForeignKey("society.society_id"))
    society_hidden_name = Column(Integer)
    dm_weight = Column(VARCHAR(50))
    number_of_bags = Column(Integer)
    truck_number = Column(Integer)
    truck_id = Column(Integer, ForeignKey("trucks.truck_id"))
    transporter = Column(String(50))
    transporter_id = Column(Integer, ForeignKey("transporter.transporter_id"))
    transporting_rate = Column(Integer)
    transporting_rate_society_id = Column(Integer, ForeignKey("society.society_id"))
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
