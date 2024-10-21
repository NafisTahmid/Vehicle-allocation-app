from fastapi import FastAPI, HTTPException, Depends
from database.models import Employee, Vehicle, Allocation, UpdateAllocation
from configurations import employees_collection, vehicles_collection, allocations_collection, db
from bson.objectid import ObjectId
from datetime import datetime

app = FastAPI()
# Get all allocations
@app.get("/", response_model=list)
async def get_all_allocations():
    allocations = list(db.allocations.find())
    # Convert ObjectId to string for JSON serialization
    for allocation in allocations:
        allocation["_id"] = str(allocation["_id"])
    return allocations

# Get a specific allocation by ID
@app.get("/allocations/{allocation_id}", response_model=Allocation)
async def read_allocation(allocation_id: str):
    allocation = db.allocations.find_one({"_id": ObjectId(allocation_id)})
    if not allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")
    allocation["_id"] = str(allocation["_id"])  # Convert ObjectId to string
    return allocation

@app.post("/allocate/")
async def allocate_vehicle(allocation: Allocation):
    # Check if the vehicle is already allocated for the day
    if allocations_collection.find_one({"vehicle_id": allocation.vehicle_id, "date": allocation.date}):
        raise HTTPException(status_code=400, detail="Vehicle is already allocated for this date.")

    # Check if the allocation date is in the future
    if allocation.date < datetime.today():
        raise HTTPException(status_code=400, detail="You can only allocate for future dates.")

    # Insert allocation data
    allocations_collection.insert_one(allocation.dict())
    return {"message": "Vehicle allocated successfully."}


@app.put("/update-allocation/{allocation_id}")
async def update_allocation(allocation_id: str, updated_data: UpdateAllocation):
    allocation = allocations_collection.find_one({"_id": ObjectId(allocation_id)})
    if not allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")

    # Ensure the allocation date is not in the past
    if allocation['date'] < datetime.today():
        raise HTTPException(status_code=400, detail="You cannot update allocations for past dates.")

    # Ensure the new vehicle is not already allocated on the given date
    if allocations_collection.find_one({"vehicle_id": updated_data.vehicle_id, "date": updated_data.date}):
        raise HTTPException(status_code=400, detail="Vehicle is already allocated for this date.")

    allocations_collection.update_one({"_id": ObjectId(allocation_id)}, {"$set": updated_data.dict()})
    return {"message": "Allocation updated successfully."}


@app.delete("/delete-allocation/{allocation_id}")
async def delete_allocation(allocation_id: str):
    allocation = allocations_collection.find_one({"_id": ObjectId(allocation_id)})
    if not allocation:
        raise HTTPException(status_code=404, detail="Allocation not found.")
    
    if allocation['date'] < datetime.today():
        raise HTTPException(status_code=400, detail="You cannot delete allocations for past dates.")

    allocations_collection.delete_one({"_id": ObjectId(allocation_id)})
    return {"message": "Allocation deleted successfully."}


@app.get("/history/")
async def get_allocation_history(employee_id: str = None, vehicle_id: str = None, start_date: datetime = None, end_date: datetime = None):
    query = {}
    
    if employee_id:
        query['employee_id'] = employee_id
    if vehicle_id:
        query['vehicle_id'] = vehicle_id
    if start_date and end_date:
        query['date'] = {"$gte": start_date, "$lte": end_date}

    allocations = allocations_collection.find(query)
    return list(allocations)