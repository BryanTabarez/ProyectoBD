from PyQt4.QtGui import *
from PyQt4.QtCore import *

from listarMedicamentosUI import Ui_widgetListarMedicamentos

class WidgetListarMedicamentos( QWidget ):

	def __init__( self, parent=None ):

		"""
			Se llama al contructor de la clase padre indicando que este es 
			el contenedor de mas alto nivel pasando como argumento parent = None 
			por defecto

			Pero en este caso el contenedor padre de este es InterfazAdministrador
			por lo tanto al momento de instanciar un objeto de tipo WidgetListarMedicamentos
			se debe pasar al contructor de este el objeto padre (InterfazAdministrador)

		"""
		QWidget.__init__( self, parent )		

		"""
			Se usan los atributos y configuraciones hechas en Ui_widgetListarMedicamentos
			y se le aniaden nuevas funcionalidades en esta clase
		"""
		self.ui = Ui_widgetListarMedicamentos()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			
		"""