import functions as fn
import time

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
            fn.agregar_contacto(lista_contactos)
        elif opcion == 2:
            fn.mostrar_contactos(lista_contactos)
        elif opcion == 3:
            bandera_nombre_incorrecto = True
            while bandera_nombre_incorrecto:
                nombre_buscado = input("Ingrese el nombre a buscar: ").strip()
                if len(nombre_buscado) > 0:
                    bandera_nombre_incorrecto = False
                else:
                    print("El nombre no puede estar vacio.")
            fn.buscar_contacto(lista_contactos, nombre_buscado)
        elif opcion == 4:
            bandera_nombre_incorrecto = True
            while bandera_nombre_incorrecto:
                nombre_eliminar = input("Ingrese el nombre a eliminar: ").strip()
                if len(nombre_eliminar) > 0:
                    bandera_nombre_incorrecto = False
                else:
                    print("El nombre no puede estar vacio.")
            fn.eliminar_contacto(lista_contactos, nombre_eliminar)
        elif opcion == 5:
            bandera_de_ejecucion_incorrecta = False
            print("Gracias por utilizar la aplicación. Hasta pronto!")
    except Exception:
        print("La opción ingresada es invalida. Intente nuevamente")
    # pausa
    time.sleep(1)