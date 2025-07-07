# contains all the code for the api

from flask import Flask, request, jsonify

app = Flask(__name__)

# retrieving info abt an item that has been scanned
@app.route("/scanned/<ItemID>", methods=["GET"])
def ScannedItemInfo(ItemID):
    # send the itemid over to a function
    # function returns data about the item
    # use a function to decrement the item by 1 (for now)
    # return only: item id, item price, item name
    AllData = GetScannedItemInfo(ItemID) # will get back a dict -- will define function later
    ReturnData = {
        "id": AllData["_id"],
        "ItemName" : AllData["ItemName"],
        "Price" : AllData["Price"]
    }

    return jsonify(ReturnData)
    #wait i just realised wont this use post too???

# for lets say an employee to look up the price of an item
@app.route("/admin/<ItemID>")
def GetInfo(ItemID):
    # send itemid over to a function
    # return the info
    AllData = GetScannedItemInfo(ItemID)
    return jsonify(AllData)
    ...

# to update the amount of items restocked
@app.route("/admin/restock/<ItemID>/<RestockedAmount>", methods=["POST"])
def Restock(ItemID, RestockedAmount):
    # send this info to a function
    # function will update each row accordingly
    x = UpdateInfo(ItemID, RestockedAmount) # to be coded -- will return true/false value
    if x:
        data = {"message":"Data successfully stored"}
    else:
        data = {"message":"An error occured"}
    
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)