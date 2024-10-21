
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://nafis:abcd1234@vehicle-app.zf3bo.mongodb.net/?retryWrites=true&w=majority&appName=vehicle-app"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Access the database and collections
db = client['vehicle_allocation_db']
employees_collection = db['employees']
vehicles_collection = db['vehicles']
allocations_collection = db['allocations']
