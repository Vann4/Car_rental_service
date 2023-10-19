from sqlalchemy import Boolean, Column, Integer, String, Double
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "Users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    isAdmin = Column(Boolean)
    balance = Column(Double)
    rents_user = relationship("Rent", back_populates="owner_user")


class Transport(Base):
    __tablename__ = "transports"

    id = Column(Integer, primary_key=True)
    ownerId = Column(Integer, unsigned=True)
    canBeRented = Column(Boolean)
    transportType = Column(String)
    model = Column(String)
    color = Column(String)
    identifier = Column(String, unique=True)
    description = Column(String, nullable=True)
    latitude = Column(Double)
    longitude = Column(Double)
    minutePrice = Column(Double, nullable=True)
    dayPrice = Column(Double, nullable=True)
    radius = Column(Double)
    rents_transport = relationship("Rent", back_populates="owner_transport")


class Rent(Base):
    __tablename__ = "rent"

    id = Column(Integer, primary_key=True)
    owner_transport = relationship("Transport", back_populates="rents_transport")
    owner_user = relationship("User", back_populates="rents_user")
    color = Column(String)
    timeStart = Column(String)
    timeEnd = Column(String, nullable=True)
    priceOfUnit = Column(Double)
    priceType = Column(String)
    finalPrice = Column(String, nullable=True)
