SQL Row Streamer — Python Generator
 Objective

Create a Python generator that streams rows from an SQL database one by one using yield.

Setup Script: seed.py

This script sets up and seeds a MySQL database named ALX_prodev with sample user data.

Functions

connect_db() → Connects to the MySQL server.

create_database(connection) → Creates the ALX_prodev database if it doesn’t exist.

connect_to_prodev() → Connects to the ALX_prodev database.

create_table(connection) → Creates a table user_data with fields:

user_id (UUID, Primary Key, Indexed)

name (VARCHAR, NOT NULL)

email (VARCHAR, NOT NULL)

age (DECIMAL, NOT NULL)

insert_data(connection, data) → Populates the table from user_data.csv.

🧩 Test Script: 0-main.py

Runs all setup steps and confirms:

Database and table creation

Successful data insertion

Displays first 5 rows of the user_data table

Example Output
connection successful
Table user_data created successfully
Database ALX_prodev is present
[('00234e50-34eb-4ce2-94ec-26e3fa749796', 'Dan Altenwerth Jr.', 'Molly59@gmail.com', 67), ...]

📁 Files
├── 0-main.py
├── seed.py
├── user_data.csv
└── README.md

🐍 Requirements

Python 3.x

MySQL server

mysql-connector-python package

Install dependencies:

pip install mysql-connector-python
