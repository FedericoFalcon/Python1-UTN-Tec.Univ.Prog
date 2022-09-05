#TP6 EJERCICIO 3
''' 3. Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, 
Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en 
cada asignatura y guarde en una lista las aprobadas y en otra las desaprobadas. '''

asignaturas = ["Matematica","Fisica","Quimica","Historia","Lengua"] 

listaAprobadas = []

listaDesaprobadas = []

for i in range(len(asignaturas)):
    print(asignaturas[i])
    nota = int(input("Nota? "))
    if nota >= 6:
        listaAprobadas.append(asignaturas[i])
    else:
        listaDesaprobadas.append(asignaturas[i])

print("Lista aprobadas: ",listaAprobadas)
print("Lista desaprobadas: ",listaDesaprobadas)




