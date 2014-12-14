from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from componentes_enfermera import DialogPaciente
from componentes_enfermera import WidgetListarPacientes
from componentes_administrador import DialogInformacion

#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazEnfermera

#=======================================================================================================================

Interfaz_E_class , Interfaz_E_Base_class = uic.loadUiType( 'gui/enfermera_uis/MainWindowEnfermera.ui' )

class InterfazEnfermera( QMainWindow, Interfaz_E_class ):

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


		self.dialogInformacion = DialogInformacion( self )
		#================================================> WIDGETS LISTAR <=============================================
		self.widgetListarPacientes = WidgetListarPacientes( self.widgetCuerpo )
		self.widgetListarPacientes.hide()

	
		"""
				SENIALES Y SLOTS			
		"""
		#===================================================> PACIENTE <================================================
		self.connect( self.commandLinkButtonNuevoPaciente, SIGNAL( "clicked()" ), self.nuevoPaciente )
		self.connect( self.commandLinkButtonModificarPaciente, SIGNAL( "clicked()" ), self.modificarPaciente )
		self.connect( self.commandLinkButtonEliminarPaciente, SIGNAL( "clicked()" ), self.eliminarPaciente )
		self.connect( self.commandLinkButtonListarPacientes, SIGNAL( "clicked()" ), self.listarPacientes )


	def nuevoPaciente( self ):

		dialogNuevoPaciente = DialogPaciente( parent=self )
		dialogNuevoPaciente.exec_()

	def modificarPaciente( self ):

		fila_seleccionada = self.widgetListarPacientes.tableWidgetPacientes.currentRow()
		if self.widgetListarPacientes.hide() or fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Modificar Paciente", 
				"Por favor liste los pacientes, seleccione de la tabla el que desea modificar, luego presione 'Modificar Paciente'" )
			
		else:

			dialogModificarPaciente = DialogPaciente( "codigo_paciente", "controaldor", self )
			dialogModificarPaciente.exec_()

	def listarPacientes( self ):

		self.widgetListarPacientes.show()

	def eliminarPaciente( self ):

		fila_seleccionada = self.widgetListarPacientes.tableWidgetPacientes.currentRow()
		if self.widgetListarPacientes.hide() or fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Modificar Paciente", 
				"Por favor liste los pacientes, seleccione de la tabla el que desea modificar, luego presione 'Modificar Paciente'" )
			
		else:

			print("PACEINTE ELIMINADO")














