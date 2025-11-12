import sqlite3
import functools
import time

def with_db_connection(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        conn = sqlite3.connect("users.db")
        print("[INFO] Database connection opened.")
        try:
            return func(conn, *args, **kwargs)
        finally:
            conn.close()
            print("[INFO] Database connection closed.")
    return wrapper

def retry_on_failure(retries=3, delay=1):
    """Decorator to retry function execution on failure"""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, retries+1):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    print(f"[RETRY] Attempt {attempt} failed: {e}")
                    time.sleep(delay)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@with_db_connection
@retry_on_failure(retries=3, delay=1)
def fetch_users_with_retry(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users")
    return cursor.fetchall()

if __name__ == "__main__":
    users = fetch_users_with_retry()
    print(users)
