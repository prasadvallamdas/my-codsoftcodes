import tkinter as tk

class ToDoListApp:
    def __init__(self, master):
        self.master = master
        self.tasks = []

        self.create_widgets()

    def create_widgets(self):
        self.task_var = tk.StringVar()
        self.task_entry = tk.Entry(self.master, textvariable=self.task_var)
        self.task_entry.pack()

        self.add_button = tk.Button(self.master, text="Add Task", command=self.add_task)
        self.add_button.pack()

        self.tasks_listbox = tk.Listbox(self.master)
        self.tasks_listbox.pack()

        self.delete_button = tk.Button(self.master, text="Delete Task", command=self.delete_task)
        self.delete_button.pack()

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.task_var.set("")
            self.tasks_listbox.delete(0, tk.END)
            for task in self.tasks:
                self.tasks_listbox.insert(tk.END, task)

    def delete_task(self):
        selected_task = self.tasks_listbox.get(tk.ACTIVE)
        if selected_task:
            self.tasks.remove(selected_task)
            self.tasks_listbox.delete(tk.ACTIVE)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ToDo List")
    app = ToDoListApp(root)
    root.mainloop()