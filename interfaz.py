import tkinter as tk
import  operaciones as op


class botonera:

    def __init__(self):
        self.reset = False

    def iniciar(self,ventana):

        botones = [
        '7', '8', '9', ' / ',
        '4', '5', '6', ' * ',
        '1', '2', '3', ' - ',
        '0', '=', ' + '
        ]

        fila = 1
        columna = 0

        entrada = tk.Entry(ventana, justify="right", font=('Arial', 24), bd=10, relief=tk.SUNKEN)
        entrada.grid(row=0, column=0, columnspan=4, sticky="nsew", padx=10, pady=10)


        def cambiar_texto(valor):
            if self.reset == True:
                entrada.delete(0, tk.END)
                self.reset = False
                entrada.insert(1 + len(entrada.get()) , valor)
            else:
                texto = entrada.get()
                entrada.insert(1 + len(entrada.get()), valor)

        def operaciones():

            operador = op.Operaciones()
            valor = operador.lector(entrada.get())

            self.reset = True

            entrada.delete(0, tk.END)
            entrada.insert(0,valor)


        for texto_boton in botones:
            if texto_boton != "=":
                boton = tk.Button(ventana, text=texto_boton, font=('Arial', 18), bd=5, command=lambda valor=texto_boton: cambiar_texto(valor))
            else:
                boton = tk.Button(ventana, text=texto_boton, font=('Arial', 18), bd=5, command=lambda : operaciones())


            boton.grid(row=fila, column=columna, sticky="nsew", padx=5, pady=5)

            columna += 1
            if columna > 3:
                columna = 0
                fila += 1

        ventana.grid_columnconfigure((0, 1, 2, 3), weight=1)
        ventana.grid_rowconfigure((1, 2, 3, 4), weight=1)



class interfaz:
    def __init__(self):

        ventana = tk.Tk()
        ventana.title("Calculadora")
        ventana.geometry("600x400")
        botones = botonera()
        botones.iniciar(ventana)


        ventana.mainloop()
