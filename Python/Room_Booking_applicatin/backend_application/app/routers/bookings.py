from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/customers/")
def create_customer(customer: schemas.CustomerCreate, db: Session = Depends(get_db)):
    return crud.create_customer(db, customer)

@router.post("/bookings/")
def book_room(booking: schemas.BookingCreate, db: Session = Depends(get_db)):
    booked = crud.book_room(db, booking)
    if booked:
        return {"status": "success", "booking_id": booked.id}
    return {"status": "failed", "message": "Room not available"}
