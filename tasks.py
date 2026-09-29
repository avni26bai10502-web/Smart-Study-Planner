import database
import validation


def add_task():
    name = input("Enter task name: ").strip()
    subject = input("Enter subject: ").strip()
    deadline = input("Enter deadline (DD-MM-YYYY): ").strip()
    priority = input("Enter priority (High/Medium/Low): ").strip()

    if not validation.validate_text(name):
        print("Task name cannot be empty.")
        return

    if not validation.validate_text(subject):
        print("Subject cannot be empty.")
        return

    if not validation.validate_date(deadline):
        print("Invalid date. Use DD-MM-YYYY.")
        return

    if not validation.validate_priority(priority):
        print("Priority must be High, Medium, or Low.")
        return

    priority = priority.capitalize()

    database.add_task(
        name,
        subject,
        deadline,
        priority
    )

    print("Task added successfully!")


def view_tasks():
    tasks = database.get_tasks()

    if not tasks:
        print("No tasks added yet.")
        return

    print("\n========== YOUR TASKS ==========")

    for task in tasks:

        task_id, name, subject, deadline, priority, status = task

        print("\n------------------------------")
        print(f"ID       : {task_id}")
        print(f"Name     : {name}")
        print(f"Subject  : {subject}")
        print(f"Deadline : {deadline}")
        print(f"Priority : {priority}")
        print(f"Status   : {status}")


def complete_task():
    tasks = database.get_tasks()

    if not tasks:
        print("No tasks to complete.")
        return

    view_tasks()

    task_id = input("\nEnter task ID to complete: ")

    if not validation.validate_id(task_id):
        print("Please enter a valid ID.")
        return

    updated = database.complete_task(int(task_id))

    if updated:
        print("Task marked as completed!")
    else:
        print("Task ID not found.")


def delete_task():
    tasks = database.get_tasks()

    if not tasks:
        print("No tasks to delete.")
        return

    view_tasks()

    task_id = input("\nEnter task ID to delete: ")

    if not validation.validate_id(task_id):
        print("Please enter a valid ID.")
        return

    deleted = database.delete_task(int(task_id))

    if deleted:
        print("Task deleted successfully!")
    else:
        print("Task ID not found.")