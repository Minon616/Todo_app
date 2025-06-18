import os
import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host=os.environ['localhost'],
            user=os.environ['root'],
            password=os.environ['Minon#616747'],
            database=os.environ['todo']
        )
        return connection
    except mysql.connector.Error as err:
        print("❌ DB Connection Error:", err)
        raise
