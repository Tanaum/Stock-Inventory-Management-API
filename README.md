# Stock Inventory Mangement API

A simple RESTful API built with **Flask** and **MongoDB Atlas** to manage inventory for a store-like system.

## Features
- Fetching item info upon scanning
- Automatically decrementing stock on scan
- Restocking items
- Flagging low-stock items
- Out-of-stock check
- Secure `.env` usage for MongoDB URI
  
## Technologies Used
- Python
- Flask
- MongoDB (hosted on MongoDB Atlas)
- `pymongo`
- `python-dotenv`

## API Endpoints

### 1. **GET** `/scanned/<ItemID>/<NumTimesScanned>`
Returns basic info (name, price, total price) for a scanned item.  
Rejects if item is out of stock.

### 2. **PATCH** `/scanned/<ItemID>/<NumTimesScanned>`
Decreases the item's `NumInStock` by the number of times it was scanned.  
Automatically flags item if stock drops to ≤10.

### 3. **GET** `/admin/<ItemID>`
Returns full data for the given item. Useful for store employees/admins.

### 4. **PATCH** `/admin/restock/<ItemID>/<RestockedAmount>`
Increases the stock of an item by the given amount.

## Project Structure
├── main.py          # Flask API code
├── dbCode.py        # Database logic (fetching, updating)
├── .env             # MongoDB URI (in .gitignore)
├── requirements.txt # pip packages
├── README.md        # (this file)
