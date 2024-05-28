from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter()

@router.post("/", response_model=schemas.Reporter)
def create_reporter(reporter: schemas.ReporterCreate, db: Session = Depends(database.get_db)):
    try:
        return crud.create_reporter(db=db, reporter=reporter)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/", response_model=list[schemas.Reporter])
def read_reporters(db: Session = Depends(database.get_db)):
    return crud.get_reporters(db=db)
