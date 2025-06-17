import mysql.connector

def get_connection():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Minon#616747",
            database="todo"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"❌ Error: {err}")
        return None
