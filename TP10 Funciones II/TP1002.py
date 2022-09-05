"""TP10 EJERCICIO 2
2. Escribir una función que espere un numero no limitado de parámetros e imprima por pantalla 
las siguientes característica: Cantidad y tipo de parámetros recibidos.
Probar con la siguiente entrada: 1, 2.3, 'Hola', [3,5]"""

def funcionargs(*args):
    for i in args:
        print(type(i))

funcionargs(1,2.3,"Hola",[3,5])