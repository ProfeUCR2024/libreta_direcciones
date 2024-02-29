import os

class Contacto:
    def __init__(self, nombre,telefono,correo):
        self.nombre = nombre
        self.telefono = telefono
        self.correo = correo

class LibretaDirecciones:
    def __init__(self,archivo):
        self.archivo = archivo
        self.contactos = []
        if os.path.exists(self.archivo):
            self.cargar_contactos()

    def cargar_contactos(self):
        with open(self.archivo, 'r') as f:
            for linea in f:
                nombre, telefono, correo = linea.strip().split(',')
                self.contactos.append(Contacto(nombre,telefono,correo))

    def guardar_contactos(self):
        with open(self.archivo, 'w') as f:
            for contacto in self.contactos:
                f.write(f'{contacto.nombre},{contacto.telefono},{contacto.correo}\n')

    def agregar_contacto(self,nombre,telefono,correo):
        self.contactos.append(Contacto(nombre,telefono,correo))
        self.guardar_contactos()

    def listar_contactos(self):
        for contacto in self.contactos:
            print(f'Nombre: {contacto.nombre}, Telefono: {contacto.telefono}, Correo: {contacto.correo}')