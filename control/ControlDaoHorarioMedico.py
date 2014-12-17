
from accesoDatos import DaoHorarioMedico
from logica import Medico


class ControlDaoHorarioMedico():

	def __init__( self, conexion ):

		self.daoHorarioMedico = DaoHorarioMedico( conexion )


	#=======================> OBTENER HORARIOS DE MEDICOS POR ESPECIALIDAD

	def consultarHorariosMedicosPorEspecialidad( self, especialidad ):

		horarios_medicos = self.daoMedico.consultarHorariosMedicosPorEspecialidad( especialidad )
		return horarios_medicos