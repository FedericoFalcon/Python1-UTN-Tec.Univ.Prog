#TP7 EJERCICIO 2
''' 2. Hacer el mismo ejercicio que el punto 1, pero trabajando con sets,  sets = {1, 2, 3, 4, 5, 6} '''

sets = {1, 2, 3, 4, 5, 6}
lista_del_set = list(sets)

while True:
    i = int(input("Indice? "))
    if i >= len(lista_del_set) or i < 0:
        print("Error. Fuera de rango.")
    else:
        print(lista_del_set[i])
    continue
