from flask import Flask, request, jsonify
from dbCode import GetScannedItemInfo, UpdateInfoRestocked, UpdateInfoScanned

app = Flask(__name__)

# retrieving info abt an item that has been scanned
@app.route("/scanned/<ItemID>/<NumTimesScanned>", methods=["GET"])
def ScannedItemInfo(ItemID, NumTimesScanned):
    AllData = GetScannedItemInfo(int(ItemID)) # will get back a dict

    if AllData is None:
        return jsonify({"Message": "Item not found"}), 400
    elif AllData["Flagged"]:
        return jsonify({"Message": "Item out of stock"}), 400        
    else:
        ReturnData = {
            "id": AllData["_id"],
            "ItemName" : AllData["ItemName"],
            "Price" : AllData["Price"],
            "TotalPrice" : float(AllData["Price"])*int(NumTimesScanned)
        }

        return jsonify(ReturnData), 200        

# to decrement
@app.route("/scanned/<ItemID>/<NumTimesScanned>", methods=["PATCH"])
def DecrementItems(ItemID, NumTimesScanned):
    x = UpdateInfoScanned(int(ItemID), int(NumTimesScanned)) # to be coded -- will return true/false value
    if x:
        data = {"message":"Data successfully stored"}
        return jsonify(data), 200
    else:
        data = {"message":"An error occured"}
        return jsonify(data), 400   

# for lets say an employee to look up the price of an item
@app.route("/admin/<ItemID>", methods=["GET"])
def GetInfo(ItemID):
    AllData = GetScannedItemInfo(int(ItemID))
    if AllData is None:
        return jsonify({"Message": "Item not found"}), 400
    else:        
        return jsonify(AllData), 200

# to update the amount of items restocked
@app.route("/admin/restock/<ItemID>/<RestockedAmount>", methods=["PATCH"])
def Restock(ItemID, RestockedAmount):
    # send this info to a function
    # function will update each row accordingly
    x = UpdateInfoRestocked(int(ItemID), int(RestockedAmount)) # will return true/false value
    if x:
        data = {"message":"Data successfully stored"}
        return jsonify(data), 200
    else:
        data = {"message":"An error occured"}
        return jsonify(data), 400

if __name__ == "__main__":
    app.run(debug=True)