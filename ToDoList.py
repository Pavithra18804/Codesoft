import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        tasks.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        all_tasks.append(task)
    else:
        messagebox.showwarning("Warning", "Please enter a task!")

def remove_task():
    try:
        index = tasks.curselection()[0]
        task = tasks.get(index)
        tasks.delete(index)
        all_tasks.remove(task)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def delete_all_tasks():
    confirmed = messagebox.askyesno("Confirm", "Are you sure you want to delete all tasks?")
    if confirmed:
        tasks.delete(0, tk.END)
        all_tasks.clear()

def search_tasks():
    search_text = search_entry.get().strip().lower()
    tasks.delete(0, tk.END)
    if search_text:
        for task in all_tasks:
            if search_text in task.lower():
                tasks.insert(tk.END, task)
    else:
        for task in all_tasks:
            tasks.insert(tk.END, task)

def exit_app():
    root.destroy()

# Sample tasks (for demonstration)
all_tasks = ["Task 1", "Task 2", "Task 3"]

# Create the main window
root = tk.Tk()
root.title("To-Do List Application")

# Task Entry
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

# Add Task Button
add_button = tk.Button(root, text="Add Task", command=add_task, bg="Turquoise", fg="white")
add_button.pack()

# Remove Task Button
remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg="#E0b0FF", fg="white")
remove_button.pack()

# Delete All Tasks Button
delete_all_button = tk.Button(root, text="Delete All Tasks", command=delete_all_tasks, bg="coral", fg="white")
delete_all_button.pack()

# Search Entry
search_entry = tk.Entry(root, width=50)
search_entry.pack(pady=10)

# Search Button
search_button = tk.Button(root, text="Search", command=search_tasks, bg="#800020", fg="white")
search_button.pack()

# Tasks Listbox
tasks = tk.Listbox(root, width=50)
tasks.pack(pady=10)

# Add sample tasks to the listbox
for task in all_tasks:
    tasks.insert(tk.END, task)

# Exit Button
exit_button = tk.Button(root, text="Exit", command=exit_app, bg="teal", fg="white")
exit_button.pack()

# Start the GUI main loop
root.mainloop()
