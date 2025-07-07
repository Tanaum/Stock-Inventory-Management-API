# contains all the code for the api

from flask import Flask, request, jsonify

app = Flask(__name__)

# retrieving info abt an item that has been scanned
@app.route("/scanned/<ItemID>")
def ScannedItemInfo(ItemID):
    # send the itemid over to a function
    # function returns data about the item
    # use a function to decrement the item by 1 (for now)
    # return only: item id, item price, item name
    ...

# for lets say an employee to look up the price of an item
@app.route("/admin/<ItemID>")
def GetInfo(ItemID):
    # send itemid over to a function
    # return the info
    ...

# to update the amount of items restocked
@app.route("/admin/restock/<ItemID>-<RestockedAmount>")
def Restock(ItemID, RestockedAmount):
    # send this info to a function
    # function will update each row accordingly
    ...

if __name__ == "__main__":
    app.run(debug=True)