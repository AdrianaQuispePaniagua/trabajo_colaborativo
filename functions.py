
    
def agregar_contacto(contactos):
    while True:
        nombre = input("ingrese  Nombre").capitalize()
        if len(nombre)>2:
            print("el nombre ingresado es valido.")
            
            break
        else:
            print("el nombre tiene que tener mas de 3 caracteres ")

    while   True:
        try:

            telefono = (input(" ingrese el telefono"))
            if len(telefono)==9:
                telefono=int(telefono)
                print("el telefono ingresado es valido")
                
                break
            else:
                print("el telefono ingresado tiene que tener 9 digitos")
        except:
            print("tiene que ser numeros ") 
    while True:
        email = input(" ingrese el email")
        if len(email)>3 and "@" in email:
            print("email ingresado correctamente.")
            break
        else:
            print("email ingresado tiene que tener un @")


    
    
    contactos.append([nombre,telefono,email])
    
    

def mostrar_contactos(lista_contactos):
    
    if lista_contactos ==[]:
        print("no existe contacto registrado")
    else:
        for contactos in lista_contactos:
            print(f"nombre: {contactos[0]}, telefono: {contactos[1]}, email: {contactos[2]}")    

def buscar_contacto(lista):
    if lista == []:
        print('No existen contactos registrados')
    else:   
        contacto = input('Ingrese nombre de contacto que quiere buscar: ').capitalize()
        while contacto == '':
            contacto = input('Error. Debe ingresar un nombre válido')
        nombre = ''
        telefono = 0
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
                

    