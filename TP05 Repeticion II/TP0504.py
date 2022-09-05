#TP 5 EJERCICIO 4
# 4. Dado un número entero positivo, mostrar su factorial. El factorial de un número se obtiene 
# multiplicando todos los números enteros positivos que hay entre el 1 y ese número.

numero = int(input("Numero? "))

for i in range(1, numero):
    numero = numero * i

print(numero)
 