#TP7 EJERCICIO 1
# 1. Dada una tupla ya definida, tupla = (1, 2, 3, 4, 5, 6), escribir un programa donde se le pida al 
# usuario el indice y se devuelva el valor. El programa debe estar preparado para tener mensaje 
# de error y volverle a pedir el numero las veces que sea necesario, en caso de que el valor 
# ingresado sea incorrecto

tupla = (1, 2, 3, 4, 5, 6)

while True:
    i = int(input("Indice? "))
    if i >= len(tupla) or i < 0:
        print("Error. Fuera de rango.")
    else:
        print(tupla[i])
    continue



