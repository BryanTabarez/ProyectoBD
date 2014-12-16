# NO IMPORTAR TODO | SELECCIONAR SOLO LOS NECESARIOS
from accesoDatos import DaoEnfermera
from logica import Enfermera
import psycopg2
#from logica import Medico
#from accesoDatos import DaoMedico


#============= METODO PARA MOSTRAR LAS EXCEPCIONES DE psycopg2 ==================
def mostrarReturn(resultado):
    if isinstance(resultado, psycopg2.Error):
        "ERROR DE BASE DE DATOS!"
    if resultado is not None:
        print("\nOTRO TIPO DE ERROR!")
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
		if enfe is 1:
			print "NO RESULTADOS!"
		if isinstance(enfe, Enfermera):
			
			# Datos personales
			e = [ str(enfe.get_identificacion()) ]
			e.append( enfe.get_nombre() )
			e.append( enfe.get_direccion() )
			e.append( enfe.get_telefono())
			# Datos de empleado
			e.append( str(enfe.get_codigo_area()) )
			e.append( enfe.get_email() )
			e.append( enfe.get_salario() )
			e.append( str(enfe.get_id_jefe()) )
			# Datos Enfermera
			e.append( str(enfe.get_anhos_experiencia()) )

			return e
		if isinstance(enfe, Exception):
			mostrarReturn(enfe)
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
