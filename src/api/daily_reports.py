from fastapi import APIRouter, HTTPException
import datetime
from pydantic import BaseModel, EmailStr, Field
from typing import List
from src.schemas.daily_report import DailyReport
from src.db.database import daily_reports

router = APIRouter()

def format_daily_report(report) -> dict:
    return {
        "email": report.get("email"),
        "date": report.get("date"),
        "details": report.get("details"),
        "description": report.get("description")
    }

@router.post("/", response_model=DailyReport, status_code=201)
async def create_daily_report(report: DailyReport):
    report_dict = report.dict()
    today_date = datetime.datetime.now().strftime("%Y-%m-%d")
    
    if report_dict.get("date") == "string":
        report_dict["date"] = today_date

    existing_report = await daily_reports.find_one({"email": report_dict["email"], "date": report_dict["date"]})
    if existing_report:
        raise HTTPException(status_code=400, detail="A report for the given date already exists")
    
    result = await daily_reports.insert_one(report_dict)
    new_report = await daily_reports.find_one({"_id": result.inserted_id})
    
    return format_daily_report(new_report)


@router.get("/{email}", response_model=List[DailyReport])
async def get_daily_reports(email: str):
    reports = []
    async for report in daily_reports.find({"email": email}):
        reports.append(format_daily_report(report))
    return reports
