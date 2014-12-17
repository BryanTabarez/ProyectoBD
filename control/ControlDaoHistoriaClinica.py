from accesoDatos import DaoHistoriaClinica



class ControlDaoHistoriaClinica():

	def __init__( self, conexion ):

		self.daoHistoriaClinica = DaoHistoriaClinica( conexion )

	def consultarNumeroHistoria( self, id_paciente):

		resultado = self.daoHistoriaClinica.consultarNumeroHistoria( id_paciente )
		return resultado
