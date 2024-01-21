from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string

# This is like a default dict. Doesn't exist? Will instantiate
db = client.movie
collection = db.metadata

for document in collection.find():
    for k, v in document.items():
        print("{}: {}".format(k, v))
