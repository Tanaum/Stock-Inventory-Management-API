# will containt all the code to retrieve data from the db and to update it
import os
from dotenv import load_dotenv
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

load_dotenv() # loads stuff from .env into environment variables

uri = os.getenv("MONGO_URI")

uri = os.getenv("MONGO_URI")

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

db = client['inventory']
collection = db['inventory_items']

def GetScannedItemInfo(ItemID):
    query = {"_id": ItemID}
    doc = collection.find_one(query)
    return doc

def UpdateInfoRestocked(ItemID, RestockedAmount):
    query = {"_id":ItemID}
    doc = collection.find_one(query)
    newvalue = {"$set":{"NumInStock": (doc["NumInStock"] + RestockedAmount)}}
    result = collection.update_one(query, newvalue)

    return result.modified_count > 0 # checks if anything even modified