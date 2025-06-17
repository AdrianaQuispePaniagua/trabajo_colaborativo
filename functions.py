def agregar_contacto(lista_contactos):
    # TODO: logica agregar contacto. Borrar 'pass'
    pass

def mostrar_contactos(lista_contactos):
    # TODO: logica mostrar todos los contactos. Borrar 'pass'
    pass

def buscar_contacto(lista):
    if lista == []:
        print('No existen contactos registrados')
    else:   
        contacto = input('Ingrese nombre de contacto que quiere buscar: ').capitalize()
        while contacto == '':
            contacto = input('Error. Debe ingresar un nombre válido')
        nombre = ''
        telefono = ''
        mail = ''
        for contactos in lista:
            if contacto not in contactos:
                print('Contacto no encontrado')      
            if contacto in contactos:
                nombre = contactos[0]
                telefono = contactos[1]
                mail = contactos[2]
                break
        print(f'Nombre: {nombre}')
        print(f'Telefono: {telefono}')
        print(f'Mail: {mail}')
        
def eliminar_contacto(lista):
    if lista == []:
        print('No existen contactos registrados')
    else:   
        contacto = input('Ingrese nombre de contacto que desea borrar: ').capitalize()
        while contacto == '':
            contacto = input('Error. Debe ingresar un nombre válido')
        for i in lista:
            if contacto not in i:
                print('Contacto no encontrado') 
            if contacto in i:
                lista.remove(i)
                break
                    
        print(f'{contacto} borrado')
                

    