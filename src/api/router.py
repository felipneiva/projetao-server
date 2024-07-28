from fastapi import APIRouter

from src.api import test
from src.api import user
from src.api import daily_reports
from src.api import predict


api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(daily_reports.router, prefix="/daily_reports", tags=["daily_reports"])
api_router.include_router(predict.router, prefix="/predition", tags=["prediction"])