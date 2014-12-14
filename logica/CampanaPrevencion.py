class CampanaPrevencion():
    """Clase CampanaPrevencion( [{codigo,} id_medico, nombre, fecha_realizacion,
        objetivo] )"""
    def __init__(self, *args):
        if len(args) is 5:
            self.__codigo = args[0]
            self.__id_medico = args[1]
            self.__nombre = args[2]
            self.__fecha_realizacion = args[3]
            self.__objetivo = args[4]
        if len(args) is 4:
            self.__id_medico = args[0]
            self.__nombre = args[1]
            self.__fecha_realizacion = args[2]
            self.__objetivo = args[3]

    def get_codigo(self):
        return self.__codigo

    def get_id_medico(self):
        return self.__id_medico

    def get_nombre(self):
        return self.__nombre

    def get_fecha_realizacion(self):
        return self.__fecha_realizacion

    def get_objetivo(self):
        return self.__objetivo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_id_medico(self, id_medico):
        self.__id_medico = id_medico

    def set_fecha_realizacion(self, fecha_realizacion):
        self.__fecha_realizacion = fecha_realizacion

    def set_objetivo(self, objetivo):
        self.__objetivo = objetivo