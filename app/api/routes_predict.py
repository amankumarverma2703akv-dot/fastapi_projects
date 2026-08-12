from fastapi import APIRouter, Depends
from app.api.dependencies import get_current_user
from app.services.redis_cache import get_cache, set_cache
from app.services.model_service import predict

router = APIRouter()

@router.post("/predict")
def predict_endpoint(features: list, user: dict = Depends(get_current_user)):
    key = str(features)
    cached = get_cache(key)
    if cached:
        return {"prediction": int(cached), "cached": True}
    result = predict(features)
    set_cache(key, result)
    return {"prediction": result, "cached": False}
