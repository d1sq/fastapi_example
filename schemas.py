from pydantic import BaseModel


class ReportedNumberBase(BaseModel):
    phoneNumber: str
    reportCount: int


class ReportedNumberCreate(ReportedNumberBase):
    pass


class ReportedNumber(ReportedNumberBase):
    id: int

    class Config:
        from_attributes = True


class BlockedNumberBase(BaseModel):
    phoneNumber: str
    blockedDate: str


class BlockedNumberCreate(BlockedNumberBase):
    pass


class BlockedNumber(BlockedNumberBase):
    id: int

    class Config:
        from_attributes = True


class UserReportBase(BaseModel):
    userId: int
    phoneNumber: str


class UserReportCreate(UserReportBase):
    pass


class UserReport(UserReportBase):
    id: int

    class Config:
        from_attributes = True


class ReporterBase(BaseModel):
    ReporterNumber: str
    ReportedNumber: str


class ReporterCreate(ReporterBase):
    pass


class Reporter(ReporterBase):
    class Config:
        from_attributes = True
