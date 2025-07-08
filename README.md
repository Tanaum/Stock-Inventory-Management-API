# Stock Inventory Management API

A simple RESTful API built with **Flask** and **MongoDB Atlas** to manage inventory for a store-like system.

## Features
- Fetching item info upon scanning
- Automatically decrementing stock on scan
- Restocking items
- Flagging low-stock items
- Out-of-stock check
- Secure `.env` usage for MongoDB URI
  
## Technologies Used
- Flask
- MongoDB (hosted on MongoDB Atlas)
- Postman (for testing the API)
- `pymongo`
- `python-dotenv`

## What I Learned
- Using `.env` to avoid accidentally pushing sensitive data onto a public repo
- CRUD operations in MongoDB
- Difference between PATCH/POST/PUT HTTP methods

## API Endpoints

### GET
1. `/scanned/<ItemID>/<NumTimesScanned>`
  - Returns basic info (name, price, total price) for a scanned item.
  - Rejects if item is out of stock.
2. `/admin/<ItemID>`
  - Returns full data for the given item. Useful for store employees/admins.

### PATCH
1. `/scanned/<ItemID>/<NumTimesScanned>`
  - Decreases the item's `NumInStock` by the number of times it was scanned.
  - Automatically flags item if stock drops to ≤10.

2. `/admin/restock/<ItemID>/<RestockedAmount>`
  - Increases the stock of an item by the given amount.

## How To Run It
1. Clone the repository onto your machine.
2. Make sure that necessary libraries are installed using:
   ```bash
   pip install python-dotenv
   pip install pymongo
   ```
3. In place of `os.getenv("MONGO_URI")` paste your MongoDB URI.
4. Add some data into your collection (by either using MongoDB Atlas or Python). It must have the following field names: _id (INT), Price, Flagged (BOOLEAN), ItemName (STR).
5. Run `main.py`, copy the URL in the terminal and paste it in Postman.

Fun facts:
1. I coded all of this in less than 10 hours!
2. It was inspired by an example given in my O Levels CS textbook.
