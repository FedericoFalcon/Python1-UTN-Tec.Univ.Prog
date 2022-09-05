#TP 3 EJERCICIO 6
'''6. Hacer una calculadora, donde el usuario ingresa dos numeros y escribe una de 4 palabras: 
suma, resta, multiplicacion o division. El programa debe devolver error si el usuario escribió 
otra palabra que no este dentro de esas 4 o en el caso de la division si quiere hacerlo por 0.
Ayuda: usar exit para terminar la ejecución del programa 
from sys import exit
exit() '''

from sys import exit 

print("PROGRAMA CALCULADORA")
operando_1 = float(input("Ingrese primer operando: "))
operando_2 = float(input("Ingrese segundo operando: "))
operador = input("Ingrese operador: (suma/resta/multiplicacion/division): ")

if operador.lower() == "suma" or operador.lower() == "resta" or operador.lower() == "multiplicacion" or operador.lower() == "division": 
    if operador.lower() == "suma":
       print("Resultado suma: %.2f" %(operando_1 + operando_2))
    elif operador.lower() == "resta":
        print("Resultado resta: %.2f" %(operando_1 - operando_2))
    elif operador.lower() == "multiplicacion":
        print("Resultado multiplicacion: %.2f" %(operando_1 * operando_2))
    elif operador.lower() == "division" and operando_2 != 0:
        print("Resultado division: %.2f" %(operando_1 / operando_2))
    else:
        print("Error! No se puede dividir por 0.")
        exit()
else:  
    print("Error! Ingrese un operador valido.")
    exit()





    
