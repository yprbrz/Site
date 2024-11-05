
# Django Project with MongoDB Integration

This project demonstrates the integration of Django with MongoDB as the primary database. It includes steps to set up and populate MongoDB, interact with it through Django, and test the functionality of the project.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Database Setup](#database-setup)
- [Usage](#usage)
- [Populating the Database](#populating-the-database)

## Prerequisites

- Python 3.6+
- Django
- MongoDB
- Pymongo

## Installation

1. **Set up a virtual environment** (recommended):

    ```bash
    python -m venv env
    source env/bin/activate  # for macOS/Linux
    env\Scripts\activate  # for Windows
    ```

2. **Install project dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

3. **Install MongoDB dependencies**:

    ```bash
    pip install pymongo
    ```

## Database Setup

1. **Create a MongoDB database**:
    - If using a local MongoDB, start MongoDB on your machine.

2. **Configure MongoDB connection**

## Usage

1. **Run migrations**:

    ```bash
    python src/manage.py migrate
    ```

2. **Start the Django development server**:

    ```bash
    python src/manage.py runserver
    ```

3. **Visit the application** in your browser at `http://127.0.0.1:8000/`.

## Populating the Database

To populate the database with initial data, you can use a Django management command or an independent script.