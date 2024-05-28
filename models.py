from sqlalchemy import Column, Integer, String, Date
from database import Base


class ReportedNumbers(Base):
    __tablename__ = "ReportedNumbers"
    id = Column(Integer, primary_key=True, index=True)
    phoneNumber = Column(String, unique=True, index=True)
    reportCount = Column(Integer)


class BlockedNumbers(Base):
    __tablename__ = "BlockedNumbers"
    id = Column(Integer, primary_key=True, index=True)
    phoneNumber = Column(String, unique=True, index=True)
    blockedDate = Column(Date)


class UserReports(Base):
    __tablename__ = "UserReports"
    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer)
    phoneNumber = Column(String)


class Reporters(Base):
    __tablename__ = "Reporters"
    ReporterNumber = Column(String, primary_key=True, index=True)
    ReportedNumber = Column(String, primary_key=True, index=True)
