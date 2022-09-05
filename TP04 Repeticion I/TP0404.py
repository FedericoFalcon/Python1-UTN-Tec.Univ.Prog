#TP 4 EJERCICIO 4
''' Realiza un programa, que muestre un menú en pantalla con las opciones:
1) Sumar
2) Restar
3) Multiplicar
4) Dividir 
5) Salir
El usuario debe seleccionar una opción. y a continuación, el programa deber solicitar el 
ingreso de 2 números enteros. Una vez ingresados los números, se deberá evaluar con una 
sentencia if realizando la operación correspondiente a la opción seleccionada.
La ejecución debe realizarse una y otra vez, hasta que el usuario seleccione la opción # 5.'''

print()
print("PROGRAMA CALCULADORA WHILE")



while True:
    print()
    print("1) Sumar")
    print("2) Restar")
    print("3) Multiplicar")
    print("4) Dividir")
    print("5) Salir")

    opcion = int(input("Opcion? "))
    if opcion == 5 or opcion > 5 or opcion < 0:
        print("Programa terminado.")
        break
    nro1 = float(input("Ingrese primer operando: "))
    nro2 = float(input("Ingrese segundo operando: "))

    if opcion == 1:
        resultado = nro1 + nro2
        print(nro1, "+", nro2,"=", resultado)
        print()
    elif opcion == 2:
        resultado = nro1 - nro2
        print(nro1, "-", nro2,"=", resultado)
        print()
    elif opcion == 3:
        resultado = nro1 * nro2
        print(nro1, "*", nro2,"=", resultado)
        print()
    elif opcion == 4:
        if nro2 != 0:
            resultado = nro1 / nro2
            print(nro1, "/", nro2,"=", resultado)
            print()
        else:
            print("No se puede dividir por 0.")
    else:
        print("Error!")
        


        
