#TP7 EJERCICIO 4
''' 4. Hacer un programa que encuentre el elemento perdido entre dos grupos de valores 
Entrada: A = [1, 4, 5, 7, 9], B = [4, 5, 7, 9]
Salida: [1] '''

A = [1, 4, 5, 7, 9]
set_A = set(A)

B = [4, 5, 7, 9]
set_B = set(B)

C = set_A - set_B

lista_C = list(C)
print(lista_C)