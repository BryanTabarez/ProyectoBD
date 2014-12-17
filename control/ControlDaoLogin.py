from accesoDatos import DaoLogin


class ControlDaoLogin():
	
	def __init__(self, conexion):
		self.daoLogin = DaoLogin(conexion)

	#============================== INSERTAR ====================================
	def iniciarSesionAdministrador(self, identificacion, nombre):
		resultado = self.daoLogin.iniciarSesionAdministrador(identificacion, nombre)
		return resultado

	def iniciarSesionEnfermera(self, identificacion, nombre):
		resultado = self.daoLogin.iniciarSesionEnfermera(identificacion, nombre)
		return resultado
