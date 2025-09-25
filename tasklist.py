import json

tasks = json.load(open("task.json"))

def add_task(title, description, completed):
    tasks["tasks"].append({"title": title, "description": description, "completed": completed})
    json.dump(tasks, open("task.json", "w"))

def remove_task(title):
    tasks["tasks"] = [task for task in tasks["tasks"] if task["title"] != title]
    json.dump(tasks, open("task.json", "w"))

def mark_task_as_completed(title):
    tasks["tasks"] = [task for task in tasks["tasks"] if task["title"] == title]
    tasks["tasks"][0]["completed"] = "True"
    json.dump(tasks, open("task.json", "w"))

def list_tasks():
    return tasks["tasks"]

def save_tasks():
    json.dump(tasks, open("task.json", "w"))

if __name__ == "__main__":
    print("Welcome to the task list!") 
    while True:
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. List tasks")
        print("5. Save tasks")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_task(input("Enter the title of the task: "), input("Enter the description of the task: "), input("Enter the completed status of the task: ")) 
        elif choice == "2":
            remove_task(input("Enter the title of the task to remove: "))
        elif choice == "3":
            mark_task_as_completed(input("Enter the title of the task to mark as completed: "))
        elif choice == "4":
            print(list_tasks())
        elif choice == "5":
            print(save_tasks())
        elif choice == "6":
            break