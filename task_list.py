# task_list.py
import tkinter as tk
from tkinter import messagebox
from db import get_all_tasks, mark_done

def open_task_list():
    window = tk.Toplevel()
    window.title("Task List")
    window.geometry("500x400")
    window.configure(bg="white",fg="black")

    heading = tk.Label(window, text="All Tasks", font=("Arial", 15, "bold"), bg="white")
    heading.pack(pady=10)

    tasks = get_all_tasks()

    if not tasks:
        tk.Label(window, text="No tasks found.", font=("Arial", 12), bg="white").pack(pady=20)
        return

    for task in tasks:
        frame = tk.Frame(window, borderwidth=1, relief="solid", pady=5, padx=5, bg="white")
        frame.pack(fill="x", padx=10, pady=5)

        info = f"ID: {task[0]} | Title: {task[1]} | Due: {task[2]} | Status: {task[3]}"
        tk.Label(frame, text=info, font=("Arial", 10), bg="white", anchor="w", justify="left").pack(anchor="w")

        if task[3] == "Pending":
            def mark_done_closure(tid=task[0], w=window):
                mark_done(tid)
                messagebox.showinfo("Updated", f"Task {tid} marked as done.")
                w.destroy()
                open_task_list()  # Reload tasks

            tk.Button(frame, tex
