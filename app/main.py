from fastapi import FastAPI
from app.api import routes_auth, routes_predict
from app.middleware.logging_middleware import LoggingMiddleware

app = FastAPI()
app.include_router(routes_auth.router)
app.include_router(routes_predict.router)
app.add_middleware(LoggingMiddleware)
