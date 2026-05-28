from fastapi import FastAPI
from backend.routes import inference, health

app = FastAPI(title="LLMOps Monitoring System")

app.include_router(inference.router)
app.include_router(health.router)
