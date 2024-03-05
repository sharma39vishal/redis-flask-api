# Redis API with Flask

This is a simple RESTful API built with Flask for interacting with a Redis database. It provides endpoints for setting key-value pairs and retrieving values associated with keys.

## Setup

1. Clone the repository:

    ```
    git clone https://github.com/sharma39vishal/redis-flask-api.git
    ```

2. Install dependencies:

    ```
    pip install -r requirements.txt
    ```

3. Set up environment variables:
   
   Create a `.env` file in the root directory of the project and add the following:

    ```
    REDIS_HOST=your_redis_host
    REDIS_PORT=your_redis_port
    REDIS_PASSWORD=your_redis_password
    ```

   Replace `your_redis_host`, `your_redis_port`, and `your_redis_password` with your actual Redis Cloud credentials.

4. Run the Flask app:

    ```
    python app.py
    ```

   The API will start running on `http://localhost:5000`.

## Endpoints

### Get Value
- **URL:** `/get_value/<key>`
- **Method:** `GET`
- **Parameters:**
  - `key`: The key for which to retrieve the value
- **Response:**
  - Success: `200 OK`
    ```json
    {
        "key": "<key>",
        "value": "<value>"
    }
    ```
  - Not Found: `404 Not Found`
    ```json
    {
        "error": "Key not found"
    }
    ```

### Set Value
- **URL:** `/set_value`
- **Method:** `POST`
- **Body:**
  ```json
  {
      "key": "<key>",
      "value": "<value>"
  }
  ```
- **Response:**
  - Success: `201 Created`
    ```json
    {
        "message": "Key-value pair set successfully"
    }
    ```
  - Bad Request: `400 Bad Request`
    ```json
    {
        "error": "Key and value must be provided in JSON format"
    }
    ```

