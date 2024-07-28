from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from src.schemas.prediction_input import PredictionInput
import pandas as pd
import xgboost as xgb
import os

# Dynamically determine the model path
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, '..', 'model', 'overall_model.json')

# Load the model (make sure the model file path is correct)
loaded_model = xgb.XGBClassifier()
loaded_model.load_model(model_path)

# Method to perform prediction given an input
def predict(input_data, model):
    """
    Predict if the user is smoking given input data.

    Parameters:
    input_data (list): A list containing latitude, longitude, seconds, minutes, hour, day_of_week.
                       Example: [37.7749, -122.4194, 30, 15, 14, 2]
    model (XGBClassifier): The trained XGBoost model.

    Returns:
    int: 1 if the user is smoking, 0 otherwise.
    """
    input_df = pd.DataFrame([input_data], columns=['latitude', 'longitude', 'seconds', 'minutes', 'hour', 'day_of_week'])
    prediction = model.predict(input_df)
    return int(prediction[0])

# Define the request body model
class PredictionInput(BaseModel):
    latitude: float
    longitude: float
    seconds: int
    minutes: int
    hour: int
    day_of_week: int

router = APIRouter()

@router.put("/", status_code=200, tags=["prediction"])
def test(input_data: PredictionInput):
    data = [input_data.latitude, input_data.longitude, input_data.seconds, input_data.minutes, input_data.hour, input_data.day_of_week]
    
    try:
        result = predict(data, loaded_model)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
    return {"prediction": result}
