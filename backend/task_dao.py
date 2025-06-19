from backend.sql_connection import get_connection

# -------------------------------
# Add a task
# -------------------------------
def add_task(title):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tasks (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()

# -------------------------------
# Remove a task by ID
# -------------------------------
def remove_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()

# -------------------------------
# Display all tasks
# -------------------------------
def display_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM tasks")
    results = cursor.fetchall()
    conn.close()
    return results

# -------------------------------
# Delete all tasks
# -------------------------------
def delete_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks")
    conn.commit()
    conn.close()
