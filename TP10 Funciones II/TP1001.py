"""TP10 EJERCICIO 1
1. Escribir una función para hacer un censo, la función debe recibir 4 parámetros: Nombre, 
Apellido, Edad y si trabaja o no. El Nombre y Apellido no son parámetros obligatorio, asi que 
por default debería ser Anónimo en caso de no recibir nada, los otros parámetros son 
obligatorios. La función debe retornar una lista de los parámetros si todo esta bien, caso 
contrario un error."""

def censo(nombre = "anonimo", apellido = "anonimo", edad = None,trabajo = None):
    lista = []
    if edad == None or trabajo == None:
        return "error, faltan datos"
    else:
        lista.append(nombre)
        lista.append(apellido)
        lista.append(edad)
        lista.append(trabajo)
        return lista

nombre = "federico"
apellido = "falcon"
edad = 29
trabajo = "si"
resultado_error = censo(nombre,apellido,edad)
resultado = censo(nombre,apellido,edad,trabajo)
print(resultado_error)
print(resultado)