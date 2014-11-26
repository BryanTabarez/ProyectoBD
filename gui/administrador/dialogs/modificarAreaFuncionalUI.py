from PyQt4.QtGui import *
from PyQt4.QtCore import *
from modificarAreaUI import Ui_dialogModificarArea

class DialogModificarArea( QDialog ):

	def __init__( self, parent=None ):

		"""
			Se llama al contrcutor de la clase padre inidicando que este es 
			el contenedor de mas alto nivel pasando como argumento paren = None
			por defecto

			Pero en este caso el contenedor padre de este es InterfazAdministrador
			por lo tanto al momento de instanciar un objeto de tipo DialogModificarArea
			se debe pasar al constructor de este el objeto padre (InterfazAdministrador)
		"""
		QWidget.__init__( self, parent )


		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_dialogModificarArea()
		self.ui.setupUi( self )

		
		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar los eventos que se generen 
			en la interfaz de administrador
		"""

