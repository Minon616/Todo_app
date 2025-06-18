import os
import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ['DB_HOST'],
            user=os.environ['DB_USER'],
            password=os.environ['DB_PASSWORD'],
            database=os.environ['DB_NAME']
        )
        return connection
    except mysql.connector.Error as err:
        print("❌ DB Connection Error:", err)
        raise
