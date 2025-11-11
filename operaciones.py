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
