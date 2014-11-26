from PyQt4.QtGui import *
from PyQt4.QtCore import *
from modificarEmpleadoUI import Ui_dialogModificarEmpleado

class DialogModificarEmpleado( QDialog ):

	def __init__( self, parent=None ):

		"""
			Se llama al constructor de la clase padre indicando que es el contenedor de mas 
			alto nivel pasando como argumento parent = None como valor por defecto al constructor
			del QWidget

			Pero en este caso como este Dialog esta contenido en el contenedor InterfazAdministrador
			entonces cuando se instancia un objeto de tipo DialogNuevoEmpleado se debe recibir como 
			argumento el objeto padre , InterfazAdministrador
		"""

		QWidget.__init__( self, parent )

		"""
			Se usand los atributos y configuraciones hechas en  Ui_DialogModificarEmpleado
			y se aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_dialogModificarEmpleado()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS 
			Se definen las seniales y slots que van a administrar los eventos que se generan 
			en la interfaz de dialogo modificar usuario
		"""

