from pydantic import BaseModel
from datetime import datetime

class Employee(BaseModel):
    employee_id: str
    name: str
    department: str

class Vehicle(BaseModel):
    vehicle_id: str
    model: str
    driver_name: str

class Allocation(BaseModel):
    allocation_id: str
    employee_id: str
    vehicle_id: str
    date: datetime

class UpdateAllocation(BaseModel):
    vehicle_id: str
    date: datetime