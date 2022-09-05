#TP 5 EJERCICIO 7
'''  7. La idea es la misma que el ejercicio anterior, pero esta vez se deberán imprimir los números 
correspondiente a cada casillero:
1 
1 2 
1 2 3  
1 2 3 4 
1 2 3 4 5  '''


numero = int(input("Numero? "))

for i in range(numero+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()