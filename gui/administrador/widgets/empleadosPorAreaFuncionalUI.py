from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from empleadosPorAreaUI import Ui_widgetEmpleadosPorArea

class WidgetEmpleadosPorArea( QWidget ):

	def __init__( self, parent=None ):

		"""
			Se llama al constructor de la clase padre indicando que este es el 
			contenedor de mas alto nivel pasando como argumento parent = Nonet
			por defecto

			Pero en este caso el contenedor padre de este es InterfazAdministrador
			por lo tanto al momento de instanciar un objeto de tipo WidgetEmpleadosPorArea
			se debe pasar al contructor de este el objeto padre InterfazAdministrador

		"""
		QWidget.__init__( self, parent )

		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_widgetEmpleadosPorArea()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar los eventos que se generen 
			en la interfaz de administrador
		"""