#TP6 EJERCICIO 4
''' 4. A partir de dos listas A y B, generar dos nuevas listas: una de ellas llamada “intersección” con 
los elementos presentes en A y en B, la otra llamada “restante” que tenga los elementos de A 
y B que no están en ambas listas. 
Listas:
A = [1,2,3,4,5,6], B = [2,3,4,10,11,12]  
Resultado:
intersección = [2,3,4]
restante = [1,5,6,10,11,12] '''

A = [1,2,3,4,5,6]

B = [2,3,4,10,11,12] 
interseccion = []
restante = []

for i in range(len(A)):
    for j in range(len(B)):
        if A[i] == B[j]:
            interseccion.append(B[j])

for x in A:
    if x not in interseccion:
        restante.append(x)

for x in B:
    if x not in interseccion:
        restante.append(x)

print("Interseccion:",interseccion)
print()
print("Restante:",restante)
