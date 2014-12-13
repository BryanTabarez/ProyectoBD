from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic




#_____________________________________________________  Agendar Cita Medico _________________________________________

DialogAgendarCitaInterfaz_clas, DialogAgendarCitaInterfazBase = uic.loadUiType('gui/enfermera/uis/DialogAgendarCita.ui')

class DialogAgendarCita( QDialog, DialogAgendarCitaInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )
		
		
#______________________________________________________ Cancelar Cita Paciente _______________________________________

DialogCancelarCitaPacienteInterfaz_class, DialogCancelarCitaPacienteInterfazBase_class = uic.loadUiType('gui/enfermera/uis/DialogCancelarCitaPaciente.ui')

class DialogCancelarCitaPaciente( QDialog, DialogAgendarCitaPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )

#______________________________________________________ Modificar Agenda Medicos _______________________________________

ModificarAgendaMedicosInterfaz_class, ModificarAgendaMedicosInterfazBase_class = uic.loadUiType('gui/enfermera/uis/DialogModificarAgendaMedicos.ui')

class DialogModficarAgendaMedicos( QDialog, ModificarAgendaMedicosInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )

#______________________________________________________ Modificar Paciente _______________________________________

DialogModificarPacienteInterfaz_class, DialogModificarPacienteInterfazBase_class = uic.loadUiType('gui/enfermera/uis/DialogModificarPaciente.ui')

class DialogModificarPaciente( QDialog, DialogModificarPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )

#______________________________________________________ Modificar Paciente _______________________________________

DialogNuevaCitaPacienteInterfaz_class, DialogNuevaCitaPacienteInterfazBase_class = uic.loadUiType('gui/enfermera/uis/DialogNuevaCitaPaciente.ui')

class DialogNuevaCitaPaciente( QDialog, DialogNuevaCitaPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )


#______________________________________________________ Nuevo Paciente _______________________________________

DialogNuevoPacienteInterfaz_class, DialogNuevoPacienteInterfazBase_class = uic.loadUiType('gui/enfermera/uis/DialogNuevoPaciente.ui')

class DialogNuevoPaciente( QDialog, DialogNuevaoPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )