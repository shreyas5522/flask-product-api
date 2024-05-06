
### API Documentation

This API allows users to manage products and user authentication.

### Base URL
```
http://localhost:5000/
```

### Endpoints

#### 1. User Authentication

##### Sign Up
- **URL:** `/signup`
- **Method:** `POST`
- **Description:** Creates a new user account.
- **Request Body:**
  ```json
  {
      "username": "example_user",
      "password": "example_password"
  }
  ```
- **Response:**
  - `201 Created`: User created successfully
  - `400 Bad Request`: Invalid request body

##### Login
- **URL:** `/login`
- **Method:** `POST`
- **Description:** Authenticates a user and provides a JWT token.
- **Request Body:**
  ```json
  {
      "username": "example_user",
      "password": "example_password"
  }
  ```
- **Response:**
  - `200 OK`: JWT token provided
  - `401 Unauthorized`: Invalid username or password

#### 2. Product Management

##### Get Products
- **URL:** `/products`
- **Method:** `GET`
- **Description:** Retrieves a list of all products.
- **Authorization Header:** `Bearer <JWT Token>`
- **Response:**
  - `200 OK`: List of products retrieved successfully

##### 3. Get Product by ID
- **URL:** `/products/<product_id>`
- **Method:** `GET`
- **Description:** Retrieves details of a specific product.
- **Authorization Header:** `Bearer <JWT Token>`
- **Response:**
  - `200 OK`: Product details retrieved successfully
  - `404 Not Found`: Product not found

##### 4. Create Product
- **URL:** `/products`
- **Method:** `POST`
- **Description:** Creates a new product.
- **Authorization Header:** `Bearer <JWT Token>`
- **Request Body:**
  ```json
  {
      "title": "Example Product",
      "description": "This is an example product",
      "price": 10.99
  }
  ```
- **Response:**
  - `201 Created`: Product created successfully
  - `400 Bad Request`: Invalid request body

##### 5. Update Product
- **URL:** `/products/<product_id>`
- **Method:** `PUT`
- **Description:** Updates details of a specific product.
- **Authorization Header:** `Bearer <JWT Token>`
- **Request Body:**
  ```json
  {
      "title": "Updated Product Title",
      "description": "Updated product description",
      "price": 19.99
  }
  ```
- **Response:**
  - `200 OK`: Product updated successfully
  - `404 Not Found`: Product not found

##### 6. Delete Product
- **URL:** `/products/<product_id>`
- **Method:** `DELETE`
- **Description:** Deletes a specific product.
- **Authorization Header:** `Bearer <JWT Token>`
- **Response:**
  - `200 OK`: Product deleted successfully
  - `404 Not Found`: Product not found

