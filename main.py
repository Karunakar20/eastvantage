from fastapi import FastAPI
from api.routers import address
from core.db.db_config import engine
from core.db.database import Base

# Create FastAPI app
app = FastAPI(title="Address Book API", description="API for managing addresses and spatial queries")

# Create tables
Base.metadata.create_all(bind=engine)

# Include router
app.include_router(address.router)

@app.get("/")
def home():
    return {"message": "Welcome to Address Book API! Visit /docs for Swagger UI."}
