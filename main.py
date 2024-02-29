from libreta import LibretaDirecciones

def menu():
    print('1. Agregar Contacto')
    print('2. Listar Contactos')
    print('3. Eliminar contacto por correo electronico')
    print('4. Salir')

    opcion = input('Seleccione una opcion: ')
    return opcion

def main():
    libreta = LibretaDirecciones("contactos.txt")

    while True:
        opcion = menu()

        if opcion == '1':
            nombre = input("Nombre: ")
            telefono = input("Telefono: ")
            correo = input("Correo: ")
            libreta.agregar_contacto(nombre,telefono,correo)
            print('Contacto AGREGADO')

        elif opcion == '2':
            print('********LISTA DE CONTACTOS********')
            libreta.listar_contactos()

        elif opcion == '3':
            correo_eliminar = input('Ingrese el correo del contacto que desea eliminar: ')
            if any(contacto.correo == correo_eliminar for contacto in libreta.contactos):
                libreta.contactos = [contacto for contacto in libreta.contactos if contacto.correo != correo_eliminar]
                libreta.guardar_contactos()
                print('*****CONTACTO ELIMINADO*****')
            else:
                print(' No se encontro ningun contacto con ese correo electronico')
        
        elif opcion == '4':
            break

        else:
            print('Opcion Invalida')


if __name__ == '__main__':
    main()