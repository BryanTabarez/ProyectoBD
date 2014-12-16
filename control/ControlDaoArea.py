from accesoDatos import DaoArea
from logica import Area

#============= METODO PARA MOSTRAR LAS EXCEPCIONES DE psycopg2 ==================
def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))
#================================================================================


class ControlDaoArea():
	"""Clase ControlDaoArea"""
	def __init__(self, conexion):
		self.daoArea = DaoArea(conexion)

	#============================== INSERTAR ====================================
	def insertarArea(self, codigo, nombre, descripcion):
		area = Area(codigo, nombre, descripcion)
		insertArea = self.daoArea.guardarArea(area)
		if insertArea is 0:
			print "INSERCION EXITOSA!"
		if isinstance(insertArea, Exception):
			mostrarReturn(insertArea)
	#============================================================================

	#============================== CONSULTAR ===================================
	def buscarArea(self, nombre):
		area = self.daoArea.consultarArea(nombre)
		if isinstance(area, Exception):
			mostrarReturn(area)
		if area == 1:
			print("LA CONSULTA NO ARROJO RESULTADOS :(")
			return "", ""
		else:
			return str(area.get_codigo_area()), area.get_descripcion()
	#============================================================================

	#============================== MODIFICAR ===================================
	def actualizarArea(self, codigo, nombre, descripcion):
		area = Area(codigo, nombre, descripcion)
		modArea = self.daoArea.modificarArea(area)
		if modArea is 0:
			print "MODIFICACION EXITOSA!"
		if isinstance(modArea, Exception):
			mostrarReturn(modArea)
	#============================================================================

	#============================== ELIMINAR ====================================
	def eliminarArea(self, codigo):
		delArea = self.daoArea.borrarArea(codigo)
		if delArea is 0:
			print "ELIMINACION EXITOSA!"
		if isinstance(delArea, Exception):
			mostrarReturn(delArea)
	#============================================================================