import sqlite3
import os

# Define the path where the DB should be saved
db_path = os.path.join(os.path.dirname(__file__), "tasks.db")

# Connect and create the table
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL
)
""")

conn.commit()
conn.close()

print(f"✅ SQLite database created at: {db_path}")
