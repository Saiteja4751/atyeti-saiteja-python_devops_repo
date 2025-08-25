# main.py

from sqlalchemy.orm import sessionmaker  # Used to manage DB sessions
from db_config import engine  # Import engine from config file
from models import Base, User  # Import Base and User model

# Step 1: Create all tables defined in models.py (if not already created)
Base.metadata.create_all(engine)  # Creates tables in the connected DB

# Step 2: Create a session (used to interact with the DB)
Session = sessionmaker(bind=engine)  # Bind session to the engine
session = Session()  # Create a session object

# Step 3: Create a new user object
new_user = User(name="John Doe", email="john@example.com")  # Create a new User instance

# Step 4: Add and commit the user to the database
session.add(new_user)  # Add the new user to the session
session.commit()  # Commit the transaction to the DB

# Step 5: Query the users table
users = session.query(User).all()  # Retrieve all users from the table

# Step 6: Print the result
for user in users:  # Loop through each user
    print(f"ID: {user.id}, Name: {user.name}, Email: {user.email}")  # Print user details

# Step 7: Close the session
session.close()  # It's a good practice to close the session
