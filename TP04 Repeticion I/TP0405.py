#TP 4 EJERCICIO 5
'''  Se necesita crear un programa para un almacén de barrio, el programa debe permitir al 
usuario ingresar el precio de los productos, y al final imprimir el ticket con la cantidad de 
productos ingresados y el precio total con y sin IVA. '''

print("TICKET ALMACEN") 
print("Ingrese el valor de cada producto.")
print("Al final recibira el precio total con y sin IVA.")
print("Para terminar, ingrese 0.")

precioTotal = 0.00

while True:
    precio = float(input("Precio? "))
    if precio == 0:
        break
    precioTotal = precio + precioTotal

print("Precio total: %.2f" %precioTotal)
precioTotalConIva = precioTotal + (precioTotal * 0.21)
print("Precio total con IVA: %.2f" %precioTotalConIva)
