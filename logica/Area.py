class Area():
    """Clase Area ( [{codigo_area,} nombre_area, descripcion] )"""
    def __init__(self, *args):
        if len(args) is 3:
            self.__codigo_area = args[0]
            self.__nombre_area = args[1]
            self.__descripcion = args[2]
        if len(args) is 2:
            self.__nombre_area = args[0]
            self.__descripcion = args[1]

    def get_codigo_area(self):
        return self.__codigo_area

    def get_nombre_area(self):
        return self.__nombre_area

    def get_descripcion(self):
        return self.__descripcion

    def set_codigo_area(self, codigo_area):
        self.__codigo_area = codigo_area

    def set_nombre_area(self, nombre):
        self.__nombre_area = nombre

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion
