from . import Empleado


class Medico(Empleado):
    """Clase Medico que hereda de Empleado"""
    def __init__(self, especialidad, universidad, num_licencia):
        super(Medico, self).__init__()
        self.__especialidad = especialidad
        self.__universidad = universidad
        self.__num_licencia = num_licencia

        def get_especialidad(self):
            return self.__especialidad

        def get_universidad(self):
            return self.__universidad

        def get_num_licencia(self):
            return self.__num_licencia

        def set_especialidad(self, especialidad):
            self.__especialidad = especialidad

        def set_universidad(self, universidad):
            self.__universidad = universidad

        def set_num_licencia(self, num_licencia):
            self.__num_licencia = num_licencia
