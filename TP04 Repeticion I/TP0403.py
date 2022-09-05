#TP04 EJERCICIO 3
# Escriba un programa que solicite una contraseña (el texto de la contraseña no es importante) 
# y la vuelva a solicitar hasta que las dos contraseñas coincidan, con un límite de tres 
# repeticiones

print() 
print("PROGRAMA PASSWORDS")

intentos = 3

while intentos > 0:
    print()
    contrasenia = input("Ingrese contrasenia: ")
    contrasenia_2 = input("Confirme contrasenia: ")
    if contrasenia == contrasenia_2:
        print()
        print("Todo correcto.")
        break
    else:
        print()
        print("Las contrasenias no coinciden.")
        intentos = intentos - 1
        continue

if intentos == 0:
    print()
    print("Ha excedido el limite de intentos.")