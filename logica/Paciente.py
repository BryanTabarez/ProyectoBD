from logica.Persona import Persona


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
        return self.__num_seg_social

    def set_actividad_economica(self, actividad_economica):
        self.__actividad_economica = actividad_economica

    def set_fecha_nacimiento(self, fecha_nacimiento):
        self.__fecha_nacimiento = fecha_nacimiento

    def set_num_seg_social(self, num_seg_social):
        self.__num_seg_social = num_seg_social
