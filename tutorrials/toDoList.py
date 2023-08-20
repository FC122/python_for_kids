import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
    task_entry.delete(0, tk.END)

def delete_task():
    try:
        listbox.delete(listbox.curselection())
    except:
        messagebox.showinfo("Warning", "You must select a task to delete")

def complete_task():
Pčo0   v>aaaaaaaaaaaa   FF
        listbox.itemconfig(listbox.curselection(), fg="green")
    except:
        messagebox.showinfo("Warning", "You must select a task to mark as completed")

root = tk.Tk()

root.geometry("300x400")
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(pady=10)

listbox = tk.Listbox(
    frame,
    width=50,
    height=15,
    bg="SystemButtonFace",
    bd=0,
    fg="#464646",
    highlightthickness=0,
    selectbackground="#a6a6a6",
)
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

task_entry = tk.Entry(root, font=("Helvetica", 24))
task_entry.pack(pady=20)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=10)

delete_task_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_task_button.pack(pady=10)

complete_task_button = tk.Button(root, text="Complete Task", command=complete_task)
complete_task_button.pack(pady=10)

root.mainloop()
