# KudiGo RestFul APi

This project is a simple Django-based RESTful API that supports basic CRUD operations for managing resources (e.g., books). This README provides comprehensive instructions on how to set up and use the API.
Table of Contents

  - Installation
  - Database Setup
  - Running the Server
  - API Endpoints
  - Examples

# Installation

Before you begin, ensure you have Python and Django installed on your system. You can install Django using pip:
```
pip install django
```

Next, clone this repository to your local machine:
```
git clone https://github.com/dtgamer/Django-Restful-API.git
```
```
cd Django-Restful-API
```

# Install project dependencies:
```
pip install -r requirements.txt
```

# Database Setup

By default, this project uses SQLite as the database backend. To set up the database, run the following commands:
```
python manage.py makemigrations
python manage.py migrate
```

Running the Server

Start the development server:
```
python manage.py runserver
```
The API will be accessible at http://localhost:8000/resources/.

# API Endpoints

This API provides the following endpoints for managing resources:

    GET /resources/: Retrieve a list of all resources.
    POST /resources/: Create a new resource.
    GET /resources/<id>/: Retrieve a specific resource by ID.
    PUT /resources/<id>/: Update a specific resource by ID.
    DELETE /resources/<id>/: Delete a specific resource by ID.

# Examples
Creating a New Resource

To create a new resource (e.g., a book), send a POST request to http://localhost:8000/resources/ with JSON data:

```
curl -X POST -H "Content-Type: application/json" -d '{
  "title": "Sample Book",
  "author": "John Doe",
  "publication_date": "2023-09-23",
  "isbn": "1234567890123",
  "description": "This is a sample book description."
}'
```
```
http://localhost:8000/resources/
```

# Retrieving a List of Resources

To retrieve a list of all resources, send a GET request to http://localhost:8000/resources/:
```
curl http://localhost:8000/resources/
```

Retrieving a Specific Resource

To retrieve a specific resource by its ID, send a GET request to http://localhost:8000/resources/<id>/:
```
curl http://localhost:8000/resources/1/
```
# Updating a Resource
```
curl -X PUT -H "Content-Type: application/json" -d '{
  "title": "Save The Night",
  "author": "Abakpa Dominic",
  "publication_date": "2023-09-20",
  "isbn": "1748935064783",
  "description": "A nice read"
}'
```
```
 http://localhost:8000/resources/1/
```
# Deleting a Resource

To delete a specific resource by its ID, send a DELETE request to http://localhost:8000/resources/<id>/:

```
curl -X DELETE http://localhost:8000/resources/1/
```
