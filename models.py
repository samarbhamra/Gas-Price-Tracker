from sqlalchemy import Column, Integer, Float, String, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class GasPrice(Base):
    __tablename__ = 'gas_prices'
    id = Column(Integer, primary_key=True)
    city = Column(String)
    province = Column(String)
    date = Column(Date)
    price = Column(Float)
