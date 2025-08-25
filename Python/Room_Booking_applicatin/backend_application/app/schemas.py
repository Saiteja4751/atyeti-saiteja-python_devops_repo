from pydantic import BaseModel

class RoomBase(BaseModel):
    number: str
    type: str
    price: int

class RoomCreate(RoomBase):
    pass

class RoomOut(RoomBase):
    id: int
    is_booked: bool

    class Config:
        from_attributes  = True

class CustomerBase(BaseModel):
    name: str
    contact: str

class CustomerCreate(CustomerBase):
    pass

class CustomerOut(CustomerBase):
    id: int

    class Config:
        from_attributes  = True

class BookingCreate(BaseModel):
    customer_id: int
    room_id: int
