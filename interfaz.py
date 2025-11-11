import tkinter as tk
from tkinter.constants import CENTER


class botonera:
    def __init__(self):
       pass

    def iniciar(self,ventana):
        entrada = tk.Entry(ventana, justify="center",bg="lightgray")
        entrada.place()

class interfaz:
    def __init__(self):

        ventana = tk.Tk()
        ventana.title("Calculadora")
        ventana.geometry("600x400")
        botones = botonera()
        botones.iniciar(ventana)


        ventana.mainloop()