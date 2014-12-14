from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic




#_____________________________________________________  Agendar Cita Medico _________________________________________

DialogAgendarCitaInterfaz_class, DialogAgendarCitaInterfazBase = uic.loadUiType('gui/enfermera_uis/DialogAgendarCita.ui')

class DialogAgendarCita( QDialog, DialogAgendarCitaInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )
		
		
#______________________________________________________ Cancelar Cita Paciente _______________________________________

DialogCancelarCitaPacienteInterfaz_class, DialogCancelarCitaPacienteInterfazBase_class = uic.loadUiType('gui/enfermera_uis/DialogCancelarCitaPaciente.ui')

class DialogCancelarCitaPaciente( QDialog, DialogCancelarCitaPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )

#______________________________________________________ Modificar Agenda Medicos _______________________________________

DialogModificarAgendaMedicosInterfaz_class, DialogModificarAgendaMedicosInterfazBase_class = uic.loadUiType('gui/enfermera_uis/DialogModificarAgendaMedicos.ui')

class DialogModificarAgendaMedicos( QDialog, DialogModificarAgendaMedicosInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )

#______________________________________________________ Modificar Paciente _______________________________________

DialogModificarPacienteInterfaz_class, DialogModificarPacienteInterfazBase_class = uic.loadUiType('gui/enfermera_uis/DialogModificarPaciente.ui')

class DialogModificarPaciente( QDialog, DialogModificarPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )

#______________________________________________________ Modificar Paciente _______________________________________

DialogNuevaCitaPacienteInterfaz_class, DialogNuevaCitaPacienteInterfazBase_class = uic.loadUiType('gui/enfermera_uis/DialogNuevaCitaPaciente.ui')

class DialogNuevaCitaPaciente( QDialog, DialogNuevaCitaPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )


#______________________________________________________ Nuevo Paciente _______________________________________

DialogNuevoPacienteInterfaz_class, DialogNuevoPacienteInterfazBase_class = uic.loadUiType('gui/enfermera_uis/DialogNuevoPaciente.ui')

class DialogNuevoPaciente( QDialog, DialogNuevoPacienteInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QDialog.__init__( self, parent )
		self.setupUi( self )