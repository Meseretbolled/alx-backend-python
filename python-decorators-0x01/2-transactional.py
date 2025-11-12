from functools import wraps

def manage_transaction(func):
    @wraps(func)
    def wrapper(conn, *args, **kwargs):
        try:
            result = func(conn, *args, **kwargs)
            conn.commit()
            print("[INFO] Transaction committed successfully.")
            return result
        except Exception as e:
            conn.rollback()
            print("[ERROR] Transaction rolled back.", e)
            raise
    return wrapper
