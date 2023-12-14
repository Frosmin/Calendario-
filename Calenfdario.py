import tkinter as tk
from tkinter import messagebox

def agregar_actividad(nombre, tarea, dia):
    # Validar que se haya ingresado un nombre, una tarea y un día
    if nombre and tarea and dia:
        # Obtener el índice de la columna correspondiente al día ingresado
        dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
        try:
            columna = dias_semana.index(dia)
        except ValueError:
            messagebox.showerror('Error', 'Día inválido')
            return

        # Agregar la actividad a la tabla
        tabla[columna].append((nombre, tarea))
        # Actualizar la etiqueta de la actividad en la tabla
        label_actividad = tk.Label(ventana, text=f'{nombre}: {tarea}')
        label_actividad.grid(row=len(tabla[columna])+1, column=columna)

        messagebox.showinfo('Éxito', 'Actividad agregada correctamente')
    else:
        messagebox.showerror('Error', 'Debes ingresar un nombre, una tarea y un día')

# Crear la ventana principal
ventana = tk.Tk()
ventana.title('Tabla Semanal')

# Crear la tabla vacía
tabla = [[] for _ in range(7)]

# Crear los encabezados de los días de la semana
dias_semana = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
for i, dia in enumerate(dias_semana):
    label_dia = tk.Label(ventana, text=dia, relief=tk.RAISED, padx=10, pady=5)
    label_dia.grid(row=0, column=i, sticky="nsew")

# Crear las filas de la tabla
for fila in range(6):
    for columna in range(7):
        # Asignar un color diferente a cada celda de la tabla
        if fila % 2 == 0:
            color = 'lightgray'
        else:
            color = 'white'
        label_actividad = tk.Label(ventana, text='', relief=tk.SOLID, padx=10, pady=5, bg=color)
        label_actividad.grid(row=fila+1, column=columna, sticky="nsew")

# Crear los campos de entrada para el nombre, la tarea y el día
label_nombre = tk.Label(ventana, text='Nombre:', relief=tk.RAISED, padx=10, pady=5)
label_nombre.grid(row=7, column=0, sticky="nsew")
entry_nombre = tk.Entry(ventana)
entry_nombre.grid(row=7, column=1, sticky="nsew")

label_tarea = tk.Label(ventana, text='Tarea:', relief=tk.RAISED, padx=10, pady=5)
label_tarea.grid(row=7, column=2, sticky="nsew")
entry_tarea = tk.Entry(ventana)
entry_tarea.grid(row=7, column=3, sticky="nsew")

label_dia = tk.Label(ventana, text='Día:', relief=tk.RAISED, padx=10, pady=5)
label_dia.grid(row=7, column=4, sticky="nsew")
entry_dia = tk.Entry(ventana)
entry_dia.grid(row=7, column=5, sticky="nsew")

# Crear el botón para agregar actividades
boton_agregar = tk.Button(ventana, text='Agregar actividad', command=lambda: agregar_actividad(entry_nombre.get(), entry_tarea.get(), entry_dia.get()), relief=tk.RAISED, padx=10, pady=5)
boton_agregar.grid(row=7, column=6, sticky="nsew")

# Configurar el sistema de rejilla para que las celdas se expandan
for i in range(8):
    ventana.grid_columnconfigure(i, weight=1)
for i in range(8):
    ventana.grid_rowconfigure(i, weight=1)

# Iniciar el bucle de eventos de la ventana
ventana.mainloop()
