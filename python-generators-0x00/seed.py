#!/usr/bin/python3
"""
seed.py

Seed the users.db SQLite database from user_data.csv
"""

import sqlite3
import csv
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")
CSV_PATH = os.path.join(os.path.dirname(__file__), "user_data.csv")

def seed_database() -> None:
    """Seed the users.db database from user_data.csv"""
    
    # Check if CSV exists
    if not os.path.exists(CSV_PATH):
        print(f"❌ CSV file not found: {CSV_PATH}")
        return

    # Connect to database (creates it if not exists)
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    print(f"✅ Connected to database: {DB_PATH}")

    # Drop table if it exists
    cur.execute("DROP TABLE IF EXISTS user_data;")
    print("✅ Dropped existing table if it existed")

    # Create table
    cur.execute("""
        CREATE TABLE user_data (
            user_id TEXT PRIMARY KEY,
            name TEXT,
            email TEXT,
            age INTEGER
        );
    """)
    print("✅ Created table user_data")

    # Insert CSV data into table
    with open(CSV_PATH, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        rows_inserted = 0
        for row in reader:
            cur.execute("""
                INSERT INTO user_data (user_id, name, email, age)
                VALUES (?, ?, ?, ?)
            """, (row["user_id"], row["name"], row["email"], int(row["age"])))
            rows_inserted += 1

    conn.commit()
    conn.close()
    print(f"✅ Database seeded successfully with {rows_inserted} rows!")

if __name__ == "__main__":
    seed_database()
