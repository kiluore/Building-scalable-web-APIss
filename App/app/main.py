# Remember to run we need to put uvicorn app.main:app --reload in the terminal since our main sits in our app directory
from fastapi import FastAPI
from .score import predict_sentiment
from .models import request_body
 
app = FastAPI(
    title= 'Data Gathering & Warehousing',
    description= 'Deploy Predictive web Service'
)
 
@app.get("/")
def read_root():
    return{"Hello Kent": "Kindly Deploy this model!"}
 
@app.post('/predict')
def predict(data : request_body):
    y_predict = predict_sentiment(data.review)
    return y_predict
 
 
 