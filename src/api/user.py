from fastapi import APIRouter, HTTPException
import datetime
from pydantic import BaseModel, Field
from typing import List
from bson import ObjectId
from src.schemas.user import User
from src.db.database import users

router = APIRouter()

def format_result(user) -> dict:
    return {
        "name": user.get("name"),
        "email": user.get("email"),
        "password": user.get("password"),
        "creation_date": user.get("creation_date"),
        "time_using_vape": user.get("time_using_vape"),
        "frequency_using_vape": user.get("frequency_using_vape"),
        "times_of_day_using_vape": user.get("times_of_day_using_vape"),
        "reasons_using_vape": user.get("reasons_using_vape"),
        "tried_to_quit": user.get("tried_to_quit"),
        "biggest_challenge_imagined": user.get("biggest_challenge_imagined"),
        "quit_attempts": user.get("quit_attempts"),
        "challenges_faced": user.get("challenges_faced"),
        "strategies_to_quit": user.get("strategies_to_quit"),
        "failures": user.get("failures"),
        "perceives_health_impact": user.get("perceives_health_impact"),
        "health_impacts": user.get("health_impacts"),
        "current_program_participation": user.get("current_program_participation"),
        "motivation_level": user.get("motivation_level"),
        "hobbies": user.get("hobbies"),
        "willing_to_receive_notifications": user.get("willing_to_receive_notifications"),
        "additional_habits_info": user.get("additional_habits_info")
    }

# create user
@router.post("/", response_model=User, status_code=201)
async def create_user(user: User):
    user_dict = user.dict()
    user_dict["creation_date"] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    created_user = await users.find_one({"email": user_dict["email"]})
    if not created_user:
        result = await users.insert_one(user_dict)
        new_user = await users.find_one({"_id": result.inserted_id})
        return format_result(new_user)
    raise HTTPException(status_code=400, detail="User could not be created")

# get users
@router.get("/", response_model=List[User])
async def get_users():
    user_list = []
    async for user in users.find():
        user_list.append(format_result(user))
    return user_list
