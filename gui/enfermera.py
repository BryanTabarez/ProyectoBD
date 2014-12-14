from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from componentes_enfermera import DialogAgendarCita
from componentes_enfermera import DialogCancelarCitaPaciente
from componentes_enfermera import DialogModificarAgendaMedicos
from componentes_enfermera import DialogModificarPaciente
from componentes_enfermera import DialogNuevaCitaPaciente
from componentes_enfermera import DialogNuevoPaciente

InterfazEnfermeraInterfaz_class , InterfazEnfermeraInterfazBase_class = uic.loadUiType( 'gui/enfermera_uis/VentanaEnfermera.ui' )

class InterfazEnfermera( QMainWindow, InterfazEnfermeraInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QMainWindow.__init__( self, parent )
		self.setupUi( self )


		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )

	
	"""
			SENIALES Y SLOTS			
	"""	


	#Metodo: nuevaCita
	#Funcion: Permite mostrar la interfaz que  enlaza una cita con el paciente
	def nuevaCita( self ):
		dialogNuevaCitaPaciente = DialogNuevaCitaPaciente( self )
		dialogNuevaCitaPaciente.exec_()


	#Metodo: cancelarCita
	#Funcion: Permite mostrar la interzar para cancelacion de citas 
	def cancelarCita( self ):
		dialogCancelarCita = DialogCancelarCita( self )
		dialogCancelarCita.exec_()

	#Metodo: listarCitas
	#Funcion: Permite listar citas que se han creado en la base de datos
	def listarCitas( self ):
		"""FALTA"""
		pass

	#Metodo: nuevoPaciente
	#Funcion: Permite mostrar la interfaz para creacion de pacientes en la base de datos
	def nuevoPaciente( self ):
		dialogNuevoPaciente = DialogNuevoPaciente( self )
		dialogNuevoPaciente.exec_()

	#Metodo: modificarPaciente
	#Funcion: Permite modificar un paciente ya creado en la base de datos
	def modificarPaciente( self ):
		dialogModificarPaciente = DialogModificarPaciente( self )
		dialogModificarPaciente.exec_()

	#Metodo: listarPacientes
	#Funcion: Permite listar pacientes de la base de datos
	def listarPacientes( self ):
		"""FALTA"""
		pass




