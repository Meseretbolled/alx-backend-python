import sqlite3
from functools import wraps

def handle_connection(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        print("[INFO] Database connection opened.")
        try:
            result = func(conn, *args, **kwargs)
            return result
        finally:
            conn.close()
            print("[INFO] Database connection closed.")
    return wrapper
