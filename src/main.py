from fastapi import FastAPI

from src.routers import (
    flag_router, env_router, variation_router, segment_router
)

app = FastAPI(
    title="Feature Flag API",
    description="API for managing feature flags",
    version="0.1.0",
)

app.include_router(flag_router)
app.include_router(env_router)
app.include_router(variation_router)
app.include_router(segment_router)

# Optional root endpoint to check if service is alive


@app.get("/")
async def root():
    return {"message": "Feature Flag API is running"}
