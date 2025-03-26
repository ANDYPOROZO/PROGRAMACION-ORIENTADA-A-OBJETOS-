import tkinter as tk
from tkinter import messagebox

class TaskManagerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Gestor de Tareas")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        # Entrada de nueva tarea
        self.entry = tk.Entry(root, width=40)
        self.entry.pack(pady=10)
        self.entry.focus()

        # Botones
        self.btn_frame = tk.Frame(root)
        self.btn_frame.pack(pady=5)

        self.add_btn = tk.Button(self.btn_frame, text="Añadir", command=self.add_task)
        self.add_btn.grid(row=0, column=0, padx=5)

        self.complete_btn = tk.Button(self.btn_frame, text="Marcar como completada", command=self.complete_task)
        self.complete_btn.grid(row=0, column=1, padx=5)

        self.delete_btn = tk.Button(self.btn_frame, text="Eliminar", command=self.delete_task)
        self.delete_btn.grid(row=0, column=2, padx=5)

        # Lista de tareas
        self.task_listbox = tk.Listbox(root, width=50, height=15, selectmode=tk.SINGLE)
        self.task_listbox.pack(pady=10)

        # Atajos de teclado
        root.bind('<Return>', lambda event: self.add_task())
        root.bind('<c>', lambda event: self.complete_task())
        root.bind('<C>', lambda event: self.complete_task())
        root.bind('<d>', lambda event: self.delete_task())
        root.bind('<D>', lambda event: self.delete_task())
        root.bind('<Delete>', lambda event: self.delete_task())
        root.bind('<Escape>', lambda event: root.quit())

    def add_task(self):
        task = self.entry.get().strip()
        if task:
            self.task_listbox.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Campo vacío", "Escriba una tarea antes de añadirla.")

    def complete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task_text = self.task_listbox.get(index)
            if not task_text.startswith("[✓] "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "[✓] " + task_text)
        else:
            messagebox.showinfo("Selección requerida", "Seleccione una tarea para marcarla como completada.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            self.task_listbox.delete(selected[0])
        else:
            messagebox.showinfo("Selección requerida", "Seleccione una tarea para eliminarla.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TaskManagerApp(root)
    root.mainloop()
