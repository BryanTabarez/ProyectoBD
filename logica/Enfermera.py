from logica.Empleado import Empleado


class Enfermera(Empleado):
    """Clase Enfermera que hereda de Empleado"""
    def __init__(self, identificacion, nombre, direccion, telefono, codigo_area,
        email, salario, id_jefe, anhos_experiencia, habilidades):
        super(Enfermera, self).__init__(identificacion, nombre, direccion,
            telefono, codigo_area, email, salario, id_jefe)
        self.__anhos_experiencia = anhos_experiencia
        self.__habilidades = habilidades

    def get_anhos_experiencia(self):
        return self.__anhos_experiencia

    def get_habilidades(self):
        return self.__habilidades

    def set_anhos_experiencia(self, anhos):
        self.__anhos_experiencia = anhos


    def set_habilidad(self, habilidad):
        self.__habilidades = habilidad
