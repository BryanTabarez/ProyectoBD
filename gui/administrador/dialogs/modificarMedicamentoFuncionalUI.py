from PyQt4.QtGui import*
from PyQt4.QtCore import *

from modificarMedicamentoUI import Ui_dialogModificarMedicamento

class DialogModificarMedicamento( QDialog ):

	def __init__( self, parent=None ):

		"""
			Se llama al constructor de la clase padre indicando que este es el contenedor 
			de mas alto nivel pasando como argumento parent = None por defecto

			Por en este caso el contenedor padre de este es InterfazAdministrador
			por lo tanto al momento de instanciar un objeto de tipo DialogModificarMedicamento
			se debe pasar al constructor de este el objeto pare (InterfazAdministrador)

		"""
		QWidget.__init__( self, parent )


		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_dialogModificarMedicamento()
		self.ui.setupUi( self )

		"""
			SENIALES Y SLOTS
			
		"""