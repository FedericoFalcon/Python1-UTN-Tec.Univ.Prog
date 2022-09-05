#TP4 EJERCICIO 2
# Hacer un programa que muestre los números pares entre 0 y un numero ingresado por el 
# usuario.

numero = int(input("Ingrese numero: ")) 

while numero >= 0:
    if numero % 2 == 0:
        print(numero)
        numero = numero - 2
        
    elif numero % 2 != 0:
        numero = numero -1
        
    