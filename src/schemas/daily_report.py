from pydantic import BaseModel, Field, EmailStr
from src.schemas.daily_report_answers import Feelings
from typing import List, Union
import datetime

class DailyReport(BaseModel):
    email: EmailStr
    date: str = Field(default_factory=lambda: datetime.datetime.now().strftime("%Y-%m-%d"))
    details: List[Union[Feelings, str]]
    description: str 

    class Config:
        schema_extra = {
            "example": {
                "email": "user@example.com",
                "details": ["Triste", "Ansioso", "Estressado"],
                "description": "Tive um dia muito difícil"	
            }
        }
