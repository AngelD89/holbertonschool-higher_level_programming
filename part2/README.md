# HBnB Project - Part 2: API Implementation

## Overview

This is Part 2 of the HBnB project, which implements the business logic and RESTful API endpoints for a property rental application similar to AirBnB. The application is built using Flask and flask-restx, following a modular three-layer architecture.

## Architecture

The application follows a layered architecture:

### 1. Presentation Layer (`app/api/`)
- RESTful API endpoints using Flask-RESTx
- Request validation and response formatting
- API documentation via Swagger

### 2. Business Logic Layer (`app/models/` and `app/services/`)
- Core entity models: User, Place, Review, Amenity
- Business rules and validation
- Facade pattern for simplified communication

### 3. Persistence Layer (`app/persistence/`)
- In-memory repository (to be replaced with database in Part 3)
- Data storage and retrieval operations

## Project Structure

```
part2/
├── app/
│   ├── __init__.py              # Flask app initialization
│   ├── api/
│   │   ├── __init__.py
│   │   └── v1/
│   │       ├── __init__.py
│   │       ├── users.py         # User endpoints
│   │       ├── places.py        # Place endpoints
│   │       ├── reviews.py       # Review endpoints
│   │       └── amenities.py     # Amenity endpoints
│   ├── models/
│   │   ├── __init__.py
│   │   ├── base.py             # Base model
│   │   ├── user.py             # User model
│   │   ├── place.py            # Place model
│   │   ├── review.py           # Review model
│   │   └── amenity.py          # Amenity model
│   ├── services/
│   │   ├── __init__.py
│   │   └── facade.py           # Facade pattern
│   └── persistence/
│       ├── __init__.py
│       └── repository.py        # In-memory repository
├── run.py                       # Application entry point
├── config.py                    # Configuration settings
├── requirements.txt             # Python dependencies
└── README.md                    # This file
```

## Installation

1. Clone the repository:
```bash
git clone https://github.com/AngelD89/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/part2
```

2. Create a virtual environment (recommended):
```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

Start the Flask development server:

```bash
python3 run.py
```

The API will be available at `http://localhost:5000/`

## API Documentation

Interactive API documentation is available via Swagger UI at:
- `http://localhost:5000/api/v1/docs`

## API Endpoints

### Users

- **POST** `/api/v1/users/` - Create a new user
- **GET** `/api/v1/users/` - Get all users
- **GET** `/api/v1/users/<user_id>` - Get user by ID
- **PUT** `/api/v1/users/<user_id>` - Update user

### Amenities

- **POST** `/api/v1/amenities/` - Create a new amenity
- **GET** `/api/v1/amenities/` - Get all amenities
- **GET** `/api/v1/amenities/<amenity_id>` - Get amenity by ID
- **PUT** `/api/v1/amenities/<amenity_id>` - Update amenity

### Places

- **POST** `/api/v1/places/` - Create a new place
- **GET** `/api/v1/places/` - Get all places
- **GET** `/api/v1/places/<place_id>` - Get place by ID (with owner and amenity details)
- **PUT** `/api/v1/places/<place_id>` - Update place

### Reviews

- **POST** `/api/v1/reviews/` - Create a new review
- **GET** `/api/v1/reviews/` - Get all reviews
- **GET** `/api/v1/reviews/<review_id>` - Get review by ID
- **PUT** `/api/v1/reviews/<review_id>` - Update review
- **DELETE** `/api/v1/reviews/<review_id>` - Delete review
- **GET** `/api/v1/reviews/places/<place_id>` - Get all reviews for a place

## Testing with cURL

### Create a User

```bash
curl -X POST http://localhost:5000/api/v1/users/ \
  -H "Content-Type: application/json" \
  -d '{
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com",
    "password": "securepassword123"
  }'
```

### Get All Users

```bash
curl -X GET http://localhost:5000/api/v1/users/
```

### Create an Amenity

```bash
curl -X POST http://localhost:5000/api/v1/amenities/ \
  -H "Content-Type: application/json" \
  -d '{
    "name": "WiFi"
  }'
```

### Create a Place

```bash
curl -X POST http://localhost:5000/api/v1/places/ \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Cozy Apartment",
    "description": "A beautiful apartment in the city center",
    "price": 100.0,
    "latitude": 37.7749,
    "longitude": -122.4194,
    "owner_id": "<user_id>",
    "amenities": ["<amenity_id>"]
  }'
```

### Create a Review

```bash
curl -X POST http://localhost:5000/api/v1/reviews/ \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Great place to stay!",
    "rating": 5,
    "place_id": "<place_id>",
    "user_id": "<user_id>"
  }'
```

### Delete a Review

```bash
curl -X DELETE http://localhost:5000/api/v1/reviews/<review_id>
```

## Validation Rules

### User
- `first_name`: Required, max 50 characters
- `last_name`: Required, max 50 characters
- `email`: Required, valid email format, unique
- `password`: Required, min 6 characters

### Amenity
- `name`: Required, max 50 characters

### Place
- `title`: Required, max 100 characters
- `description`: Required
- `price`: Required, must be positive
- `latitude`: Required, between -90 and 90
- `longitude`: Required, between -180 and 180
- `owner_id`: Required, must reference existing user

### Review
- `text`: Required, cannot be empty
- `rating`: Required, integer between 1 and 5
- `place_id`: Required, must reference existing place
- `user_id`: Required, must reference existing user
- Users cannot review their own places

## Features

- **Data Validation**: All inputs are validated according to business rules
- **Error Handling**: Appropriate HTTP status codes and error messages
- **Extended Serialization**: Related objects include detailed information (e.g., places include owner details)
- **Relationship Management**: Automatic handling of relationships between entities
- **Swagger Documentation**: Interactive API documentation
- **RESTful Design**: Following REST best practices

## Status Codes

- `200 OK`: Successful GET/PUT request
- `201 Created`: Successful POST request
- `204 No Content`: Successful DELETE request
- `400 Bad Request`: Invalid input or validation error
- `404 Not Found`: Resource not found
- `409 Conflict`: Duplicate resource (e.g., email already exists)

## Future Enhancements (Part 3)

- JWT authentication
- Role-based access control
- Database integration with SQLAlchemy
- Advanced querying and filtering
- File uploads for place images

## License

This project is part of the Holberton School curriculum.

## Authors

- Angel D.
