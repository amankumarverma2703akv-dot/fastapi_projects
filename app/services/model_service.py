import joblib
import os

# Safe loader that checks both root and models directory
model_path = "models/model.joblib" if os.path.exists("models/model.joblib") else "model.joblib"

try:
    model = joblib.load(model_path)
except Exception as e:
    model = None

def predict(features: list):
    if model is None:
        return 0
    return int(model.predict([features])[0])
