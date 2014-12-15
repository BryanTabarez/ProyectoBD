class Cita():
    """Clase Cita (id_horario, numero_historia, asistencia, tipoSolicitud)"""
    def __init__(self, id_horario, numero_historia, asistencia, tipoSolicitud):
        self.__id_horario = id_horario
        self.__numero_historia = numero_historia
        self.__asistencia = asistencia
        self.__tipoSolicitud = tipoSolicitud

    def get_id_horario(self):
        return self.__id_horario

    def get_numero_historia(self):
        return self.__numero_historia

    def get_asistencia(self):
        return self.__asistencia

    def get_tipo_solicitud(self):
        return self.__tipoSolicitud

    def set_asistencia(self, asistencia):
        self.__asistencia = asistencia

    def set_tipo_solicitud(self, tipoSolicitud):
        self.__tipoSolicitud = tipoSolicitud