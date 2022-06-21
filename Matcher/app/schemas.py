from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from database import Base

class Animal(Base):
  __tablename__ = 'animal'
  size = Column(Integer, primary_key = True)
  body = Column(Integer)
  chest = Column(Integer)
  neck = Column(Integer)
  breed = Column(Integer)
  signDate = Column(DateTime)
  statusInd = Column(Boolean, default = True)

class Sociopath(Base):
  __tablename__ = 'sociopath'
  rfc =	Column(String(100),primary_key = True)
  street = Column(String(100))
  number = Column(Integer)
  secction = Column(String(100))
  district = Column(String(100))
  village = Column(String(100))
  country = Column(String(100))
  code = Column(Integer)
  signDate = Column(DateTime)
  #statusInd = Column(Boolean. default = True) 

class Adopter(Base):
  __tablename__ = 'adopter'
  rfc =	Column(String(100), primary_key = True)
  street = Column(String(100))
  number = Column(Integer)
  secction = Column(String(100))
  district = Column(String(100))
  village = Column(String(100))
  country = Column(String(100))
  code = Column(Integer)
  signDate = Column(DateTime)
  #statusInd = Column(Boolean, default = True)

class Partnership(Base):
  __tablename__ = 'partnership'
  rfc =	Column(String(100), primary_key = True)
  street = Column(String(100))
  number = Column(Integer)
  secction = Column(String(100))
  district = Column(String(100))
  village = Column(String(100))
  country = Column(String(100))
  code = Column(Integer)
  signDate = Column(DateTime)
  #statusInd = Column(Boolean, primary_key = True)
