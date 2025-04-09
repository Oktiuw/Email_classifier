from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_URL = "http://127.0.0.1:8000/predict" 

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        email_message = request.form["email_message"]
        response = requests.post(API_URL, json={"message": email_message})
        if response.status_code == 200:
            prediction = response.json().get("label", "Erreur dans la réponse de l'API.")
        else:
            prediction = "Erreur avec l'API."
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)  # Serveur sur le port 80