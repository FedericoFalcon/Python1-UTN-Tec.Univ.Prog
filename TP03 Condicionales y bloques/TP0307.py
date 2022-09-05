#TP03 Ejercicio 7
'''7. Crear un juego donde el usuario tiene 3 oportunidades para adivinar un numero secreto que el 
programador le asigno a una variable llamada 'palabra_secreta', el programa debe ayudar al 
jugador diciendo si el numero que el ingreso es 'Muy alto', 'Muy bajo' o si adivino.
Ayuda: usar exit para terminar la ejecución del programa al igual que el punto 6, y tambien se 
puede agregar el siguiente codigo para generar numeros aleatorios:
from random import seed, randint 
# semilla para el generador de numeros aleatorios  
seed() 
# se generan numeros aleatorios enteros entre 0 y 10 
 numero_aleatorio = randint(0, 10) '''

from sys import exit
from random import seed, randint 

print()
print("PROGRAMA ADIVINAR NUMERO")


# semilla para el generador de numeros aleatorios 
seed() 
# se generan numeros aleatorios enteros entre 0 y 10 
palabra_secreta = randint(0, 10)


print()
print("Tienes 3 intentos para adivinar un numero aleatorio del 0 al 10")
print("Empecemos!")
print()

intento_1 = int(input("Primer intento? "))

if intento_1 == palabra_secreta:
    print("Adivinaste!")
    exit()
elif intento_1 > palabra_secreta:
    print("Muy alto!")
else:
    print("Muy bajo!")


intento_2 = int(input("Segundo intento? "))

if intento_2 == palabra_secreta:
    print("Adivinaste!")
    exit()
elif intento_2 > palabra_secreta:
    print("Muy alto!")
else:
    print("Muy bajo!")

intento_3 = int(input("Tercer intento? "))
if intento_3 == palabra_secreta:
    print("Adivinaste!")
    exit()
elif intento_3 > palabra_secreta:
    print("Muy alto!")
    print("Perdiste")
else:
    print("Muy bajo!")
    print("Perdiste")


    








    
