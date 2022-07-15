from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/customers/", response_model=schemas.Customer)
def create_customers(customer: schemas.Customer, db: Session = Depends(get_db)):
    """Create a customer"""
    db_customer = crud.get_customer(db, customer_id=customer.id)

    if db_customer:
        raise HTTPException(status_code=400, detail="Customer already registered.")

    return crud.create_customer(db=db, customer=customer)


@app.get("/customers/", response_model=List[schemas.Customer])
def read_customers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    """Get all customers"""
    customers = crud.get_customers(db, skip=skip, limit=limit)
    return customers


@app.get("/customers/{customer_id}", response_model=schemas.Customer)
def read_customer(customer_id: str, db: Session = Depends(get_db)):
    """Get customer by id"""
    db_customer = crud.get_customer(db, customer_id=customer_id)

    if not db_customer:
        raise HTTPException(status_code=404, detail="customer not found.")
    return db_customer
