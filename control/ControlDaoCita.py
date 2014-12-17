from accesoDatos import DaoCita
from logica import Cita 


class ControlDaoCita():

	def __init__( self, conexion ):

		self.daoCita = DaoCita( conexion )


	def guardarCita( self, id_horario, numero_historia, asistencia, tipoSolicitud):

		cita = Cita( id_horario, numero_historia, asistencia, tipoSolicitud )
		resultado = self.daoCita.guardarCita( cita )
		return resultado

	def cancelarCita(self, id_horario):
		cancelar  = self.daoCita.cancelarCita( id_horario )
		return cancelar

	def listarCitasPaciente(self, id_paciente):
		listar = self.daoCita.listarCitasPaciente( id_paciente )
		return listar
