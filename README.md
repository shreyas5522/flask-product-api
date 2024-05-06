## Basic GUIDE TO RUN APP ON UBUNTU/DEBAIN Linux Based System

### Step 1: Install Required Libraries
Ensure you have Python and pip installed. Then, install Flask, SQLAlchemy, Flask-SQLAlchemy, Flask-JWT-Extended, and Werkzeug:

```bash
sudo apt update
sudo apt install python3 python3-pip
sudo apt-get install python-is-python3
sudo apt-get install python3-pip
sudo apt-get install pkg-config libmysqlclient-dev
sudo apt install mysql-server
sudo apt-get install python3-venv

```


```bash
pip install Flask 
pip install Flask-SQLAlchemy 
pip install Flask-WTF 
pip install Flask-Login 
pip install mysqlclient
pip3 install Flask-JWT-Extended Werkzeug
```


### 2. Setup of MySQL

```bash
sudo mysql -u root -p 
```
#### MySQL Commands
> **Note:**
> Replace with your password in new_password.
```bash
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY '12341234';
```
```bash
FLUSH PRIVILEGES;
```
##### Login to MySQL With Updated Commands
1. Create a MySQL database:

    ```bash
    mysql -u your_username -p
    ```

2. Create the database:

    ```sql
    CREATE DATABASE IF NOT EXISTS pythonAPI;
    USE pythonAPI;
    ```

### Step 4: Run the Flask Application
Run the Flask application:

```bash
python3 app.py
```

This will start the Flask development server, and you should see output indicating that the server is running.

### Step 5: Use the API
Now that the API is running, you can use `curl` commands or any other HTTP client to interact with it. Here are some example `curl` commands:

- **Sign Up**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username": "example_user", "password": "example_password"}' http://localhost:5000/signup
  ```

- **Login**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"username": "example_user", "password": "example_password"}' http://localhost:5000/login
  ```

- **Get Products**:
  ```bash
  curl -X GET http://localhost:5000/products -H "Authorization: Bearer your_jwt_token_here"
  ```

- **Create Product**:
  ```bash
  curl -X POST -H "Content-Type: application/json" -d '{"title": "Example Product", "description": "This is an example product", "price": 10.99}' -H "Authorization: Bearer your_jwt_token_here" http://localhost:5000/products
  ```

- **Update Product**:
  ```bash
  curl -X PUT -H "Content-Type: application/json" -d '{"title": "Updated Product Title", "description": "Updated product description", "price": 19.99}' -H "Authorization: Bearer your_jwt_token_here" http://localhost:5000/products/<product_id>
  ```

- **Delete Product**:
  ```bash
  curl -X DELETE -H "Authorization: Bearer your_jwt_token_here" http://localhost:5000/products/<product_id>
  ```

Replace `your_jwt_token_here` with the JWT token obtained during login, and `<product_id>` with the actual ID of the product.


