#TP2 EJERCICIO 4
'''4. Crear un programa que complete un certificado con los datos que el usuario ingrese por 
teclado. El formulario debe ser como el siguiente:
A quien corresponda,
Por el presente se certifica que NOMBRE Y APELLIDO, con DNI: DNI y fecha de nacimiento:
FECHA DE NACIMIENTO no puede asistir a la fiesta del viernes por la noche porque esta 
estudiando para la materia MATERIA''' 

print("Programa certificado")
print()

#Asignamos las variables
nombre = input("Nombre y apellido: ")
DNI = input("DNI: ")
fechaDeNacimiento = input("Fecha de nacimiento: ")
materia = input("Materia: ")
print()

#Imprimimos el texto con las variables
print("A quien corresponda,")
print("Por el presente se certifica que", nombre, "con DNI:", DNI, "y fecha de nacimiento: ")
print(fechaDeNacimiento, "no puede asistir a la fiesta del viernes por la noche porque esta")
print("estudiando para la materia", materia,".")

print("Test ultimo de commit")
