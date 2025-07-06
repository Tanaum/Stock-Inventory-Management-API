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

# sample db + collection + data
# just realised i didnt need this el o el
# db = client['inventory']
# collection = db['inventory_items']
# print(db.list_collection_names())
# data_items = [
#     {"ItemName":"Apple", "Price": 1.50, "NumInStock":50, "Flagged":False},
#     {"ItemName":"Banana", "Price": 0.50, "NumInStock":30, "Flagged":False},
#     {"ItemName":"Orange", "Price": 2.00, "NumInStock":10, "Flagged":True}
# ]