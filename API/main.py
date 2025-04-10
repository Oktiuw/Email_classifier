import re
from html import escape

from fastapi import FastAPI, Request,HTTPException
from pydantic import BaseModel
import joblib
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from googletrans import Translator
from langdetect import detect

limiter = Limiter(key_func=get_remote_address)
MAX_MESSAGE_LENGTH = 5000

model = joblib.load("Model/spam_classifier_model.joblib")
vectorizer = joblib.load("Model/tfidf_vectorizer.joblib")

app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
translator = Translator()



class Email(BaseModel):
    message: str
def clean_input(input_str: str) -> str:
    input_str = re.sub(r'[^a-zA-Z0-9\s.,!?\'"]', '', input_str)
    return escape(input_str)

@app.post("/predict")
@limiter.limit("1/second")  
def predict_spam(email: Email,request: Request):
    if len(email.message) > MAX_MESSAGE_LENGTH:
        raise HTTPException(status_code=400, detail="Message too long. Maximum 5000 characters allowed.")
    detected_language = detect(email.message)
    message=clean_input(email.message)
    if detected_language == 'fr':
        message = translator.translate(message, src='fr', dest='en').text
    message_vector = vectorizer.transform([message])
    prediction = model.predict(message_vector)
    return {"label": prediction[0]}