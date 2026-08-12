from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm
from app.core.security import create_access_token

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    if form_data.username != "admin" or form_data.password != "password":
        return {"error": "Invalid credentials"}
    token = create_access_token({"sub": form_data.username})
    return {"access_token": token, "token_type": "bearer"}
