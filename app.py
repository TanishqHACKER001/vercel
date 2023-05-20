from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, Flask!'


@app.route('/tasks')
def tasks():
    # Retrieve task data from a database or other data source
    tasks = [...]
    return render_template('tasks.html', tasks=tasks)


tasks = []

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {"title": title, "description": description, "completed": False}
    tasks.append(task)
    print("Task added successfully!")

def update_task():
    display_tasks()
    task_index = int(input("Enter the index of the task you want to update: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index!")
        return

    new_title = input("Enter new title (leave blank to keep the existing title): ")
    new_description = input("Enter new description (leave blank to keep the existing description): ")

    if new_title:
        tasks[task_index]["title"] = new_title
    if new_description:
        tasks[task_index]["description"] = new_description

    print("Task updated successfully!")

def delete_task():
    display_tasks()
    task_index = int(input("Enter the index of the task you want to delete: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index!")
        return

    del tasks[task_index]
    print("Task deleted successfully!")

def mark_task_as_completed():
    display_tasks()
    task_index = int(input("Enter the index of the task you want to mark as completed: "))
    if task_index < 0 or task_index >= len(tasks):
        print("Invalid task index!")
        return

    tasks[task_index]["completed"] = True
    print("Task marked as completed!")

def display_tasks():
    print("Tasks:")
    for index, task in enumerate(tasks):
        print(f"{index}: {task['title']} - {task['description']} [Completed: {task['completed']}]")
    print()

def main():
    while True:
        print("To-Do List Application")
        print("1. Add Task")
        print("2. Update Task")
        print("3. Delete Task")
        print("4. Mark Task as Completed")
        print("5. Display Tasks")
        print("6. Quit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            update_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            mark_task_as_completed()
        elif choice == "5":
            display_tasks()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
   
    app.run()
