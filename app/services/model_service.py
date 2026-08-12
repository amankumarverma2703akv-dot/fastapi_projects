import joblib

model, scaler = joblib.load("models/model.joblib")

def predict(features: list):
    scaled = scaler.transform([features])
    return int(model.predict(scaled)[0])
