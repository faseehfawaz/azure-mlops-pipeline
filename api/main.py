import mlflow
import numpy as np
from fastapi import FastAPI

app = FastAPI()

mlflow.set_tracking_uri("http://mlflow:5000")

MODEL_URI = "models:/LogisticRegression/latest"
model = None

@app.on_event("startup")
def load_model():
    global model
    try:
        model = mlflow.sklearn.load_model(MODEL_URI)
        print("Model loaded successfully")
    except Exception as e:
        print("Model not available yet:", e)

@app.post("/predict")
def predict(data: list):
    if model is None:
        return {"error": "Model not loaded"}
    arr = np.array(data)
    preds = model.predict(arr)
    return {"predictions": preds.tolist()}
