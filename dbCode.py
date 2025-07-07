import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson.decimal128 import Decimal128

load_dotenv() # loads stuff from .env into environment variables

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

db = client['inventory']
collection = db['inventory_items']

def GetScannedItemInfo(ItemID):
    query = {"_id": ItemID}
    doc = collection.find_one(query)
    # Convert Decimal128s to str
    if isinstance(doc["Price"], Decimal128):
        doc["Price"] = str(doc["Price"].to_decimal())
    return doc

def UpdateInfoRestocked(ItemID, RestockedAmount):
    query = {"_id":ItemID}
    doc = collection.find_one(query)
    NewAmount = doc["NumInStock"] + RestockedAmount
    newvalue = {"$set":{"NumInStock": NewAmount}}
    result = collection.update_one(query, newvalue)

    return result.modified_count > 0 # checks if anything even modified

def UpdateInfoScanned(ItemID, NumTimesScanned):
    query = {"_id":ItemID}
    doc = collection.find_one(query)
    NewAmount = doc["NumInStock"] - NumTimesScanned

    if NewAmount <= 10:
        newvalue = {"$set":{"NumInStock": NewAmount, "Flagged": True}}
        result = collection.update_one(query, newvalue)
    else:
        newvalue = {"$set":{"NumInStock": NewAmount}}
        result = collection.update_one(query, newvalue)        

    return result.modified_count > 0