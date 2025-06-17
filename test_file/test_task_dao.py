import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from backend.task_dao import add_task, remove_task, display_tasks, delete_all_tasks

def menu():
    while True:
        print("\n=== TODO MENU ===")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Display All Tasks")
        print("4. Delete All Tasks")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            add_task(title)
        elif choice == '2':
            task_id = input("Enter task ID to remove: ")
            if task_id.isdigit():
                remove_task(int(task_id))
            else:
                print("⚠️ Invalid ID.")
        elif choice == '3':
            display_tasks()
        elif choice == '4':
            confirm = input("Are you sure you want to delete ALL tasks? (y/n): ")
            if confirm.lower() == 'y':
                delete_all_tasks()
        elif choice == '5':
            print("👋 Exiting...")
            break
        else:
            print("❌ Invalid choice. Try again.")

menu()
