from tkinter import *

# *!<--------------FUNCIONES-------------->


def delete():
    entry.delete(0, END)


def backspace():
    entry.delete(len(entry.get()) - 1, END)


def agregar(valor):
    entry.insert(END, valor)


def calcular():
    try:
        resultado = eval(entry.get().replace("x", "*").replace("÷", "/"))
        entry.delete(0, END)
        entry.insert(END, str(resultado))
    except:
        entry.delete(0, END)
        entry.insert(END, "Error")


# *!<--------------VENTANA-------------->
window = Tk()
window.configure(bg="black")

# *!<--------------ENTRADA-------------->
entry = Entry(window, font=("Consolas", 25),
              justify=RIGHT, bd=5, bg="black", fg="white")
entry.pack()

# *!<--------------MARCO-------------->
frame = Frame(window, bd=5, bg="black")
frame.pack()

# *!<--------------BOTONES-------------->


def crear_boton(texto, fila, columna, comando, color_fondo, color_texto, borde=0):
    Button(frame, text=texto, font=("Consolas", 25), width=3, command=comando,
           bg=color_fondo, fg=color_texto, bd=borde).grid(row=fila, column=columna)


crear_boton("AC", 0, 1, delete, "black", "orange")
crear_boton("⌫", 0, 2, backspace, "black", "orange")
crear_boton("%", 0, 3, lambda: agregar("%"), "black", "orange")
crear_boton("÷", 0, 4, lambda: agregar("÷"), "black", "orange")

crear_boton("7", 1, 1, lambda: agregar("7"), "black", "white")
crear_boton("8", 1, 2, lambda: agregar("8"), "black", "white")
crear_boton("9", 1, 3, lambda: agregar("9"), "black", "white")
crear_boton("x", 1, 4, lambda: agregar("x"), "black", "orange")

crear_boton("4", 2, 1, lambda: agregar("4"), "black", "white")
crear_boton("5", 2, 2, lambda: agregar("5"), "black", "white")
crear_boton("6", 2, 3, lambda: agregar("6"), "black", "white")
crear_boton("-", 2, 4, lambda: agregar("-"), "black", "orange")

crear_boton("1", 3, 1, lambda: agregar("1"), "black", "white")
crear_boton("2", 3, 2, lambda: agregar("2"), "black", "white")
crear_boton("3", 3, 3, lambda: agregar("3"), "black", "white")
crear_boton("+", 3, 4, lambda: agregar("+"), "black", "orange")

crear_boton("", 4, 1, lambda: None, "black", "white")  
crear_boton("0", 4, 2, lambda: agregar("0"), "black", "white")
crear_boton(".", 4, 3, lambda: agregar("."), "black", "white")
crear_boton("=", 4, 4, calcular, "orange", "white")

# *!<--------------EJECUCIÓN-------------->
window.mainloop()
