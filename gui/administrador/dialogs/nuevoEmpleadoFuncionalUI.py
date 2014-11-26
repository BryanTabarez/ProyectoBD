from PyQt4.QtGui import *
from PyQt4.QtCore import *
from nuevoEmpleadoUI import Ui_dialogNuevoEmpleado

class DialogNuevoEmpleado( QDialog ):

	def __init__( self, parent=None ):

		"""
			Se llama al constructor de la clase padre indicando que es el contendeor 
			de mas alto nivel pasando como argumento parent = None al constructor del 
			QWidget

			Pero en este caso como este Dialog esta contenido en el contendeor IntefazAdministrador
			entonces cuando se instancia un objeto   de tipo DialogNuevoEmpleado debe recibir
			como argumento el objeto padre, IntefazAdministrador
		"""

		QWidget.__init__( self, parent )

		"""
			Se usan los atributos y configuraciones hechas en Ui_DialogNuevoEmpleado
			y se aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_dialogNuevoEmpleado()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar los eventos que se generen
			en la interfaz de dialogo de nuevo empleado
		"""