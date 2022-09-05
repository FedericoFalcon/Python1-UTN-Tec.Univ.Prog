'''
Proyecto   : Sistema de comandas
Integrantes: Falcon Federico          / Durando Ignacio
Contacto   : ffalcondepizzo@gmail.com / durandodepizzoignacio@gmail.com
'''

#Biblioteca para borrar la consola
import sys, os


#Diccionarios para el menu del restaurant
bebidas = {'Coca': 200, 'Fanta': 200, 'Sprite': 200}
entradas = {'Rabas': 300, "Picada p/4" : 600, "Patitas pollo" : 400}
principales = {'Asado c/ papas': 700, "Milanesa c/pure" : 550, "Tallarines" : 400}
postres = {'Helado': 350, "Flan c/ddl" : 300, "Torta cumple" : 500}
pizzas = {'Muzzarela': 450, "4 quesos" : 550, "Especial" : 500}

#Listas para cada mesa
mesa0 = []
mesa1 = []
mesa2 = []
mesa3 = []
mesa4 = []
mesa5 = []
mesa6 = []
mesa7 = []
mesa8 = []
mesa9 = []

#Lista para el total de las mesas
mesasTotales = []
mesasTotales.append(mesa0)
mesasTotales.append(mesa1)
mesasTotales.append(mesa2)
mesasTotales.append(mesa3)
mesasTotales.append(mesa4)
mesasTotales.append(mesa5)
mesasTotales.append(mesa6)
mesasTotales.append(mesa7)
mesasTotales.append(mesa8)
mesasTotales.append(mesa9)


#Menu Principal
def menuPrincipal():
    """Menu principal del programa"""

    while (True):
        os.system('cls')
        print()
        print('*************************')
        print('**    Menu Principal   **')
        print('*************************')
        print('*                       *')
        print('*  Seleccione:          *')
        print('*                       *')
        print('*   [1] Consultar carta *')
        print('*   [2] Modificar carta *')
        print('*   [3] Gestionar Mesas *')
        print('*   [0] Salir           *')
        print('*                       *')
        print('*************************')

        opcion = input('Opcion?: ')

        if opcion == "0":
            break

        if opcion.isdigit():
            opcion = int(opcion)
        else:
            continue

        if opcion == 1:
            consultarCarta()

        if opcion == 2:
            modificarCarta()
    
        if opcion == 3:
            gestionarMesas()
        
        if opcion == 0:
            break
 
#Funciones del menu principal
def consultarCarta():
    """Muestra la carta"""

    while(True):
        os.system('cls')
        print()
        print('-----------------------')
        print('--       Carta       --')
        print('-----------------------')
        print()
        print('Seleccione:')
        print()
        print('    1) Bebidas')
        print('    2) Entradas')
        print('    3) Platos Principales')
        print('    4) Pizzas')
        print('    5) Postres')
        print('    0) Volver al menu principal')
        print()

        opcion = input('Opcion?: ')
        print()

        if opcion.isdigit():
            opcion = int(opcion)
        else:
            continue

        if opcion == 1:
            os.system('cls')
            print(' ___________')
            print('|  Bebidas  |')
            print()

            for x in bebidas:
                print(x, "   $", '%.2f'%bebidas[x])
            input()
                
        elif opcion == 2:
            os.system('cls')
            print(' ____________')
            print('|  Entradas  |')
            print()

            for x in entradas:
                print(x, "   $", '%.2f'%entradas[x])
            input()

        elif opcion == 3:
            os.system('cls')
            print(' _______________')
            print('|  Principales  |')
            print()

            for x in principales:
                print(x, "   $", '%.2f'%principales[x])
            input()

        elif opcion == 4:
            os.system('cls')
            print(' __________')
            print('|  Pizzas  |')
            print()

            for x in pizzas:
                print(x, "   $", '%.2f'%pizzas[x])
            input()

        elif opcion == 5:
            os.system('cls')
            print(' ___________')
            print('|  Postres  |')
            print()

            for x in postres:
                print(x, "   $", '%.2f'%postres[x])
            input()
        
        elif opcion == 0:
            break

def modificarCarta():
    """Muestra menu para modificar la carta"""

    while(True):
        os.system('cls')
        print()
        print('-------------------------------')
        print('--      Modificar Carta      --')
        print('-------------------------------')
        print()

        print('Seleccione para modificar: ')
        print()
        print('       1) Bebidas')
        print('       2) Entradas')
        print('       3) Platos principales')
        print('       4) Pizzas')
        print('       5) Postres')
        print('       0) Volver al menu principal')
        print()

        opcion = input('Opcion?: ')

        if opcion.isdigit():
            opcion = int(opcion)
        else:
            continue
        if opcion == 0:
            break
        if opcion == 1:
            while(True):
                os.system('cls')
                print()
                print(" Que desea hacer?")
                print()
                print(' 1) Agregar bebida')
                print(' 2) Quitar bebida')
                print(' 0) Volver al menu anterior')
                print()

                opcion2 = input('Opcion?: ')
                if opcion2.isdigit():
                    opcion2 = int(opcion2)
                else:
                    continue

                if opcion2 == 1:
                    agregarBebida()

                elif opcion2 == 2:
                    quitarBebida()
                
                elif opcion2 == 0:
                    break

        elif opcion == 2:
            while(True):
                os.system('cls')
                print()
                print(" Que desea hacer?")
                print()
                print(' 1) Agregar entrada')
                print(' 2) Quitar entrada')
                print(' 0) Volver al menu anterior')
                print()

                opcion2 = input('Opcion?: ')
                if opcion2.isdigit():
                    opcion2 = int(opcion2)
                else:
                    continue

                if opcion2 == 1:
                    agregarEntrada()

                elif opcion2 == 2:
                    quitarEntrada()
                
                elif opcion2 == 0:
                    break

        elif opcion == 3:
            while(True):
                os.system('cls')
                print()
                print(" Que desea hacer?")
                print()
                print(' 1) Agregar plato principal')
                print(' 2) Quitar plato principal')
                print(' 0) Volver al menu anterior')
                print()

                opcion2 = input('Opcion?: ')
                if opcion2.isdigit():
                    opcion2 = int(opcion2)
                else:
                    continue

                if opcion2 == 1:
                    agregarPrincipal()

                elif opcion2 == 2:
                    quitarPrincipal()
                
                elif opcion2 == 0:
                    break
        
        elif opcion == 4:
            while(True):
                os.system('cls')
                print()
                print(" Que desea hacer?")
                print()
                print(' 1) Agregar pizza')
                print(' 2) Quitar pizza')
                print(' 0) Volver al menu anterior')
                print()

                opcion2 = input('Opcion?: ')
                if opcion2.isdigit():
                    opcion2 = int(opcion2)
                else:
                    continue

                if opcion2 == 1:
                    agregarPizza()

                elif opcion2 == 2:
                    quitarPizza()
                
                elif opcion2 == 0:
                    break

        elif opcion == 5:
            while(True):
                os.system('cls')
                print()
                print(" Que desea hacer?")
                print()
                print(' 1) Agregar postre')
                print(' 2) Quitar postre')
                print(' 0) Volver al menu anterior')
                print()

                opcion2 = input('Opcion?: ')
                if opcion2.isdigit():
                    opcion2 = int(opcion2)
                else:
                    continue

                if opcion2 == 1:
                    agregarPostre()

                elif opcion2 == 2:
                    quitarPostre()
                
                elif opcion2 == 0:
                    break

def gestionarMesas():
    """Muestra las mesas y permite elegir una para acceder"""

    while True:
        os.system('cls')
        print()
        print("*****   MESAS   ******")
        print()
        print("Mesa 0:", mesa0)
        print("Mesa 1:", mesa1)
        print("Mesa 2:", mesa2)
        print("Mesa 3:", mesa3)
        print("Mesa 4:", mesa4)
        print("Mesa 5:", mesa5)
        print("Mesa 6:", mesa6)
        print("Mesa 7:", mesa7)
        print("Mesa 8:", mesa8)
        print("Mesa 9:", mesa9)
        print()
        opcionMesa = input("A que mesa desea acceder? (S para salir) ")
        if opcionMesa == "s" or opcionMesa == "S":
            break
        if opcionMesa.isdigit():
            opcionMesa = int(opcionMesa)
        else:
            continue

        if opcionMesa > 9 or opcionMesa < 0:
            continue
        menuMesas(opcionMesa)

#Funciones para gestionar cada mesa
def menuMesas(opcionMesa):
    """Muestra el menu de opciones para cada mesa"""

    while True:
        os.system('cls')
        print( "-----------------------------------" )
        print( "--      GESTIONAR MESA [",opcionMesa, "]     --" )
        print( "-----------------------------------" )
        print()
        print( "Seleccione: " )
        print()
        print( "	1) Cargar mesa" )
        print( "	2) Cerrar mesa" )
        print( "	0) Volver al menu principal" )
        print()
        opcionMenuMesas = input("Opcion? ")
        if opcionMenuMesas == "0":
            break

        if opcionMenuMesas.isdigit():
            opcionMenuMesas = int(opcionMenuMesas)
        else:
            continue
        
        if opcionMenuMesas == 0:
            break
        elif opcionMenuMesas == 1:
            cargarMesa(opcionMesa)
        elif opcionMenuMesas == 2:
            cerrarMesa(opcionMesa)
    

def cargarMesa(opcionMesa):
    """Muestra las opciones que se pueden cargar a cada mesa"""

    while True:
        os.system('cls')
        print()
        print("-----Mesa [",opcionMesa,"] -----")
    
        print(mesasTotales[opcionMesa])
        print()
        print("Que desea cargar a la mesa?")
        print()
        print('    1) Bebidas')
        print('    2) Entradas')
        print('    3) Platos Principales')
        print('    4) Pizzas')
        print('    5) Postres')
        print('    0) Volver al menu principal')
        print()

        opcion = input('Opcion?: ')
        print()

        if opcion.isdigit():
            opcion = int(opcion)
        else:
            continue

        if opcion == 1:
            os.system('cls')
            print(' ___________')
            print('|  Bebidas  |')
            print()

            listaBebidas = []
            contador = 0
            for x in bebidas:
                print(contador,x, "   $", bebidas[x])
                listaBebidas.append(x)
                listaBebidas.append(bebidas[x])
                contador = contador +1
                
            opcionAgregar = input("Opcion ? ")
            if opcionAgregar.isdigit():
                opcionAgregar = int(opcionAgregar)
            else:
                continue
            if opcionAgregar >= len(listaBebidas)/2:
                print("Error! Fuera de rango.")
                input()
                break

            mesasTotales[opcionMesa].append(listaBebidas[opcionAgregar*2])
            mesasTotales[opcionMesa].append(listaBebidas[opcionAgregar*2+1])
                
        elif opcion == 2:
            os.system('cls')
            print(' ____________')
            print('|  Entradas  |')
            print()

            listaEntradas = []
            contador = 0
            for x in entradas:
                print(contador,x, "   $", entradas[x])
                listaEntradas.append(x)
                listaEntradas.append(entradas[x])
                contador = contador +1
                
            opcionAgregar = input("Opcion ? ")
            if opcionAgregar.isdigit():
                opcionAgregar = int(opcionAgregar)
            else:
                continue
            if opcionAgregar >= len(listaEntradas)/2:
                print("Error! Fuera de rango.")
                input()
                break

            mesasTotales[opcionMesa].append(listaEntradas[opcionAgregar*2])
            mesasTotales[opcionMesa].append(listaEntradas[opcionAgregar*2+1])

        elif opcion == 3:
            os.system('cls')
            print(' _______________')
            print('|  Principales  |')
            print()

            listaPrincipales = []
            contador = 0
            for x in principales:
                print(contador,x, "   $", principales[x])
                listaPrincipales.append(x)
                listaPrincipales.append(principales[x])
                contador = contador +1
                
            opcionAgregar = input("Opcion ? ")
            if opcionAgregar.isdigit():
                opcionAgregar = int(opcionAgregar)
            else:
                continue
            if opcionAgregar >= len(listaPrincipales)/2:
                print("Error! Fuera de rango.")
                input()
                break

            mesasTotales[opcionMesa].append(listaPrincipales[opcionAgregar*2])
            mesasTotales[opcionMesa].append(listaPrincipales[opcionAgregar*2+1])

        elif opcion == 4:
            os.system('cls')
            print(' __________')
            print('|  Pizzas  |')
            print()

            listaPizzas = []
            contador = 0
            for x in pizzas:
                print(contador,x, "   $", pizzas[x])
                listaPizzas.append(x)
                listaPizzas.append(pizzas[x])
                contador = contador +1
                
            opcionAgregar = input("Opcion ? ")
            if opcionAgregar.isdigit():
                opcionAgregar = int(opcionAgregar)
            else:
                continue
            if opcionAgregar >= len(listaPizzas)/2:
                print("Error! Fuera de rango.")
                input()
                break

            mesasTotales[opcionMesa].append(listaPizzas[opcionAgregar*2])
            mesasTotales[opcionMesa].append(listaPizzas[opcionAgregar*2+1])

        elif opcion == 5:
            os.system('cls')
            print(' ___________')
            print('|  Postres  |')
            print()

            listaPostres = []
            contador = 0
            for x in postres:
                print(contador,x, "   $", postres[x])
                listaPostres.append(x)
                listaPostres.append(postres[x])
                contador = contador +1
                
            opcionAgregar = input("Opcion ? ")
            if opcionAgregar.isdigit():
                opcionAgregar = int(opcionAgregar)
            else:
                continue
            if opcionAgregar >= len(listaPostres)/2:
                print("Error! Fuera de rango.")
                input()
                break

            mesasTotales[opcionMesa].append(listaPostres[opcionAgregar*2])
            mesasTotales[opcionMesa].append(listaPostres[opcionAgregar*2+1])
        
        elif opcion == 0:
            break

def cerrarMesa(opcionMesa):
    """Cierra la mesa, imprime el ticket y borra el contenido"""

    while True:
        os.system('cls')
        print()
        print("------ CERRAR MESA [",opcionMesa,"] -------")
        print()
        print(mesasTotales[opcionMesa])
        print()
        opcion = input("Confirma que desea cerrar mesa? (si/no): ")
        if opcion == "no" or opcion == "NO":
            break
        elif opcion == "si" or opcion == "SI":
            os.system('cls')
            print()
            print("================================")
            print("====== TICKET MESA [",opcionMesa,"] =======")
            print("================================")
            
            sumaTotal = 0
            contador = 0
            
            for x in mesasTotales[opcionMesa]:
                if contador % 2 == 0:
                    print("{:->15}".format(x), end="          $",)
                else:
                    print('%.2f'%x)
                    sumaTotal = sumaTotal + x
                
                contador = contador + 1

            mesasTotales[opcionMesa].clear()

            print()
            print("================================")    
            print("Total:            $",'%.2f'%sumaTotal)    
            print("================================")
            print("Gracias por elegirnos!")
       
            input()
            break
    menuPrincipal()

#Funciones del menu "modificarCarta()"      
def agregarBebida():
    """Agrega bebida nueva"""

    while True:
        nombreProducto = input('Ingrese nueva bebida: ').capitalize()
        valorProducto = (input('Precio para '+ nombreProducto + "?: "))
        if valorProducto.isdigit():
            valorProducto = int(valorProducto)
        else:
            print()
            print('Error! Ingrese un valor valido.')
            input()
            break

        bebidas[nombreProducto] = valorProducto
        print("Agregado con exito.")
        input()
        break

def quitarBebida():
    """Quita bebida existente"""

    print(' ___________')
    print('|  Bebidas  |')
    print()
    for x in bebidas:
       print(x, bebidas[x])
    print()
    opcionQuitar = input("Ingrese cual desea quitar? ")
    error = "No existe"
    bebidas.pop(opcionQuitar.capitalize(), error)
    print("Eliminado con exito.")
    input()

def agregarEntrada():
    """Agrega entrada nueva"""

    while True:
        nombreProducto = input('Ingrese nueva entrada: ').capitalize()
        valorProducto = (input('Precio para '+ nombreProducto + "?: "))
        if valorProducto.isdigit():
            valorProducto = int(valorProducto)
        else:
            print()
            print('Error! Ingrese un valor valido.')
            input()
            break

        entradas[nombreProducto] = valorProducto
        print("Agregado con exito.")
        input()
        break

def quitarEntrada():
    """Quita entrada existente"""

    print(' ____________')
    print('|  Entradas  |')
    print()
    for x in entradas:
        print(x, entradas[x])
    print()     
    opcionQuitar = input("Ingrese cual desea quitar? ")
    error = "No existe"
    entradas.pop(opcionQuitar.capitalize(), error)
    print("Eliminado con exito.")
    input()

def agregarPrincipal():
    """Agrega plato principal nuevo"""

    while True:
        nombreProducto = input('Ingrese nuevo plato principal: ').capitalize()
        valorProducto = (input('Precio para '+ nombreProducto + "?: "))
        if valorProducto.isdigit():
            valorProducto = int(valorProducto)
        else:
            print()
            print('Error! Ingrese un valor valido.')
            input()
            break

        principales[nombreProducto] = valorProducto
        print("Agregado con exito.")
        input()
        break

def quitarPrincipal():
    """Quita plato principal existente"""

    print(' _______________')
    print('|  Principales  |')
    print()
    for x in principales:
        print(x, principales[x])
    print()     
    opcionQuitar = input("Ingrese cual desea quitar? ")
    error = "No existe"
    principales.pop(opcionQuitar.capitalize(), error)
    print("Eliminado con exito.")
    input()

def agregarPizza():
    """Agrega pizza nueva"""

    while True:
        nombreProducto = input('Ingrese nueva pizza: ').capitalize()
        valorProducto = (input('Precio para '+ nombreProducto + "?: "))
        if valorProducto.isdigit():
            valorProducto = int(valorProducto)
        else:
            print()
            print('Error! Ingrese un valor valido.')
            input()
            break

        pizzas[nombreProducto] = valorProducto
        print("Agregado con exito.")
        input()
        break

def quitarPizza():
    """Quita pizza existente"""

    print(' __________')
    print('|  Pizzas  |')
    print()
    for x in pizzas:
        print(x, pizzas[x])
    print()     
    opcionQuitar = input("Ingrese cual desea quitar? ")
    error = "No existe"
    pizzas.pop(opcionQuitar.capitalize(), error)
    print("Eliminado con exito.")
    input()

def agregarPostre():
    """Agrega postre nuevo"""

    while True:
        nombreProducto = input('Ingrese nuevo postre: ').capitalize()
        valorProducto = (input('Precio para '+ nombreProducto + "?: "))
        if valorProducto.isdigit():
            valorProducto = int(valorProducto)
        else:
            print()
            print('Error! Ingrese un valor valido.')
            input()
            break

        postres[nombreProducto] = valorProducto
        print("Agregado con exito.")
        input()
        break

def quitarPostre():
    """Quita postre existente"""

    print(' ___________')
    print('|  Postres  |')
    print()
    for x in postres:
        print(x, postres[x])
    print()     
    opcionQuitar = input("Ingrese cual desea quitar? ")
    error = "No existe"
    postres.pop(opcionQuitar.capitalize(), error)
    print("Eliminado con exito.")
    input()

menuPrincipal()