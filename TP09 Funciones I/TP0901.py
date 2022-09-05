"""TP9 EJERCICIO 1
1. Crear una función que se llame max_de_tres donde reciba como parámetros 3 números y 
devuelva el máximo. """

def max_de_tres(numero1,numero2,numero3):
    if numero1 > numero2:
        if numero1 > numero3:
            return numero1
    elif numero2 > numero3:
        return numero2
    else:
        return numero3

num1 = int(input("Numero 1: "))
num2 = int(input("Numero 2: "))
num3 = int(input("Numero 3: "))
resultado = max_de_tres(num1, num2, num3)

print(resultado)