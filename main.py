# contains all the code for the api

from flask import Flask, request, jsonify
from dbCode import GetScannedItemInfo, UpdateInfoRestocked, UpdateInfoScanned

app = Flask(__name__)

# retrieving info abt an item that has been scanned
@app.route("/scanned/<ItemID>/<NumTimesScanned>", methods=["GET"])
def ScannedItemInfo(ItemID, NumTimesScanned):
    # send the itemid over to a function
    # function returns data about the item
    # use a function to decrement the item by 1 (for now)
    # return only: item id, item price, item name
    AllData = GetScannedItemInfo(ItemID) # will get back a dict
    ReturnData = {
        "id": AllData["_id"],
        "ItemName" : AllData["ItemName"],
        "Price" : AllData["Price"],
        "TotalPrice" : AllData["Price"]*int(NumTimesScanned)
    }

    return jsonify(ReturnData)
    #wait i just realised wont this use post too??? --> make it into separate functions (idt these are called functions but idek)

# to decrement
@app.route("/scanned/<ItemID>/<NumTimesScanned>", methods=["PATCH"])
def DecrementItems(ItemID, NumTimesScanned):
    x = UpdateInfoScanned(ItemID, NumTimesScanned) # to be coded -- will return true/false value
    if x:
        data = {"message":"Data successfully stored"}
        return jsonify(data), 200
    else:
        data = {"message":"An error occured"}
        return jsonify(data), 400   

# for lets say an employee to look up the price of an item
@app.route("/admin/<ItemID>", methods=["GET"])
def GetInfo(ItemID):
    # send itemid over to a function
    # return the info
    AllData = GetScannedItemInfo(ItemID)
    return jsonify(AllData)

# to update the amount of items restocked
@app.route("/admin/restock/<ItemID>/<RestockedAmount>", methods=["PATCH"])
def Restock(ItemID, RestockedAmount):
    # send this info to a function
    # function will update each row accordingly
    x = UpdateInfoRestocked(ItemID, RestockedAmount) # will return true/false value
    if x:
        data = {"message":"Data successfully stored"}
        return jsonify(data), 200
    else:
        data = {"message":"An error occured"}
        return jsonify(data), 400

if __name__ == "__main__":
    app.run(debug=True)