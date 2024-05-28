from fastapi import FastAPI
from database import init_db
from routers import reported_numbers, blocked_numbers, user_reports, reporters

app = FastAPI()


@app.on_event("startup")
async def startup():
    init_db()


app.include_router(reported_numbers.router, prefix="/reportednumbers", tags=["reported numbers"])
app.include_router(blocked_numbers.router, prefix="/blockednumbers", tags=["blocked numbers"])
app.include_router(user_reports.router, prefix="/userreports", tags=["user reports"])
app.include_router(reporters.router, prefix="/reporters", tags=["reporters"])
