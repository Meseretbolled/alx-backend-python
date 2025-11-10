#!/usr/bin/python3
"""
0-stream_users.py

A generator that streams rows from the users.db database one by one
"""

import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "users.db")

def stream_users():
    """Generator function to yield users one by one from the database"""
    if not os.path.exists(DB_PATH):
        print(f"❌ Database not found at {DB_PATH}")
        return

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # allows accessing columns by name
    cur = conn.cursor()

    cur.execute("SELECT * FROM user_data;")
    for row in cur:
        yield dict(row)  # yield each row as a dictionary

    conn.close()
