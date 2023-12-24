



import tkinter as tk
from tkinter import messagebox
import random
import tkinter as tk
import random

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Función para manejar el evento de cierre de la ventana
def cerrar_ventana():
    ventana.destroy()

# Asociar el manejador de eventos al evento de cierre de la ventana
ventana.protocol("WM_DELETE_WINDOW", cerrar_ventana)

# Variable para controlar el turno del jugador
turno = "X"

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el valor de la casilla con el turno actual
        tablero[fila][columna] = turno

        # Actualizar el texto del botón
        botones[fila][columna].config(text=turno)

        # Verificar si hay un ganador
        if verificar_ganador(turno):
            messagebox.showinfo("Fin del juego", f"¡El jugador {turno} ha ganado!")
            reiniciar_juego()
        else:
            # Cambiar el turno al siguiente jugador
            turno = "O" if turno == "X" else "X"
            if turno == "O":
                jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True

    # Verificar columnas
    for columna in range(3):
        if [tablero[fila][columna] for fila in range(3)].count(jugador) == 3:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para reiniciar el juego
def reiniciar_juego():
    global turno, tablero

    # Reiniciar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Reiniciar los textos de los botones
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ")

    # Reiniciar el turno
    turno = "X"

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Función para manejar el evento de cierre de la ventana
def cerrar_ventana(event):
    ventana.destroy()

# Asociar el manejador de eventos al evento de cierre de la ventana
ventana.bind("<Destroy>", cerrar_ventana)

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna)
        fila_botones.append(boton)
    botones.append(fila_botones)

# Iniciar el juego
ventana.mainloop()

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el valor de la casilla con el turno actual
        tablero[fila][columna] = turno

        # Actualizar el texto del botón
        botones[fila][columna].config(text=turno)

        # Verificar si hay un ganador
        if verificar_ganador(turno):
            messagebox.showinfo("Fin del juego", f"¡El jugador {turno} ha ganado!")
            reiniciar_juego()
        else:
            # Cambiar el turno al siguiente jugador
            turno = "O" if turno == "X" else "X"
            if turno == "O":
                jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return True

    # Verificar columnas
    for columna in range(3):
        if [tablero[fila][columna] for fila in range(3)].count(jugador) == 3:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para reiniciar el juego
def reiniciar_juego():
    global turno, tablero

    # Reiniciar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Reiniciar los textos de los botones
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ")

    # Reiniciar el turno
    turno = "X"

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Crear botones del tablero
if __name__ == "__main__":
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title("Tres en Raya")

    # Crear tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Variable para controlar el turno del jugador
    turno = "X"

    # Función para manejar el clic en un botón del tablero
    def manejar_clic(fila, columna):
        global turno

        # Verificar si la casilla está vacía
        if tablero[fila][columna] == " ":
            # Actualizar el valor de la casilla con el turno actual
            tablero[fila][columna] = turno

            # Actualizar el texto del botón
            botones[fila][columna].config(text=turno)

            # Verificar si hay un ganador
            if verificar_ganador(turno):
                messagebox.showinfo("Fin del juego", f"¡El jugador {turno} ha ganado!")
                reiniciar_juego()
            else:
                # Cambiar el turno al siguiente jugador
                turno = "O" if turno == "X" else "X"
                if turno == "O":
                    jugar_computadora()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el valor de la casilla con el turno actual
        tablero[fila][columna] = turno

        # Actualizar el texto del botón
        botones[fila][columna].config(text=turno)

        # Verificar si hay un ganador
        if verificar_ganador(turno):
            messagebox.showinfo("Fin del juego", f"¡El jugador {turno} ha ganado!")
            reiniciar_juego()
        else:
            # Cambiar el turno al siguiente jugador
            turno = "O" if turno == "X" else "X"
            if turno == "O":
                jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador:
            return True

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para reiniciar el juego
def reiniciar_juego():
    global tablero, turno

    # Reiniciar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Reiniciar el turno
    turno = "X"

    # Reiniciar los textos de los botones
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ")

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)

        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)

        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    pass

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)

        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
# Ejecutar la ventana principal
ventana.mainloop()

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)

        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
ventana.mainloop()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el tablero
        tablero[fila][columna] = turno

        # Actualizar el texto y color del botón
        if turno == "X":
            botones[fila][columna].config(text=turno, fg="red")
        else:
            botones[fila][columna].config(text=turno, fg="blue")

        # Cambiar el turno
        turno = "O" if turno == "X" else "X"

        # Verificar si hay un ganador
        ganador = verificar_ganador(turno)
        if ganador:
            messagebox.showinfo("Fin del juego", f"¡El jugador {ganador} ha ganado!")
            reiniciar_juego()
        elif not hay_movimientos_disponibles():
            messagebox.showinfo("Fin del juego", "¡Empate!")
            reiniciar_juego()
        elif turno == "O":
            # Aquí puedes agregar la lógica para la inteligencia artificial del juego
            pass

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in tablero:
        if fila.count(jugador) == 3:
            return jugador

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return jugador

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return jugador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return jugador

    return None

# Función para reiniciar el juego
def reiniciar_juego():
    global turno, tablero

    # Reiniciar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Reiniciar los botones
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ", fg="black")

    # Reiniciar el turno
    turno = "X"

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)

        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
#ventana.mainloop()

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el tablero
        tablero[fila][columna] = turno

        # Actualizar el texto del botón
        botones[fila][columna].config(text=turno)

        # Cambiar el turno
        turno = "O" if turno == "X" else "X"

        # Verificar si hay un ganador
        ganador = verificar_ganador(turno)
        if ganador:
            messagebox.showinfo("Fin del juego", f"¡El jugador {ganador} ha ganado!")
            reiniciar_juego()
        elif not hay_movimientos_disponibles():
            messagebox.showinfo("Fin del juego", "¡Empate!")
            reiniciar_juego()
        elif turno == "O":
            jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador:
            return jugador

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return jugador

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return jugador
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return jugador

    return None

# Función para verificar si hay movimientos disponibles
def hay_movimientos_disponibles():
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                return True
    return False

# Función para reiniciar el juego
def reiniciar_juego():
    global turno, tablero

    # Reiniciar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Reiniciar los textos y colores de los botones
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ", bg="white")

    # Reiniciar el turno
    turno = "X"

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5,
                          font=("Arial", 20), command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)
        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
ventana.mainloop()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    pass

# Función para reiniciar el juego
def reiniciar_juego():
    global turno, tablero

    # Reiniciar el tablero
    tablero = [[" " for _ in range(3)] for _ in range(3)]

    # Reiniciar los textos y colores de los botones
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ", bg="white")

    # Reiniciar el turno
    turno = "X"

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el tablero
        tablero[fila][columna] = turno

        # Actualizar el texto del botón
        botones[fila][columna].config(text=turno)

        # Cambiar el turno
        turno = "O" if turno == "X" else "X"

        # Verificar si hay un ganador
        verificar_ganador(turno)

        # Si no hay movimientos disponibles, reiniciar el juego
        if not hay_movimientos_disponibles():
            reiniciar_juego()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    pass

# Función para verificar si hay movimientos disponibles
def hay_movimientos_disponibles():
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                return True
    return False

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        # Asignar color rojo para X y verde para O
        color = "red" if turno == "X" else "green"
        boton = tk.Button(ventana, text=" ", width=10, height=5, font=("Arial", 20),
                          command=lambda fila=fila, columna=columna: manejar_clic(fila, columna), bg=color)
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)
        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
ventana.mainloop()
# Función para verificar si hay movimientos disponibles
def hay_movimientos_disponibles():
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                return True
    return False

# Función para reiniciar el juego
def reiniciar_juego():
    # Restablecer el tablero
    for fila in range(3):
        for columna in range(3):
            tablero[fila][columna] = " "
            botones[fila][columna].config(text=" ")

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno

    # Verificar si la casilla está vacía
    if tablero[fila][columna] == " ":
        # Actualizar el tablero y el botón
        tablero[fila][columna] = turno
        botones[fila][columna].config(text=turno)

        # Verificar si hay un ganador
        if verificar_ganador(turno):
            messagebox.showinfo("Fin del juego", f"¡El jugador {turno} ha ganado!")
            reiniciar_juego()
        # Verificar si hay empate
        elif not hay_movimientos_disponibles():
            messagebox.showinfo("Fin del juego", "¡Empate!")
            reiniciar_juego()
        else:
            # Cambiar el turno del jugador
            turno = "O" if turno == "X" else "X"

            # Si el turno es de la computadora, hacer que juegue
            if turno == "O":
                jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador:
            return True

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return True

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True

    return False

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, font=("Arial", 20),
                          command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)
        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
ventana.mainloop()



# Función para verificar si hay movimientos disponibles
def hay_movimientos_disponibles():
    pass

# Función para reiniciar el juego
def reiniciar_juego():
    # Restablecer el tablero
    for fila in range(3):
        for columna in range(3):
            tablero[fila][columna] = " "
            botones[fila][columna].config(text=" ", bg="white")

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = turno
        botones[fila][columna].config(text=turno, bg="red" if turno == "X" else "blue")
        verificar_ganador(turno)
        turno = "O" if turno == "X" else "X"
        jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador:
            mostrar_mensaje_ganador(jugador)
            return

    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            mostrar_mensaje_ganador(jugador)
            return

    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        mostrar_mensaje_ganador(jugador)
        return

    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        mostrar_mensaje_ganador(jugador)
        return

    # Verificar empate
    if not hay_movimientos_disponibles():
        mostrar_mensaje_empate()

# Función para mostrar un mensaje de ganador
def mostrar_mensaje_ganador(jugador):
    mensaje = f"¡El jugador {jugador} ha ganado!"
    tk.messagebox.showinfo("Fin del juego", mensaje)
    reiniciar_juego()

# Función para mostrar un mensaje de empate
def mostrar_mensaje_empate():
    tk.messagebox.showinfo("Fin del juego", "¡Empate!")
    reiniciar_juego()

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, font=("Arial", 20),
                          command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)
        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Ejecutar la ventana principal
ventana.mainloop()

# Crear ventana principal
ventana = tk.Tk()
ventana.title("Tres en Raya")

# Crear tablero
tablero = [[" " for _ in range(3)] for _ in range(3)]

# Variable para controlar el turno del jugador
turno = "X"

# Crear botones del tablero
botones = []
for fila in range(3):
    fila_botones = []
    for columna in range(3):
        boton = tk.Button(ventana, text=" ", width=10, height=5, font=("Arial", 20),
                          command=lambda fila=fila, columna=columna: manejar_clic(fila, columna))
        boton.grid(row=fila, column=columna, sticky="nsew")
        fila_botones.append(boton)
        ventana.grid_rowconfigure(fila, weight=1)
        ventana.grid_columnconfigure(columna, weight=1)
    botones.append(fila_botones)

# Función para verificar si hay movimientos disponibles
def hay_movimientos_disponibles():
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                return True
    return False

# Función para reiniciar el juego
def reiniciar_juego():
    global tablero, turno
    tablero = [[" " for _ in range(3)] for _ in range(3)]
    turno = "X"
    for fila in range(3):
        for columna in range(3):
            botones[fila][columna].config(text=" ")

# Función para manejar el clic en un botón del tablero
def manejar_clic(fila, columna):
    global turno
    if tablero[fila][columna] == " ":
        tablero[fila][columna] = turno
        botones[fila][columna].config(text=turno)
        if verificar_ganador(turno):
            mostrar_mensaje_ganador(turno)
        elif not hay_movimientos_disponibles():
            mostrar_mensaje_empate()
        else:
            turno = "O" if turno == "X" else "X"
            if turno == "O":
                jugar_computadora()

# Función para verificar si hay un ganador
def verificar_ganador(jugador):
    # Verificar filas
    for fila in range(3):
        if tablero[fila][0] == tablero[fila][1] == tablero[fila][2] == jugador:
            return True
    # Verificar columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna] == jugador:
            return True
    # Verificar diagonales
    if tablero[0][0] == tablero[1][1] == tablero[2][2] == jugador:
        return True
    if tablero[0][2] == tablero[1][1] == tablero[2][0] == jugador:
        return True
    return False

# Función para mostrar un mensaje de ganador
def mostrar_mensaje_ganador(jugador):
    mensaje = f"¡El jugador {jugador} ha ganado!"
    tk.messagebox.showinfo("Fin del juego", mensaje)
    reiniciar_juego()

# Función para mostrar un mensaje de empate
def mostrar_mensaje_empate():
    tk.messagebox.showinfo("Fin del juego", "¡Empate!")
    reiniciar_juego()

# Función para que la computadora juegue
def jugar_computadora():
    # Obtener una lista de casillas vacías
    casillas_vacias = []
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == " ":
                casillas_vacias.append((fila, columna))

    # Elegir una casilla al azar
    fila, columna = random.choice(casillas_vacias)

    # Hacer clic en la casilla elegida
    manejar_clic(fila, columna)

# Ejecutar la ventana principal
ventana.mainloop()
