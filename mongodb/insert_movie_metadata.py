from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017")  # Replace with your MongoDB connection string

# This is like a default dict. Doesn't exist? Will instantiate
db = client.movie
collection = db.metedata

document = {
    "_id": "1", # Make this match the SQL movie db
    "imdb_scrape": {
        "actor": ["bob the bobber", "jason cena", "john dena"],
        "rating": 10
    },
}

result = collection.insert_one(document)

# Print the inserted document's ID
print("Document inserted with ID:", result.inserted_id)
