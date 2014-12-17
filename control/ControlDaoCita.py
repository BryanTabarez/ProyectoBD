from accesoDatos import DaoCita
from logica import Cita 


class ControlDaoCita():

	def __init__( self, conexion ):

		self.daoCita = DaoCita( conexion )


	def guardarCita( self, id_horario, numero_historia, asistencia, tipoSolicitud):

		cita = Cita( id_horario, numero_historia, asistencia, tipoSolicitud )
		resultado = self.daoCita.guardarCita( cita )
		return resultado

	def eliminarCita( self, id_horario ):
		pass