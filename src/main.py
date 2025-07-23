from fastapi import FastAPI

from src.routers import flag_route

app = FastAPI(
    title="Feature Flag API",
    description="API for managing feature flags",
    version="0.1.0",
)

app.include_router(flag_route)
# app.include_router(rule_route)
# app.include_router(variation_route)
# app.include_router(prerequisite_route)
# app.include_router(condition_route)
# app.include_router(segment_route)


# Optional root endpoint to check if service is alive
@app.get("/")
async def root():
    return {"message": "Feature Flag API is running"}
