#TP4 EJERCICIO 1
# Implemente un programa que le pida al usuario palabras y le muestre la cantidad de letras de 
# cada una. El programa se detendrá cuando el usuario ingrese la palabra “fin”. 
# Ayuda: utilizar el método len(palabra) para saber el tamaño de una palabra. 

print("PROGRAMA CONTADOR LETRAS DE PALABRA") 
print("Ingrese 'fin' para terminar")


while True:
    palabra = input("Ingrese palabra: ")
    if palabra == "fin":
        break
    else:
        print("La palabra", palabra, "contiene", len(palabra), "letras.")
