from fastapi import APIRouter

from src.api import test
from src.api import user


api_router = APIRouter()
api_router.include_router(test.router, prefix="/test", tags=["test"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
