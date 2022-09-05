A = [1,2,3,4,5,6] 
B = [2,3,4,10,11,12]
interseccion = [] 
restante = []
flag = False
for i in A:
    for j in B:
        if i == j:
            interseccion.append(i)
            flag = True
            break
    if flag == False:
        restante.append(i)
    flag = False
for i in B:
    for j in interseccion:
        if i == j:
            flag = True
            break
    if flag == False:
        restante.append(i)
    flag = False
print(interseccion)
print(restante)
    