from accesoDatos import DaoEnfermera
from logica import Enfermera
#from logica import Medico
#from accesoDatos import DaoMedico


class ControlDaosEmpleados():

	def __init__(self, conexion):
		# LLAMAR LOS CONTRUCTORES PARA DAOS DE EMPLEADOS-> ENFERMERA Y MEDICO
		self.conexion = conexion # ES NECESARIO PARA QUE LA OBTENGAN LOS WIDG DE EMPLEADO...
		self.daoEnf = DaoEnfermera(conexion)

	#============================== INSERTAR ENFERMERA ==========================
	def insertarEnfermera (self, identificacion, nombre, direccion, telefono, codigo_area, email,
		salario, id_jefe, anhos_experiencia, habilidades):
		enfermerita = Enfermera(identificacion, nombre, direccion, telefono, codigo_area, email,
			salario, id_jefe, anhos_experiencia, habilidades)
		insertarEnf = self.daoEnf.guardarEnfermera(enfermerita)
		if insertarEnf is 0:
			return "Se inserto el registro de enfermera"
		if isinstance(insertarEnf, Exception):
			return insertarEnf.pgerror
	#============================================================================

	#============================== CONSULTAR ENFERMERA =========================
	# Devuelve un String o una lista con los datos de la consulta
	def consultarDatosEnfermera (self, identificacion):
		enfe = self.daoEnf.consultarEnfermera(identificacion)
		if enfe is 1:
			return "NO RESULTADOS!"
		if isinstance(enfe, Enfermera):
			
			# Datos personales
			e = [ str(enfe.get_identificacion()) ]
			e.append( enfe.get_nombre() )
			e.append( enfe.get_direccion() )
			e.append( enfe.get_telefono() )
			# Datos de empleado
			e.append( str(enfe.get_codigo_area()) )
			e.append( enfe.get_email() )
			e.append( enfe.get_salario() )
			e.append( str(enfe.get_id_jefe()) )
			# Datos Enfermera
			e.append( str(enfe.get_anhos_experiencia()) )
			e.append( enfe.get_habilidades() )

			return e

		if isinstance(enfe, Exception):
			return enfe.pgerror

	#============================================================================

	#============================= ELIMINAR ENFERMERA ===========================
	# Siempre retorna un string
	def eliminarEnfermera(self, identificacion):
		resultado = self.daoEnf.borrarEnfermera(identificacion)
		if resultado == 0:
			return "SE REALIZO LA OPERACION!"
		if isinstance(resultado, Exception):
			return resultado.pgerror
	#============================================================================
	

	#============================ INSERTAR MEDICO ===============================
	# def insertarMedico(self, identificacion, nombre, direccion, telefono,
 #    codigo_area, email, salario, id_jefe, especialidad, universidad,
 #    num_licencia):
 #        medico = Medico(identificacion, nombre, direccion, telefono,
 #        codigo_area, email, salario, id_jefe, especialidad, universidad,
 #        num_licencia)
 #        insertarMedico = self.daoMedico.guardarMedico(medico)
 #        if insertarMedico is 0:
 #            print "INSERCION EXITOSA!"
 #        if isinstance(insertarMedico, Exception):
 #            mostrarReturn(insertarMedico)
 #    #============================================================================
