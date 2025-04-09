from fastapi import FastAPI
from pydantic import BaseModel
import joblib

# Charger le modèle et le vectorizer
model = joblib.load("Model/spam_classifier_model.joblib")
vectorizer = joblib.load("Model/tfidf_vectorizer.joblib")

app = FastAPI()

class Email(BaseModel):
    message: str

@app.post("/predict")
def predict_spam(email: Email):
    # Transformer le texte en vecteur
    message_vector = vectorizer.transform([email.message])
    
    # Prédiction
    prediction = model.predict(message_vector)
    
    return {"label": prediction[0]}