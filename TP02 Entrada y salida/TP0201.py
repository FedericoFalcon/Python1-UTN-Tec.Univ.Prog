#TP 2 EJERCICIO 1
'''1. Se debe crear un programa que convierta las unidades de temperatura de grados Fahrenheit 
a grados Celsius (Investigar la expresión para convertir). El programa debe permitir el ingreso 
por teclado de la temperatura'''

print("Programa Conversor Farenheit a Celsius") 
farenheit = float (input('Ingrese grados Farenheit a convertir: '))
celsius = (farenheit - 32) * 5 / 9
print(farenheit, "grados Farenheit equivalen a %.2f" %celsius, "grados Celsius.")