def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicacion(a, b):
    return a * b

def division(a, b):
    return a / b


class Operaciones:
    def __init__(self):
        pass

    def lector(self,operacion):
        A = float(operacion.split(" ")[0])
        B = float(operacion.split(" ")[2])

        valor = 0

        match operacion.split(' ')[1]:

            case "+":
                valor = float(suma(A,B))
            case "-":
                valor = float(resta(A,B))
            case "*":
                valor = float(multiplicacion(A,B))
            case "/":
                valor = float(division(A,B))

        return valor

        import  interfaz as inter
import  operaciones as op

interfaz = inter.interfaz()
operaciones = op.Operaciones()


print(operaciones.lector("4 + 3"))
print(operaciones.lector("4 - 3"))
print(operaciones.lector("4 * 3"))
print(operaciones.lector("4 / 3"))



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