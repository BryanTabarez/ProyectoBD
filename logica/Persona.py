class Persona:
    """Clase base Persona"""
    def __init__(self, identificacion, nombre, direccion, telefono):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion

    def set_identificacion(self, id):
        self.__identificacion = id

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre
