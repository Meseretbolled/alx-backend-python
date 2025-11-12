import sqlite3
from functools import wraps

def log_queries(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"[LOG] Executed function: {func.__name__}")
        return result
    return wrapper
