import sys
import os

# Add the project root (Todo_app) to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.sql_connection import get_connection

conn = get_connection()

if conn:
    print("✅ Database connection successful!")
    conn.close()
else:
    print("❌ Failed to connect to the database.")
