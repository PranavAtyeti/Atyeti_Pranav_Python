from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

app = FastAPI(title="Iris Prediction API")

model = joblib.load("iris_model.joblib")

class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

species = ["setosa", "versicolor", "virginica"]

@app.get("/")
def home():
    return {"message": "Welcome to the Iris Prediction API"}

@app.post("/predict/")
def predict(data: IrisInput):
    input_data = np.array([[data.sepal_length, data.sepal_width, data.petal_length, data.petal_width]])

    prediction = model.predict(input_data)[0]
    predicted_species = species[prediction]

    return {"prediction": predicted_species}
