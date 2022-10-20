from fastapi import FastAPI
from pydantic import BaseModel
from app.model.model import predict_pipeline
from app.model.model import __version__ as model_version


app = FastAPI()


class TextIn(BaseModel):
    text: str


@app.get("/")
def home():
    return {"health_check": "OK", "model_version": model_version}


@app.post("/predict")
def predict(payload: TextIn):
    type = predict_pipeline(payload.text)
    return {"Cyberbullying Type": type}