import tkinter as tk
from tkinter import messagebox

# Función para agregar tarea
def agregar_tarea():
    tarea = entry_tarea.get()
    if tarea != "":
        lista_tareas.insert(tk.END, tarea)
        entry_tarea.delete(0, tk.END)  # Limpiar el campo de entrada
    else:
        messagebox.showwarning("Advertencia", "Por favor, ingresa una tarea.")

# Función para marcar tarea como completada
def marcar_completada():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        if tarea_seleccionada:
            tarea = lista_tareas.get(tarea_seleccionada)
            lista_tareas.delete(tarea_seleccionada)
            lista_tareas.insert(tk.END, tarea + " (Completada)")
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para eliminar tarea
def eliminar_tarea():
    try:
        tarea_seleccionada = lista_tareas.curselection()
        if tarea_seleccionada:
            lista_tareas.delete(tarea_seleccionada)
        else:
            messagebox.showwarning("Advertencia", "Por favor, selecciona una tarea.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Crear la ventana principal
root = tk.Tk()
root.title("Lista de Tareas")

# Crear campo de entrada para nueva tarea
entry_tarea = tk.Entry(root, width=30)
entry_tarea.pack(pady=10)

# Botón para agregar tarea
boton_agregar = tk.Button(root, text="Añadir Tarea", width=20, command=agregar_tarea)
boton_agregar.pack(pady=5)

# Crear la lista para mostrar las tareas
lista_tareas = tk.Listbox(root, height=10, width=50)
lista_tareas.pack(pady=10)

# Botón para marcar tarea como completada
boton_completada = tk.Button(root, text="Marcar como Completada", width=20, command=marcar_completada)
boton_completada.pack(pady=5)

# Botón para eliminar tarea
boton_eliminar = tk.Button(root, text="Eliminar Tarea", width=20, command=eliminar_tarea)
boton_eliminar.pack(pady=5)

# Ejecutar la aplicación
root.mainloop()
