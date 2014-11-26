from PyQt4.QtGui import *
from PyQt4.QtCore import *

from listarCamasUI import Ui_widgetListarCamas

class WidgetListarCamas( QWidget ):

	def __init__( self, parent=None ):

		"""
			Se llama al constructor de la clase padre indicando que este es 
			el contenedos de mas alto nivel pasando coo argumento parent = None
			por defecto

			Pero en este caso el contenedor padre de este es InterfazAdministrador
			por lo tant al momento de instanciar un objeto de tipo InterfazAdministrador
			se debe pasar al constructor de este el objeto padre (InterfazAdministrador)
		
		"""
		QWidget.__init__( self, parent )

		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""
		self.ui = Ui_widgetListarCamas()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			
		"""
