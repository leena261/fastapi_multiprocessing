

## Introduction

This is a FastAPI project.

## Installation

1. **Clone the repository**

    ```bash
    git clone https://github.com/leena261/fastapi_multiprocessing.git
    cd fastapi_multiprocessing
    ```

2. **Create and activate a virtual environment**

    ```bash
    python3 -m venv env
    source env/bin/activate
    ```

3. **Install the dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Quick Start

1. **Run the FastAPI server**

    ```bash
    uvicorn app.main:app --reload
    ```

2. **Open your browser and navigate to**

    ```
    http://127.0.0.1:8000/docs
    ```

    You will see the automatic interactive API documentation (provided by Swagger UI).

## Usage

### Example Endpoint

- **POST** `/add_process`
    


## API Documentation

FastAPI automatically generates interactive API documentation for you. You can access it at:

- **Swagger UI**: `http://127.0.0.1:8000/docs`

## Running Tests

To run tests, use `pytest`:

1. **Install test dependencies**

    ```bash
    pip install -r requirements.txt
    ```

2. **Run the tests**

    ```bash
    pytest
    ```
---

