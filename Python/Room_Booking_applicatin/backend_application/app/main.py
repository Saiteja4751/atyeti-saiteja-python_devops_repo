from fastapi import FastAPI
from app.database import engine, Base
from app.routers import rooms, bookings

app = FastAPI()

# Create MySQL tables
Base.metadata.create_all(bind=engine)

app.include_router(rooms.router, prefix="/api", tags=["Rooms"])
app.include_router(bookings.router, prefix="/api", tags=["Bookings"])
