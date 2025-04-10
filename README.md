# Spam Email Classifier

This project is a **Spam Email Classifier** built using **FastAPI** for the API and **Flask** for the frontend. The system allows users to input email messages, and it classifies them as either "spam" or "normal" based on the content of the email. The model is trained using a Logistic Regression classifier.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [API](#api)
- [Frontend](#frontend)
- [License](#license)
- [Author](#author)

## Features
- **FastAPI** backend that handles the classification of email messages as "spam" or "normal."
- **Flask** frontend that allows users to interact with the classifier via a simple web interface.
- Easy to deploy with a clean design and responsive user interface.

## Installation

Follow the steps below to set up the project on your local machine.

### Prerequisites
1. **Python 3.8+** (preferably 3.9+)
2. **pip** (Python package manager)

### 1. Clone the repository:
```bash
git clone https://github.com/yourusername/spam-email-classifier.git
cd spam-email-classifier
```
### 2. Create and activate a virtual environment
``` 
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```
### 3. Install dependencies:
```
pip install -r requirements.txt
```

## Usage 
### 1. Run the FastAPI backend:
First, ensure that the model is trained and saved as spam_classifier_model.joblib. Then, start the FastAPI backend with the following command:
```
python -m uvicorn API.main:app --reload
```
This will start the FastAPI app at http://127.0.0.1:8000.

### 2. Run the Flask frontend:

```
python Web_interface/app.py
```
This will start the Flask web server at http://127.0.0.1:80.


## API 
The FastAPI backend provides a single endpoint:

#### /predict (POST)
Input: A JSON object with a single key: "message" (the email text).
Output: A JSON object with a "label" field that can either be "spam" or "normal."

## Frontend
The frontend consists of an HTML form where users can input the email message they want to classify. The result (either "spam" or "normal") is displayed once the prediction is returned from the backend.

The frontend is built using Flask and is responsive, making it suitable for both desktop and mobile devices.
## Author
Aurélien VINCENT
Contact: vinau02@gmail.com