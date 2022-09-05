#TP7 EJERCICIO 3
'''3. Dada una tupla de tuplas, elimine todas las tuplas con longitud K en una nueva lista.
Entrada : tupla_prueba = ((4, 5),(4,),(8, 6, 7),(5, 8),(1,),(3, 4, 6, 7)), K = 2 
Salida : [(4,) ,(8, 6, 7),(1,),(3, 4, 6, 7)] '''

tupla_prueba = ((4, 5),(4,),(8, 6, 7),(5, 8),(1,),(3, 4, 6, 7))
k = 2 

salida = []

for i in range (len(tupla_prueba)):
    if len(tupla_prueba[i]) != k:
        salida.append(tupla_prueba[i])

print(salida)