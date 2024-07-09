from fastapi import APIRouter, HTTPException

router = APIRouter()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId
from src.schemas.user import User
from src.db.database import collection, format_result

# create user

@router.post("/", response_model=User, status_code=201)
async def create_user(user: User):
    user = user.dict()
    result = await collection.insert_one(user)
    created_user = await collection.find_one({"_id": result.inserted_id})
    if created_user:
        return format_result(created_user)
    raise HTTPException(status_code=400, detail="User could not be created")