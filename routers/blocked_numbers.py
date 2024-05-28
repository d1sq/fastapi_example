from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.BlockedNumber)
def create_blocked_number(blocked_number: schemas.BlockedNumberCreate, db: Session = Depends(database.get_db)):
    return crud.create_blocked_number(db=db, blocked_number=blocked_number)


@router.get("/{id}", response_model=schemas.BlockedNumber)
def read_blocked_number(id: int, db: Session = Depends(database.get_db)):
    db_blocked_number = crud.get_blocked_number(db=db, blocked_number_id=id)
    if db_blocked_number is None:
        raise HTTPException(status_code=404, detail="Blocked number not found")
    return db_blocked_number


@router.get("/", response_model=list[schemas.BlockedNumber])
def read_blocked_numbers(db: Session = Depends(database.get_db)):
    return crud.get_blocked_numbers(db=db)
