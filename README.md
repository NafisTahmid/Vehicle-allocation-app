## Overview
The Vehicle Allocation System is a FastAPI application integrated with MongoDB that allows employees to allocate vehicles for a day. The application ensures that a vehicle can only be allocated once on any specific day. The system supports basic CRUD operations for vehicle allocation and provides a history report for all allocations.

## Features
- Allocate vehicles to employees for specific dates.
- Update and delete vehicle allocations before the allocation date.
- Generate history reports with appropriate filters.
- Proper API documentation available via Swagger.
- Unit testing and integration testing included.

## Technologies Used
- FastAPI
- MongoDB
- Pydantic
- Python
- Uvicorn

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/NafisTahmid/Vehicle-allocation-app.git
   cd Vehicle-allocation-app

2. **Set Up a Virtual Environment**

python -m venv venv
source venv/bin/activate  # For Linux/macOS
venv\Scripts\activate     # For Windows


3. Install Dependencies
pip install -r requirements.txt

4. Set Up MongoDB

	-> Create a MongoDB Atlas account (if you don't have one).
	-> Set up a cluster and create a database named vehicle_allocation_db.
 	-> Add the necessary collections (e.g., allocations, vehicles, employees).

5. Configure Database Connection

Update the MongoDB connection URI in the configurations.py file.

6. Running the Application
To start the FastAPI application, run:

uvicorn main:app --reload
Access the application at http://127.0.0.1:8000.

7. API Documentation
The API documentation can be accessed via Swagger at http://127.0.0.1:8000/docs.

Usage
Endpoints
	-> GET /allocations: Retrieve all allocations.
 	-> POST /allocations: Create a new allocation.
	-> PUT /allocations/{allocation_id}: Update an existing allocation.
	-> DELETE /allocations/{allocation_id}: Delete an allocation.
	-> GET /allocations/history: Retrieve allocation history with filters.
Testing
To run the unit tests, use:


pytest tests/

Contributing
Contributions are welcome! Please open an issue or submit a pull request.

License
This project is licensed under the MIT License.

Acknowledgments
Thanks to the FastAPI and MongoDB communities for their incredible resources and support.
sql
Copy code

### Customization
- Modify any sections to better reflect your project specifics (like the API endpoints).
- Add any additional information that might be relevant, such as screenshots or examples.
- Ensure to keep the MongoDB connection instructions accurate to your setup.

Feel free to ask if you need any adjustments or additional sections!
