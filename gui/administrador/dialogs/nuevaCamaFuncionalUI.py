from PyQt4.QtGui import *
from PyQt4.QtCore import *

from nuevaCamaUI import Ui_dialogNuevaCama

class DialogNuevaCama( QDialog ):

	def __init__(self, parent=None):

		"""
			Se llama al constructor de la clase padre indicando que este es 
			el contenedor de mas alto nivel pasando como argumento parent = None
			por defecto

			Pero en este caso el contendor padre de este es IntefazAdministrador
			por lo tanto al momento de instanciar un objeto de tipo DialogNuevaCama
			se debe pasar al contructor de este el objeto padre (IntefazAdministrador)
		"""
		QWidget.__init__( self, parent )

		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_dialogNuevaCama()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar los eventos que se generen 
			en el dialogo nueva cama
		"""