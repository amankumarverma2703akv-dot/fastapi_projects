from fastapi import FastAPI
from app.api import routes_auth, routes_predict

app = FastAPI(title="BFSI Loan Approval API")

@app.get("/")
def root():
    return {"status": "ok", "message": "BFSI Loan Approval API is running!"}

app.include_router(routes_auth.router)
app.include_router(routes_predict.router)
