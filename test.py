import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["school"]
collection = db["students"]
query = { "name": "John" }
print(collection.find_one(query))