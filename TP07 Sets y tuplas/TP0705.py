#TP7 EJERCICIO 5
'''5. A partir de dos sets A y B, generar dos listas: una de ellas llamada “intersección” con los 
elementos presentes en A y en B, la otra llamada “restante” que tenga los elementos de A y B 
que no están en ambos sets. 
Entrada: A = {1,2,3,4,5,6}, B = {2,3,4,10,11,12}
Salida: 
intersección = [2,3,4]
restante = [1,5,6,10,11,12'''

A = {1,2,3,4,5,6}

B = {2,3,4,10,11,12}

C = A & B

interseccion = list(C)
print("Interseccion: ",interseccion)

restoTotal = []

for i in A:
    if i not in interseccion:
        restoTotal.append(i)

for j in B:
    if j not in interseccion:
        restoTotal.append(j)

print("Restante: ", restoTotal)