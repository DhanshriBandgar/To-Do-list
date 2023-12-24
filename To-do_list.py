import tkinter as tk
from tkinter import messagebox
from datetime import datetime

counter = 1  # Counter for numbering tasks

def add_task():
    global counter
    task = entry.get()
    if task:
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        task_with_time = f"{counter}. {current_date} {current_time} - {task}"
        listbox.insert(tk.END, task_with_time)
        entry.delete(0, tk.END)
        counter += 1  # Increment the counter for the next task
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    selected_task_index = listbox.curselection()
    if selected_task_index:
        listbox.delete(selected_task_index)
    else:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    selected_task_index = listbox.curselection()
    new_task = entry.get()
    if selected_task_index and new_task:
        current_time = datetime.now().strftime("%H:%M:%S")
        current_date = datetime.now().strftime("%Y-%m-%d")
        updated_task = f"{counter}. {current_date} {current_time} - {new_task}"
        listbox.delete(selected_task_index)
        listbox.insert(selected_task_index, updated_task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please select a task to update and enter a new task.")

def clear_tasks():
    global counter
    listbox.delete(0, tk.END)
    counter = 1  # Reset the counter when clearing all tasks

def exit_app():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("800x500")  # Set window size

# Create GUI components
page_bg_color = "#FFA500"  # Orange color for the page background
root.configure(bg=page_bg_color)  # Background color for the page

title_label = tk.Label(root, text="TO-DO List", font=("Helvetica", 24), bg=page_bg_color, fg="white")  # White color for the title
label_bg_color = "#757575"  # Green color for the label background
label = tk.Label(root, width=15, text="Enter Task:", font=("Helvetica", 12), bg=label_bg_color, fg="white")
entry = tk.Entry(root, width=30, font=("Helvetica", 12))
add_button = tk.Button(root, width=30, text="Add Task", command=add_task, bg="#4caf50", fg="white", font=("Helvetica", 12))
delete_button = tk.Button(root, width=30, text="Delete Task", command=delete_task, bg="#f44336", fg="white", font=("Helvetica", 12))
update_button = tk.Button(root, width=30, text="Update Task", command=update_task, bg="#2196f3", fg="white", font=("Helvetica", 12))
clear_button = tk.Button(root, width=30, text="Clear All", command=clear_tasks, bg="#ff9800", fg="white", font=("Helvetica", 12))
exit_button = tk.Button(root, width=30, text="Exit", command=exit_app, bg="#000080", fg="white", font=("Helvetica", 12))
listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=80, height=20, font=("Helvetica", 12))  # Increased width and height

# Place GUI components on the grid
title_label.grid(row=0, column=0, columnspan=4, pady=20)
label.grid(row=1, column=1, pady=10, sticky="E")
entry.grid(row=1, column=2, pady=10)
add_button.grid(row=2, column=2, pady=10)
delete_button.grid(row=3, column=2, pady=10)
update_button.grid(row=4, column=2, pady=10)
clear_button.grid(row=5, column=2, pady=10, padx=10)
exit_button.grid(row=6, column=2, pady=10, padx=10)
listbox.grid(row=1, column=3, rowspan=6, padx=20, pady=10)

# Start the main loop
root.mainloop()
