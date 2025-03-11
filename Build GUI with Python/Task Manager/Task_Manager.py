"""
Scenario 3: Task Manager with Task Details
Objective: Create an application where users can add tasks to a to-do list in the first window and view details about each task in a second window.
Requirements:
Window 1 (Task Manager):
Use ttk.Entry for entering the task description.
Use ttk.Button for adding the task to the list, and ttk.Listbox to display the added tasks.
Window 2 (Task Details): When the user selects a task in Window 1 and clicks a "View Details" button, Window 2 opens with detailed information about the selected task (e.g., task description, due date, status).
Use ttk.Label to display task details.
Include an option to mark tasks as complete.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import json
from datetime import datetime


# File path for saving tasks
TASKS_FILE = "tasks.json"


# Task Manager Window (Window 1)
class TaskManagerWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Task Manager")

        self.tasks = self.load_tasks()  # Load tasks from file
        self.selected_task = None

        # Task Entry and Add Button
        self.task_label = ttk.Label(self.root, text="Enter Task Description:")
        self.task_label.grid(row=0, column=0, padx=10, pady=10)

        self.task_entry = ttk.Entry(self.root, width=40)
        self.task_entry.grid(row=0, column=1, padx=10, pady=10)

        self.add_button = ttk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=2, padx=10, pady=10)

        # Listbox to display tasks
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # View Details Button
        self.view_button = ttk.Button(self.root, text="View Details", command=self.view_task_details)
        self.view_button.grid(row=2, column=0, columnspan=3, pady=10)

        # Delete Task Button
        self.delete_button = ttk.Button(self.root, text="Delete Task", command=self.delete_task)
        self.delete_button.grid(row=3, column=0, columnspan=3, pady=10)

        # Update the task listbox initially with loaded tasks
        self.update_task_listbox()

    def add_task(self):
        """Add a new task to the task list."""
        task_description = self.task_entry.get().strip()

        if task_description == "":
            messagebox.showerror("Input Error", "Task description cannot be empty!")
            return

        task = {
            "description": task_description,
            "due_date": None,  # None initially, can be updated later
            "status": "Pending",
        }

        self.tasks.append(task)

        # Save the updated tasks to file
        self.save_tasks()

        # Update the task listbox
        self.update_task_listbox()

        # Clear the task entry field
        self.task_entry.delete(0, tk.END)

    def update_task_listbox(self):
        """Update the task listbox with current tasks."""
        self.task_listbox.delete(0, tk.END)

        for i, task in enumerate(self.tasks):
            self.task_listbox.insert(tk.END, f"{i + 1}. {task['description']} - {task['status']}")

    def view_task_details(self):
        """Open the Task Details window for the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.selected_task = self.tasks[selected_index]
            TaskDetailsWindow(self.root, self.selected_task, self.update_task_listbox, self.save_tasks)
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to view its details.")

    def delete_task(self):
        """Delete the selected task."""
        try:
            selected_index = self.task_listbox.curselection()[0]
            task = self.tasks[selected_index]

            # Confirm deletion
            confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete the task:\n{task['description']}?")
            if confirm:
                del self.tasks[selected_index]  # Remove task from the list
                self.save_tasks()  # Save updated tasks to the file
                self.update_task_listbox()  # Update the listbox
        except IndexError:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def save_tasks(self):
        """Save the current list of tasks to a file."""
        with open(TASKS_FILE, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def load_tasks(self):
        """Load tasks from a file."""
        try:
            with open(TASKS_FILE, "r") as file:
                tasks = json.load(file)
            return tasks
        except (FileNotFoundError, json.JSONDecodeError):
            return []  # Return an empty list if no tasks file exists or file is corrupt


# Task Details Window (Window 2)
class TaskDetailsWindow:
    def __init__(self, root, task, update_task_listbox, save_tasks):
        self.root = root
        self.task = task
        self.update_task_listbox = update_task_listbox
        self.save_tasks = save_tasks

        # Create a new Toplevel window for Task Details
        self.details_window = tk.Toplevel(self.root)
        self.details_window.title("Task Details")

        # Task Description
        self.description_label = ttk.Label(self.details_window, text="Description:")
        self.description_label.grid(row=0, column=0, padx=10, pady=10)
        self.description_value = ttk.Label(self.details_window, text=self.task["description"])
        self.description_value.grid(row=0, column=1, padx=10, pady=10)

        # Due Date
        self.due_date_label = ttk.Label(self.details_window, text="Due Date:")
        self.due_date_label.grid(row=1, column=0, padx=10, pady=10)

        self.due_date_entry = ttk.Entry(self.details_window, width=20)
        self.due_date_entry.grid(row=1, column=1, padx=10, pady=10)
        self.due_date_entry.insert(0, self.task["due_date"] if self.task["due_date"] else "")

        # Status
        self.status_label = ttk.Label(self.details_window, text="Status:")
        self.status_label.grid(row=2, column=0, padx=10, pady=10)

        self.status_value = ttk.Label(self.details_window, text=self.task["status"])
        self.status_value.grid(row=2, column=1, padx=10, pady=10)

        # Mark Task as Complete Button
        self.mark_complete_button = ttk.Button(self.details_window, text="Mark as Complete", command=self.mark_task_complete)
        self.mark_complete_button.grid(row=3, column=0, columnspan=2, pady=10)

        # Save and Close Button
        self.save_button = ttk.Button(self.details_window, text="Save & Close", command=self.save_and_close)
        self.save_button.grid(row=4, column=0, columnspan=2, pady=10)

    def mark_task_complete(self):
        """Mark the selected task as complete."""
        self.task["status"] = "Complete"
        self.status_value.config(text=self.task["status"])
        self.update_task_listbox()

    def save_and_close(self):
        """Save the changes and close the Task Details window."""
        due_date = self.due_date_entry.get().strip()
        self.task["due_date"] = due_date if due_date else None
        self.update_task_listbox()

        # Save updated tasks to file
        self.save_tasks()

        self.details_window.destroy()


# Main Application
if __name__ == "__main__":
    root = tk.Tk()
    task_manager_window = TaskManagerWindow(root)
    root.mainloop()

