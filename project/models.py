from enum import unique
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


class Customer(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True)
    name = Column(String, unique=False)
    surname = Column(String, unique=False)
    age = Column(Integer, index=True)
    height = Column(Integer, index=True)
    addresses = Column(String, unique=True, index=True)
    idNumber = Column(Integer, unique=True, index=True)
    passportNumber = Column(Integer, index=True)
    nationality = Column(String, unique=False)
    dateCreated = Column(DateTime(timezone=True), server_default=func.now())
    lastUpdate = Column(DateTime(timezone=True), onupdate=func.now())
    active = Column(Boolean, default=True)
    expiryDate = Column(DateTime(timezone=True), server_default=func.now())
