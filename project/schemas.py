from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Customer(BaseModel):
    name: str
    surname: str
    age: int
    height: int
    addresses: str
    id: int
    idNumber: int
    passportNumber: int
    nationality: str
    dateCreated: datetime
    lastUpdate: datetime
    active: bool
    expiryDate: datetime

    class Config:
        orm_mode = True
