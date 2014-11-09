# Modulo que implementa las Clases que corresponden a la capa Logica


class Persona:
    """Clase base Persona"""
    def __init__(self, identificacion, nombre, direccion, telefono):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono

    def get_nombre(self):
        return self.__nombre

    def get_identificacion(self):
        return self.__identificacion

    def get_telefono(self):
        return self.__telefono

    def get_direccion(self):
        return self.__direccion

    def set_direccion(self, direccion):
        self.__direccion = direccion

    def set_telefono(self, telefono):
        self.__telefono = telefono

    def set_nombre(self, nombre):
        self.__nombre = nombre


class Paciente(Persona):
    """Clase Paciente que hereda de Persona"""
    def __init__(self, identificacion, nombre, direccion, telefono,
        fecha_nacimiento, actividad_economica, num_seg_social):
        super(Paciente, self).__init__(identificacion, nombre, direccion,
            telefono)
        self.__fecha_nacimiento = fecha_nacimiento
        self.__actividad_economica = actividad_economica
        self.__num_seg_social = num_seg_social

    def get_fecha_nacimiento(self):
        return self.__fecha_nacimiento

    def get_actividad_economica(self):
        return self.__actividad_economica

    def get_num_seg_social(self):
        return self._num_seg_social


class Empleado(Persona):
    """Clase Empleado que hereda de Persona"""
    def __init__(self, identificacion, nombre, direccion, telefono,
        codigo_area, email, salario, id_jefe):
        super(Empleado, self).__init__(identificacion, nombre, direccion,
            telefono)
        self.__codigo_area = codigo_area
        self.__email = email
        self.__salario = salario
        self.__id_jefe = id_jefe

        def set_codigo_area(self, codigo_area):
            self.__codigo_area = codigo_area

        def set_email(self, email):
            self.__email = email

        def set_salario(self, salario):
            self.__salario = salario

        def set_id_jefe(self, id_jefe):
            self.__id_jefe = id_jefe

        def get_codigo_area(self):
            return self.__codigo_area

        def get_email(self):
            return self.__email

        def get_salario(self):
            return self.__salario

        def get_id_jefe(self):
            return self.__id_jefe


class Medico(Empleado):
    """Clase Medico que hereda de Empleado"""
    def __init__(self, especialidad, universidad, num_licencia):
        super(Medico, self).__init__()
        self.__especialidad = especialidad
        self.__universidad = universidad
        self.__num_licencia = num_licencia

        def set_especialidad(self, especialidad):
            self.__especialidad = especialidad

        def set_universidad(self, universidad):
            self.__universidad = universidad

        def set_num_licencia(self, num_licencia):
            self.__num_licencia = num_licencia

        def get_especialidad(self):
            return self.__especialidad

        def get_universidad(self):
            return self.__universidad

        def get_num_licencia(self):
            return self.__num_licencia


class Enfermera(Empleado):

    def __init__(self, anhos_experiencia):
        super(Enfermera, self).__init__()
        self.__anhos_experiencia = anhos_experiencia
        self.__habilidades = []

    def agregar_habilidad(self, habilidad):
        self.__habilidades.append(habilidad)


class Area():

    def __init__(self):
        super(Area, self).__init__()



# PRUEBAS  (BORRAR)
unPaciente = Paciente(127, "Bryan", "Calle 13", "3122041557",
    "01-27-1994", "Traficante de organos", 1000)

otroPaciente = Paciente(128, "Stiven", "Calle 14", "3122041557",
    "01-01-2000", "Extorsionista", 1234)
