#from logica.Persona import Persona


class Empleado(object):
    """Clase Empleado que hereda de Persona"""
    def __init__(self, identificacion, nombre, direccion, telefono,
        codigo_area, email, salario, id_jefe):
        #super(Empleado, self).__init__(identificacion, nombre, direccion,
            #telefono)
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__direccion = direccion
        self.__telefono = telefono
        self.__codigo_area = codigo_area
        self.__email = email
        self.__salario = salario
        self.__id_jefe = id_jefe

        def get_codigo_area(self):
            return self.__codigo_area

        def get_email(self):
            return self.__email

        def get_salario(self):
            return self.__salario

        def get_id_jefe(self):
            return self.__id_jefe

        def set_codigo_area(self, codigo_area):
            self.__codigo_area = codigo_area

        def set_email(self, email):
            self.__email = email

        def set_salario(self, salario):
            self.__salario = salario

        def set_id_jefe(self, id_jefe):
            self.__id_jefe = id_jefe

        def get_nombre(self):
            return self.__nombre

        # METODOS DE PERSONA // BORRAR PRUEBA

        def get_identificacion(self):
            return self.__identificacion

        def get_telefono(self):
            return self.__telefono

        def get_direccion(self):
            return self.__direccion

