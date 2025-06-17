from functions import *
import os
import time
os.system('cls')


# lista principal de contactos
lista_contactos = []

bandera_de_ejecucion_incorrecta = True
while bandera_de_ejecucion_incorrecta:
    print("---APLICACION MINI AGENDA DE CONTACTOS--")
    print("1.Agregar un contacto: nombre, teléfono, email")
    print("2.Lista de contactos guardados") 
    print("3.Buscar un contacto por nombre")
    print("4.Eliminar un contacto")
    print("5.Salir del programa")
    print("Para ingresar al menu debe elegir o ingresar un número entero del 1 al 5. Gracias")
    try:
        opcion = int(input("Ingrese el número de la opción del menú que deseas seleccionar: "))
        if opcion == 1:
            agregar_contacto(lista_contactos)
        elif opcion == 2:
            mostrar_contactos(lista_contactos)
        elif opcion == 3:
            os.system('cls')
            buscar_contacto(lista_contactos)
        elif opcion == 4:
            os.system('cls')
            eliminar_contacto(lista_contactos)
        elif opcion == 5:
            bandera_de_ejecucion_incorrecta = False
            print("Gracias por utilizar la aplicación. Hasta pronto!")
    except Exception:
        print("La opción ingresada es invalida. Intente nuevamente")
    # pausa
    time.sleep(1)