#TP6 EJERCICIO 1
# 1. Generar una lista con los elementos pares múltiplos de 3 menores a 100.  
lista = []

for i in range(0,101,3):
   if i % 2 == 0:
        lista.append(i)

print(lista)
