# Product Management API

A simple REST API built with FastAPI and Pydantic for managing products. This project provides full CRUD functionality using an in-memory data structure.

## Features
* **Add a product:** Validate and store new products.
* **View products:** Retrieve all products or a specific product by its ID.
* **Update a product:** Modify existing product details.
* **Delete a product:** Remove products from the database.
* **Error Handling:** Returns proper 404 responses for non-existent items and 400 responses for duplicate IDs.

## Prerequisites
* Python 3.8+

## Installation

1. **Clone the repository:**
   ```bash
   git clone <your-repository-url>
   cd <your-repository-folder>

2. **Activate your virtual environment:**

    ```bash
    .\myenv\Scripts\activate
3. **Install the project dependencies:**

    ```bash
    pip install -r requirements.txt

## Running the Application

**Start the local server using Uvicorn:**

    ```bash
    uvicorn main:app --reload
**Testing the API**
*FastAPI automatically generates interactive documentation. Once the server is running, open your web browser and navigate to:
http://127.0.0.1:8000/docs