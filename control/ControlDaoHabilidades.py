from accesoDatos import DaoHabilidades
#from logica import Enfermera
#from logica import Medico
#from accesoDatos import DaoMedico


class ControlDaoHabilidades():

	def __init__(self, conexion):
		# LLAMAR LOS CONTRUCTORES PARA DAOS DE EMPLEADOS-> ENFERMERA Y MEDICO
		self.daoHab = DaoHabilidades(conexion)

	def buscarHabilidades(self):
		resultado = self.daoHab.consultarHabilidades()
		return resultado
		if isinstance(resultado, Exception):
			return resultado.pgerror