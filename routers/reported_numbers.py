from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.ReportedNumber)
def create_reported_number(reported_number: schemas.ReportedNumberCreate, db: Session = Depends(database.get_db)):
    return crud.create_reported_number(db=db, reported_number=reported_number)


@router.get("/{id}", response_model=schemas.ReportedNumber)
def read_reported_number(id: int, db: Session = Depends(database.get_db)):
    db_reported_number = crud.get_reported_number(db=db, reported_number_id=id)
    if db_reported_number is None:
        raise HTTPException(status_code=404, detail="Reported number not found")
    return db_reported_number
