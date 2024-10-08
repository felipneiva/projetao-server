import motor.motor_asyncio
from bson.objectid import ObjectId

MONGO_DETAILS = "mongodb+srv://podpararteste:lrM9mQ3izt4lyaHs@cluster0.wmxepkw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_DETAILS)

database = client.podparar
users = database.get_collection("users")
daily_reports = database.get_collection("daily_reports")

def format_result(result):
    if result:
        result["_id"] = str(result["_id"])
    return result
