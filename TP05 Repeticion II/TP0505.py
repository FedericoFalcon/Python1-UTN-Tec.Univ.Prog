#TP 5 EJERCICIO 5
#5. Solicitar al usuario que ingrese una frase y luego imprimir un listado de todas las vocales que 
# aparecen en esa frase.

frase = input("Frase? ")
vocales = 0
for i in frase:
    if i == "a":
        print("a",end=" ")
    elif i == "e":
        print("e",end=" ")
    elif i == "i":
        print("i",end=" ") 
    elif i == "o":
        print("o",end=" ")
    elif i == "u":
        print("u",end=" ")
          


