# Flask Calculator API

## Description

A simple REST API built with Flask that performs basic arithmetic operations such as addition, subtraction, multiplication, division, remainder, and power. This API accepts two float inputs via the URL and returns the results of all calculations in JSON format.

## Features

- **Addition**: Adds two numbers.
- **Subtraction**: Subtracts the second number from the first.
- **Multiplication**: Multiplies two numbers.
- **Division**: Divides the first number by the second (excluding division by zero).
- **Remainder**: Computes the remainder when dividing the first number by the second.
- **Power**: Calculates the first number raised to the power of the second.

## Prerequisites

- **Python 3.x**: Make sure Python is installed. [Download Python](https://www.python.org/downloads/)
- **pip**: The package installer for Python should be available. It typically comes with Python installations.

## Requirements

- **Flask**: Install Flask by running:
  ```bash
  pip install Flask
  ```

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_folder>
   ```

2. **Install Requirements**:
   Install Flask if not already installed:
   ```bash
   pip install Flask
   ```

3. **Run the Application**:
   Start the Flask server:
   ```bash
   python <filename>.py
   ```
   The application will be available at `http://127.0.0.1:5000`.

## Using the Program

### Endpoint: `/Calculator/<float:n1>/<float:n2>`

**Description**: This endpoint performs six arithmetic operations on two numbers (`n1` and `n2`) and returns the results in JSON format.

**Parameters**:
- `n1` (float): The first number
- `n2` (float): The second number

### Example Usage

#### Sample Input
To perform calculations with `n1 = 10.5` and `n2 = 2.5`, send a `GET` request to:
```http
GET http://127.0.0.1:5000/Calculator/10.5/2.5
```

#### Sample Output
The server will return JSON output with the results of all operations:
```json
{
    "add": 13.0,
    "div": 4.2,
    "Multiply": 26.25,
    "remainder": 0.5,
    "sub": 8.0,
    "Power": 525.21875
}
```

## Error Handling

- **Division by Zero**: Attempting to divide by zero will result in an error response, as dividing by zero is undefined.

## Contributors

- **Addition**: Implemented by **Rajesh**
- **Division**: Implemented by **Rajesh**
- **Subtraction**: Implemented by **Reshma**
- **Multiplication**: Implemented by **Kalyan**
- **Remainder**: Implemented by **Manisha**
- **Power**: Implemented by the development team
