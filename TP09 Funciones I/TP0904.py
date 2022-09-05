"""TP9 EJERCICIO 4
4. Escribir una función que cuente la cantidad de vocales, espacios y consonantes de una frase."""

def contador(frase):

    contador_espacios = 0
    contador_vocales = 0
    contador_consonantes = 0
    lista_vocales = ("a","e","i","o","u")

    for i in frase.lower():
        if i in lista_vocales:
            contador_vocales += 1
        elif i == " ":
            contador_espacios += 1
        else:
            contador_consonantes += 1
    
    return contador_vocales,contador_espacios,contador_consonantes

ingreso_frase = input("Frase? ")

resultado_vocales,resultado_espacios,resultado_consonantes = contador(ingreso_frase)

print("La frase tiene", resultado_vocales, "vocales,",resultado_espacios,"espacios y",
resultado_consonantes,"consonantes")


