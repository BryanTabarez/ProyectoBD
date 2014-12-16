# NO IMPORTAR TODO | SELECCIONAR SOLO LOS NECESARIOS
from accesoDatos import DaoEnfermera
from logica import Enfermera
#from logica import Medico
#from accesoDatos import DaoMedico


#============= METODO PARA MOSTRAR LAS EXCEPCIONES DE psycopg2 ==================
def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))
#================================================================================


class ControlDaosEmpleados():

	def __init__(self, conexion):
		# LLAMAR LOS CONTRUCTORES PARA DAOS DE EMPLEADOS-> ENFERMERA Y MEDICO
		self.daoEnf = DaoEnfermera(conexion)

	#============================== INSERTAR ENFERMERA ==========================
	def insertarEnfermera (self, identificacion, nombre, direccion, telefono, codigo_area, email, 
		salario, id_jefe, anhos_experiencia, habilidades):
		enfermerita = Enfermera(identificacion, nombre, direccion, telefono, codigo_area, email, 
			salario, id_jefe, anhos_experiencia, habilidades)
		insertarEnf = self.daoEnf.guardarEnfermera(enfermerita)
		if insertarEnf is 0:
			print "INSERCION EXITOSA!"
		if isinstance(insertarEnf, Exception):
			mostrarReturn(insertarEnf)
	#============================================================================

	#============================== CONSULTAR ENFERMERA =========================
	def consultarDatosEnfermera (self, identificacion):
		enfe = self.daoEnf.consultarEnfermera(identificacion)
		print "tipo de lo qeu esta retoranndo"
		print type( enfe )
		if enfe is 1:
			print "NO RESULTADOS!"
		if isinstance(enfe, Enfermera):
			print "CONSULTA EXITOSA!"
		if isinstance(enfe, Exception):
			mostrarReturn(enfe)
	#============================================================================
