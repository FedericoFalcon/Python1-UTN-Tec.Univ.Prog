"""TP10 EJERCICIO 3
3. Utilizando lo resulto en el ejercicio anterior, ahora la función deberá retornar un diccionario 
donde la key sera el tipo de dato y el value sera una lista de todos los elementos recibidos 
que sean de ese tipo.
Probar con la siguiente entrada: 1, 2.3, 'Hola', [3,5], 'como', 43, 44.5, [6,10]"""

def funcionargs(*args):
    dicc = {}
    
    for i in args:
        key = type(i)
        value = i
        dicc[key] = value
        
    print(dicc)   

funcionargs(1, 2.3, 'Hola', [3,5], 'como', 43, 44.5, [6,10])