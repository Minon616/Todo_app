import sqlite3
import os

def get_connection():
    try:
        # Create absolute path to the SQLite database inside the backend folder
        db_path = os.path.join(os.path.dirname(__file__), "tasks.db")
        connection = sqlite3.connect(db_path)
        return connection
    except sqlite3.Error as err:
        print("❌ DB Connection Error:", err)
        raise
