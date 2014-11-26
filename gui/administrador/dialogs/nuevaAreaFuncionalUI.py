from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from nuevaAreaUI import Ui_dialogNuevaArea

class DialogNuevaArea( QDialog ):

	def __init__( self, parent=None ):

		"""
			Se llama al constructr de la clase padre indicando que este es contenedor de mas
			alto nivel pasando como argumento parent = None por defecto
			
			Pero en este caso el contenedor padre de este es InterfazAdministrador
			por lo tanto al momento de instanciar un objeto de tipo DialogNuevaArea
			se debe pasar al constructor de este el objeto padre (InterfazAdministrador)

		"""
		QWidget.__init__( self, parent )


		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_dialogNuevaArea()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar los eventos que se generen 
			en la interfaz de administrador
		"""



