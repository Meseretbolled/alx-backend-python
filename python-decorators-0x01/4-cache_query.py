import sqlite3
import functools

query_cache = {}

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

def cache_query(func):
    """Decorator to cache query results"""
    @functools.wraps(func)
    def wrapper(conn, *args, **kwargs):
        query = kwargs.get("query") or (args[1] if len(args) > 1 else "")
        if query in query_cache:
            print(f"[CACHE] Returning cached result for: {query}")
            return query_cache[query]
        result = func(conn, *args, **kwargs)
        query_cache[query] = result
        print(f"[CACHE] Stored new cache for: {query}")
        return result
    return wrapper

@with_db_connection
@cache_query
def fetch_users_with_cache(conn, query):
    cursor = conn.cursor()
    cursor.execute(query)
    return cursor.fetchall()

if __name__ == "__main__":
    # First call caches the result
    users = fetch_users_with_cache(query="SELECT * FROM users")
    # Second call uses cached result
    users_again = fetch_users_with_cache(query="SELECT * FROM users")
