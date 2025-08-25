from sqlalchemy.orm import Session
from app import models, schemas

def create_room(db: Session, room: schemas.RoomCreate):
    db_room = models.Room(**room.dict())
    db.add(db_room)
    db.commit()
    db.refresh(db_room)
    return db_room

def create_customer(db: Session, customer: schemas.CustomerCreate):
    db_customer = models.Customer(**customer.dict())
    db.add(db_customer)
    db.commit()
    db.refresh(db_customer)
    return db_customer

def book_room(db: Session, booking: schemas.BookingCreate):
    db_room = db.query(models.Room).filter(models.Room.id == booking.room_id).first()
    if db_room and not db_room.is_booked:
        db_room.is_booked = True
        db_booking = models.Booking(**booking.dict())
        db.add(db_booking)
        db.commit()
        return db_booking
    return None

def get_available_rooms(db: Session):
    return db.query(models.Room).filter_by(is_booked=False).all()
