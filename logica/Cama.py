class Cama():
    """Clase Cama"""
    def __init__(self, num_cama, estado, descripcion, cod_area):
        self.__num_cama = num_cama
        self.__estado = estado
        self.__descripcion = descripcion
        self.__cod_area = cod_area

    def get_num_cama(self):
        return self.__num_cama

    def get_estado(self):
        return self.__estado

    def get_descripcion(self):
        return self.__descripcion

    def get_cod_area(self):
        return self.__cod_area

    def set_num_cama(self, num_cama):
        self.__num_cama = num_cama

    def set_estado(self, estado):
        self.__estado = estado

    def set_descripcion(self, descripcion):
        self.__descripcion = descripcion

    def set_cod_area(self, cod_area):
        self.__cod_area = cod_area
