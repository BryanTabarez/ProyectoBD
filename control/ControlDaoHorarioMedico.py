
from accesoDatos import DaoHorarioMedico



class ControlDaoHorarioMedico():

	def __init__( self, conexion ):

		self.daoHorarioMedico = DaoHorarioMedico( conexion )


	#=======================> OBTENER HORARIOS DE MEDICOS POR ESPECIALIDAD

	def consultarHorariosMedicosPorEspecialidad( self, especialidad ):

		horarios_medicos = self.daoHorarioMedico.consultarHorariosMedicosPorEspecialidad( especialidad )
		return horarios_medicos

	def cambiarEstadoHorario( self, id_horario, disponible ):

		cambia_estado = self.daoHorarioMedico.cambiarEstadoHorario(id_horario,disponible)
		return cambia_estado

	def insertarHorarios(self, id_medico, fecha):

		horaros = self.daoHorarioMedico.insertarHorarios(id_medico, fecha)
		return horarios


