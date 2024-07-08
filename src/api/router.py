from fastapi import APIRouter

from src.api import test


api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])

