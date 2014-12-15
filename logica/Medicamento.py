class Medicamento():
    """Clase Medicamento"""
    def __init__(self, *args):
        if len(args) is 4:
            self.__codigo = args[0]
            self.__costo = args[1]
            self.__nombre = args[2]
            self.__descripcion = args[3]

        if len(args) is 3:
            self.__costo = args[0]
            self.__nombre = args[1]
            self.__descripcion = args[2]

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