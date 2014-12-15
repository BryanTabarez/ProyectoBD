from accesoDatos import DaoArea
from logica import Area

def mostrarReturn(resultado):
    if resultado is not None:
        print("\nExcepcion capturada! Falta Implementar!!")
        print((resultado.pgerror))

class ControlDaoArea():

	def __init__(self, conexion):
		self.daoArea = DaoArea(conexion)

	def insertarArea(self, nombre, descripcion):
		area = Area(nombre, descripcion)
		insertArea = self.daoArea.guardarArea(area)
		if insertArea is 0:
			print "INSERCION EXITOSA!"
		if isinstance(insertArea, Exception):
			mostrarReturn(insertArea)