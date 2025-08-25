# models.py

from sqlalchemy import Column, Integer, String  # Import column types
from sqlalchemy.ext.declarative import declarative_base  # Base class for models

Base = declarative_base()  # This Base class will be inherited by all models

# Define a sample table called 'users'
class User(Base):
    __tablename__ = 'users'  # Name of the table in the database

    id = Column(Integer, primary_key=True)  # Primary key column
    name = Column(String(50))  # Name column of type string
    email = Column(String(100))  # Email column of type string
