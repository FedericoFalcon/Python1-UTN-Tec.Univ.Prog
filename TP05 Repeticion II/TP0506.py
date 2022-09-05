#TP 5 EJERCICIO 6
''' 6. Utilizando for anidados la idea es que sean capaz de, dado un numero ingresado por el 
usuario, imprimir un triangulo de asterisco de manera creciente hacia abajo donde el alto y el 
ancho debe ser igual al valor ingresado por el usuario. Ejemplo, si el usuario ingresa el numero 5, 
el programa debería imprimir lo siguiente:
*
* *
* * * 
* * * *
* * * * *                                          '''

numero = int(input("Numero? "))

for i in range(numero+1):
    for j in range(i):
        print("*",end=" ")
    print()