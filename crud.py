import datetime

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session
import models
import schemas


# ReportedNumbers CRUD
def create_reported_number(db: Session, reported_number: schemas.ReportedNumberCreate):
    db_reported_number = db.query(models.ReportedNumbers).filter(models.ReportedNumbers.phoneNumber == reported_number.phoneNumber).first()
    if db_reported_number:
        db_reported_number.reportCount += 1
        if db_reported_number.reportCount > 5:
            db_blocked_number = models.BlockedNumbers(phoneNumber=reported_number.phoneNumber, blockedDate=datetime.date.today())
            db.add(db_blocked_number)
        db.commit()
        db.refresh(db_reported_number)
        return db_reported_number
    else:
        new_reported_number = models.ReportedNumbers(phoneNumber=reported_number.phoneNumber, reportCount=1)
        db.add(new_reported_number)
        db.commit()
        db.refresh(new_reported_number)
        return new_reported_number


def get_reported_number(db: Session, reported_number_id: int):
    return db.query(models.ReportedNumbers).filter(models.ReportedNumbers.id == reported_number_id).first()


# BlockedNumbers CRUD
def create_blocked_number(db: Session, blocked_number: schemas.BlockedNumberCreate):
    db_blocked_number = models.BlockedNumbers(**blocked_number.dict())
    db.add(db_blocked_number)
    db.commit()
    db.refresh(db_blocked_number)
    return db_blocked_number


def get_blocked_number(db: Session, blocked_number_id: int):
    return db.query(models.BlockedNumbers).filter(models.BlockedNumbers.id == blocked_number_id).first()


# UserReports CRUD
def create_user_report(db: Session, user_report: schemas.UserReportCreate):
    db_user_report = models.UserReports(**user_report.dict())
    db.add(db_user_report)
    db.commit()
    db.refresh(db_user_report)
    return db_user_report


def get_user_report(db: Session, user_report_id: int):
    return db.query(models.UserReports).filter(models.UserReports.id == user_report_id).first()


# Reporters CRUD
def create_reporter(db: Session, reporter: schemas.ReporterCreate):
    # Проверка на существование записи
    existing_report = db.query(models.Reporters).filter(
        models.Reporters.ReporterNumber == reporter.ReporterNumber,
        models.Reporters.ReportedNumber == reporter.ReportedNumber
    ).first()

    if existing_report:
        raise ValueError("Report from this number to this number already exists.")

    db_reporter = models.Reporters(**reporter.dict())
    db.add(db_reporter)
    try:
        db.commit()
        db.refresh(db_reporter)
        return db_reporter
    except IntegrityError:
        db.rollback()
        raise ValueError("Failed to create report.")


def get_reporters(db: Session):
    return db.query(models.Reporters).all()


def get_blocked_numbers(db: Session):
    return db.query(models.BlockedNumbers).all()
