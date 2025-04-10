import re
from html import escape

from fastapi import FastAPI, Request
from pydantic import BaseModel
import joblib
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)

model = joblib.load("Model/spam_classifier_model.joblib")
vectorizer = joblib.load("Model/tfidf_vectorizer.joblib")

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

class Email(BaseModel):
    message: str
def clean_input(input_str: str) -> str:
    input_str = re.sub(r'[^a-zA-Z0-9\s.,!?\'"]', '', input_str)
    return escape(input_str)

@app.post("/predict")
@limiter.limit("1/second")  
def predict_spam(email: Email,request: Request):
    message=clean_input(email.message)
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    return {"label": prediction[0]}