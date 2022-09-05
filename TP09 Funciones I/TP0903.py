"""TP9 EJERCICIO 3
3. Definir una función que acepte el radio y retorne el area de un circulo. """

def area_circulo(radio):
    PI = 3.1415
    area = PI * (radio ** 2)
    return area

ingreso_radio = float(input("Radio? "))

resultado = area_circulo(ingreso_radio)

print("%.2f" %resultado)
