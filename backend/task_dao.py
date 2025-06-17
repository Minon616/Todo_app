from backend.sql_connection import get_connection

# 1. Add a new task
def add_task(title):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO tasks (task_title) VALUES (%s)"
    cursor.execute(query, (title,))
    conn.commit()
    conn.close()
    print("✅ Task added.")

# 2. Remove a task by ID
def remove_task(task_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM tasks WHERE task_id = %s"
    cursor.execute(query, (task_id,))
    conn.commit()
    conn.close()
    print(f"✅ Task {task_id} removed.")

# 3. Display all tasks
def display_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM tasks"
    cursor.execute(query)
    tasks = cursor.fetchall()
    conn.close()

    if not tasks:
        print("📭 No tasks found.")
    else:
        print("📝 Your Tasks:")
        for task in tasks:
            print(f"[{task[0]}] {task[1]}")

# 4. Delete all tasks
def delete_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    query = "DELETE FROM tasks"
    cursor.execute(query)
    conn.commit()
    conn.close()
    print("🗑️ All tasks deleted.")
