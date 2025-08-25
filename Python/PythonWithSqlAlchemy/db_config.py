# db_config.py

from sqlalchemy import create_engine  # Import the SQLAlchemy engine creator

# Replace the below values with your actual database credentials
USER = 'root'       # Your MySQL username (e.g., 'root')
PASSWORD = 'root'   # Your MySQL password
HOST = 'localhost'           # Host where MySQL is running (usually localhost)
PORT = 3306                  # Default MySQL port
DATABASE = 'testdb'          # Name of your MySQL database

# SQLAlchemy connection URL format: dialect+driver://username:password@host:port/database
DATABASE_URL = f"mysql+mysqlconnector://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}"

# Create the SQLAlchemy engine
engine = create_engine(DATABASE_URL)  # Engine is the starting point for any SQLAlchemy interaction
