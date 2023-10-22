from sqlalchemy import Boolean, Column, Integer, String, Double, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)
    isAdmin = Column(Boolean)
    balance = Column(Double)
    # rents_users = relationship("Rent", back_populates="rent_user")


class Transport(Base):
    __tablename__ = "transports"

    id = Column(Integer, primary_key=True)
    users_id = Column(Integer, ForeignKey('users.id'))
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
    # rents_transports = relationship("Rent", back_populates="rent_transport")


class Rent(Base):
    __tablename__ = "rent"

    id = Column(Integer, primary_key=True)
    rent_user_id = Column(Integer, ForeignKey('users.id'))
    rent_transports_id = Column(Integer, ForeignKey('transports.id'))
    color = Column(String)
    timeStart = Column(String)
    timeEnd = Column(String, nullable=True)
    priceOfUnit = Column(Double)
    priceType = Column(String)
    finalPrice = Column(String, nullable=True)
