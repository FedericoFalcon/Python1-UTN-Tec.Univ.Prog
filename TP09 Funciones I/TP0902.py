"""TP9 EJERCICIO 2
2. Escribir una función que sume todos los elementos de una lista y los retorne para luego 
imprimirlos en el programa principal. """

lista = (1,5,8,9)

def suma_lista(lista_a_sumar):
    suma_total = 0
    for i in range(len(lista_a_sumar)):
        suma_total += lista_a_sumar[i]

    return suma_total

resultado = suma_lista(lista)

print("El resultado de la suma es:" ,resultado)