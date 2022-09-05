#TP 3 EJERCICIO 5 Especifique una expresión condicional que, a partir de un año, determine si es bisiesto o no. 

print("PROGRAMA ANIO BISIESTO")

anio = int(input("Ingrese anio a determinar: "))

if ((anio % 4 == 0 and anio % 100 != 0) or (anio % 100 == 0 and anio % 400 == 0)):
    print("Es bisiesto")
else: 
    print("No es bisiesto")

    
    
