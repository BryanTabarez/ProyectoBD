class Area():
    """Clase Area"""
    def __init__(self, codigo_area, nombre_area, descripcion):
        self.__codigo_area = codigo_area
        self.__nombre_area = nombre_area
        self.__descripcion = descripcion

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
