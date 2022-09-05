#TP 6 EJERCICIO 2
#  2. Generar una lista X de 100 números reales entre -5 y 5, seguidamente generar la lista Y con la 
#  función f(x) = 2X^2 - 10. 
#  Ayuda: usar randint() para generar números aleatorios 

from random import seed, randint

seed()

lista = []
listaFuncion = []

for x in range(100):
    lista.append(randint(-5,5))

for x in lista:
    listaFuncion.append(2 * x ** 2 - 10)

print(lista)
print()
print(listaFuncion)