from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import crud
import database
import schemas

router = APIRouter()


@router.post("/", response_model=schemas.UserReport)
def create_user_report(user_report: schemas.UserReportCreate, db: Session = Depends(database.get_db)):
    return crud.create_user_report(db=db, user_report=user_report)


@router.get("/{id}", response_model=schemas.UserReport)
def read_user_report(id: int, db: Session = Depends(database.get_db)):
    db_user_report = crud.get_user_report(db=db, user_report_id=id)
    if db_user_report is None:
        raise HTTPException(status_code=404, detail="User report not found")
    return db_user_report
