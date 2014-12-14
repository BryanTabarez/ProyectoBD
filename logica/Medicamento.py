class Medicamento():
    """Clase Medicamento"""
    def __init__(self, codigo, costo, nombre, descripcion):
        self.__codigo = codigo
        self.__costo = costo
        self.__nombre = nombre
        self.__descripcion = descripcion

    def get_codigo(self):
        return self.__codigo

    def get_costo(self):
        return self.__costo

    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def set_costo(self, costo):
        self.__costo = costo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion