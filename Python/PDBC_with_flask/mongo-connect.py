from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Use or create a database
db = client["myDatabase"]

# Create or access a collection
collection = db["myCollection"]

# Insert a document
collection.insert_one({"name": "Alice", "age": 25})
collection.insert_one({"name": "sai", "age": 23})
print('created succuessfullly')
