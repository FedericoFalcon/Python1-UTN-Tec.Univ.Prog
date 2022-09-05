#TP 3 EJERCICIO 4. Dados 3 números enteros, implemente un algoritmo para determinar el mayor de los 3

print("PROGRAMA NUMERO MAYOR")
numero_1 = int(input("Ingrese primer numero: "))
numero_2 = int(input("Ingrese segundo numero: ")) 
numero_3 = int(input("Ingrese tercer numero: "))

if numero_1 >  numero_2:
    if numero_1 > numero_3:
        print("El numero mayor es: ")
        print(numero_1)
    else:
        print("El numero mayor es: ")
        print(numero_3)
elif numero_2 > numero_3:
        print("El numero mayor es: ")
        print(numero_2)
else:
    print("El numero mayor es: ", numero_3)
    
