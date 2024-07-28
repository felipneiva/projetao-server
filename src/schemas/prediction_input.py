from pydantic import BaseModel

class PredictionInput(BaseModel):
    latitude: float
    longitude: float
    seconds: int
    minutes: int
    hour: int
    day_of_week: int