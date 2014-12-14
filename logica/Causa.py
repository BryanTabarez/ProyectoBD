class Causa():
    """Clase Causa( [{codigo,} nombre, descripcion] )"""
    def __init__(self, *args):
        if len(args) is 3:
            self.__codigo = args[0]
            self.__nombre = args[1]
            self.__descripcion = args[2]
        if len(args is 2):
            self.__nombre = args[0]
            self.__descripcion = args[1]

    def get_codigo(self):
        return self.__codigo

    def get_nombre(self):
        return self.__nombre

    def get_descripcion(self):
        return self.__descripcion

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
