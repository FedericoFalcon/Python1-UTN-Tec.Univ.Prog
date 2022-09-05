#TP2 EJERCICIO 3

'''3. Se necesita crear un programa para un almacén de barrio, el programa debe permitir al 
usuario ingresar el nombre de 3 productos con sus respectivos precios, y al final imprimir el 
ticket con el nombre de cada producto, el precio individual y el precio total con y sin IVA.'''


#Titulo con disenio p/consola 
print("---------------------------------------------------------------------------------------------") 
print("-                                   Programa Ticket                                          ")
print("---------------------------------------------------------------------------------------------")
print()

print ("Bienvenido!") 
nombreComercio = input ("Ingrese nombre del comercio: ")
print()

                                                    
print ("Este programa realizara un ticket por el valor total de tres productos, con y sin Iva.")
print ("Ingrese nombre y luego precio de cada producto:")
print ()

#Asignacion de nombres y precios para los productos
nombreProd1 =  input("Nombre producto1: ")
precioProd1 = float (input("Precio $ :"))
nombreProd2 = input("Nombre producto2: ")
precioProd2 = float (input("Precio $ :"))
nombreProd3 = input ("Nombre producto3: ")
precioProd3 = float (input("Precio $ :"))
print()

#Calculos necesarios
total = (precioProd1 + precioProd2 + precioProd3)
IVA = (total * 0.21)
totalConIVA = (total + IVA)

#Impresion ticket
print("--------------------TICKET---------------------")
print("  Comercio:             ", nombreComercio)
print()
print(nombreProd1)
print("                         ---$ %.2f" %precioProd1)
print(nombreProd2)
print("                         ---$ %.2f" %precioProd2)
print(nombreProd3)
print("                         ---$ %.2f" %precioProd3)
print()
print("Total                    ---$ %.2f" %total)
print("IVA                      ---$ %.2f" %IVA)
print("Final                    ---$ %.2f" %totalConIVA)
print()
print("-----------Gracias por su compra!-------------")