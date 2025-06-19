import mysql.connector
import os

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ.get("DB_HOST", "localhost"),
            user=os.environ.get("DB_USER", "root"),
            password=os.environ.get("DB_PASSWORD", "Minon#616747"),
            database=os.environ.get("DB_NAME", "todo")
        )
        return connection
    except mysql.connector.Error as err:
        print("❌ DB Connection Error:", err)
        raise
