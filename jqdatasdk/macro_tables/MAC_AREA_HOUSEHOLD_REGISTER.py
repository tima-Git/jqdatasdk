# coding: utf-8
import datetime
from sqlalchemy import BigInteger, Column, DateTime, Integer, Numeric, SmallInteger, String, Table, Text, text
from sqlalchemy.dialects.mysql import TINYINT, TIMESTAMP, DECIMAL
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MAC_AREA_HOUSEHOLD_REGISTER(Base):
    """
    各地区户数、人口数、性别比和户规模表
    """
    __tablename__ = "MAC_AREA_HOUSEHOLD_REGISTER"

    id = Column(Integer, primary_key=True)
    stat_year = Column(String(4), nullable=False)
    area_code = Column(String(20), nullable=False)
    area_name = Column(String(100), nullable=False)
    population = Column(DECIMAL(20, 4))
    male = Column(DECIMAL(20, 4))
    female = Column(DECIMAL(20, 4))
    residing = Column(DECIMAL(20, 4))
    male_residing = Column(DECIMAL(20, 4))
    female_residing = Column(DECIMAL(20, 4))
    residing_6months = Column(DECIMAL(20, 4))
    male_residing_6months = Column(DECIMAL(20, 4))
    female_residing_6months = Column(DECIMAL(20, 4))
    household_unsettle = Column(DECIMAL(20, 4))
    male_household_unsettle = Column(DECIMAL(20, 4))
    female_household_unsettle = Column(DECIMAL(20, 4))
    residing_abroad = Column(DECIMAL(20, 4))
    male_residing_abroad = Column(DECIMAL(20, 4))
    female_residing_abroad = Column(DECIMAL(20, 4))
    status = Column(TINYINT(display_width=4), default=0)
    addtime = Column(TIMESTAMP, default=datetime.datetime.now)
    modtime = Column(TIMESTAMP)