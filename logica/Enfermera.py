import Empleado

class Enfermera(Empleado):
    """Clase Enfermera que hereda de Empleado"""
    def __init__(self, anhos_experiencia):
        super(Enfermera, self).__init__()
        self.__anhos_experiencia = anhos_experiencia
        self.__habilidades = []

    def get_anhos_experiencia(self):
        return self.__anhos_experiencia

    def get_habilidades(self):
        return self.__habilidades

    def set_anhos_experiencia(self, anhos):
        self.__anhos_experiencia = anhos

    def agregar_habilidad(self, habilidad):
        self.__habilidades.append(habilidad)
