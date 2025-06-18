import sys
import os
from flask import Flask, request, jsonify
#from flask_cors import CORS
from flask_cors import CORS


# Add parent directory to path for imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import your modules
from backend.task_dao import add_task, remove_task, display_tasks, delete_all_tasks
from backend.sql_connection import get_connection

# Initialize Flask app and enable CORS
app = Flask(__name__)
CORS(app)

# -------------------------------
# Add Task (Create)
# -------------------------------
@app.route('/tasks', methods=['POST'])
def api_add_task():
    data = request.get_json()
    title = data.get('task_title')  # 🔑 Match frontend JS key

    if not title:
        return jsonify({'error': 'task_title is required'}), 400

    try:
        add_task(title)
        return jsonify({'message': 'Task added'}), 201
    except Exception as e:
        print("❌ Error in add_task:", e)
        return jsonify({'error': str(e)}), 500

# -------------------------------
# Get All Tasks (Read)
# -------------------------------
@app.route('/tasks', methods=['GET'])
def api_get_tasks():
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        results = cursor.fetchall()
        tasks = [{"id": row[0], "title": row[1]} for row in results]
        conn.close()
        return jsonify(tasks)
    except Exception as e:
        print("❌ Error in get_tasks:", e)
        return jsonify({"error": str(e)}), 500

# -------------------------------
# Delete One Task by ID (Delete)
# -------------------------------
@app.route('/tasks/<int:task_id>', methods=['DELETE'])
def api_delete_task(task_id):
    try:
        remove_task(task_id)
        return jsonify({'message': f'Task {task_id} deleted'})
    except Exception as e:
        print("❌ Error in delete_task:", e)
        return jsonify({'error': str(e)}), 500

# -------------------------------
# Delete All Tasks (Delete All)
# -------------------------------
@app.route('/tasks', methods=['DELETE'])
def api_delete_all_tasks():
    try:
        delete_all_tasks()
        return jsonify({'message': 'All tasks deleted'})
    except Exception as e:
        print("❌ Error in delete_all_tasks:", e)
        return jsonify({'error': str(e)}), 500

# -------------------------------
# Run the server
# -------------------------------
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

#update