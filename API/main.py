from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
model = joblib.load("Model/spam_classifier_model.joblib")
app = FastAPI()
from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer()
class Email(BaseModel):
    message: str
@app.post("/predict")
def predict_spam(email: Email):
    message_vector = vectorizer.transform([email.message])
    prediction = model.predict(message_vector)
    return {"label": prediction[0]}
new_emails = [
    "Congratulations! You've won a free vacation. Click here to claim your prize,.",
    "Meeting reminder: Project update at 2 PM today."
]
newDocumentTermMatrix = vectorizer.transform(new_emails)
predictions = model.predict(newDocumentTermMatrix)
for email, prediction in zip(new_emails, predictions):
    print(f"Email: {email}\nPrediction: {prediction}\n")
message_vector = vectorizer.transform(['test'])
prediction = model.predict(message_vector)
print(prediction)