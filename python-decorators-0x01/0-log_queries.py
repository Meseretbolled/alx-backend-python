import sqlite3
from functools import wraps
from datetime import datetime  # For timestamp

def log_queries(func):
    """Decorator to log SQL queries before executing them"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Extract the query argument from function call
        query = kwargs.get('query') if 'query' in kwargs else args[0] if args else ''
        print(f"[{datetime.now()}] Executing SQL query: {query}")
        return func(*args, **kwargs)
    return wrapper

@log_queries
def fetch_all_users(query):
    # Use connect explicitly
    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

if __name__ == "__main__":
    users = fetch_all_users(query="SELECT * FROM users")
    print(users)
