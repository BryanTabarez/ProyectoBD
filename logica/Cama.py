class Cama():
    """Clase Cama"""
    """Puesto que Cama tiene num_cama como una secuencia no se debe almacenar
    para ingresar pero si se debe almacenar para la consulta y en todo ademas
    se debe almacenar estado, descripcion, cod_area"""
    def __init__(self, *args):
        if len(args) is 4:
            self.__num_cama = args[0]
            self.__estado = args[1]
            self.__descripcion = args[2]
            self.__cod_area = args[3]
        if len(args) is 3:
            self.__estado = args[0]
            self.__descripcion = args[1]
            self.__cod_area = args[2]

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
