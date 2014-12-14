from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from componentes_enfermera import DialogPaciente
from componentes_enfermera import WidgetListarPacientes

from componentes_administrador import DialogInformacion
from componentes_administrador import WidgetListarCamas

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

		
		QMainWindow.__init__( self, parent )
		self.setupUi( self )


		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )


		
		#================================================> WIDGETS  <===================================================
		self.dialogInformacion = DialogInformacion( self )

		self.widgetListarPacientes = WidgetListarPacientes( self.widgetCuerpo )
		self.widgetListarPacientes.hide()

		self.widgetListarCamas = WidgetListarCamas( self.widgetCuerpo )
		self.widgetListarCamas.hide()
		#================================================> CONTROLADORES <==============================================
		self.controladorPaciente = "controladorPacientes"
		self.controladorCama = "controladorCama"


	
		#================================================> SENIALES Y SLOTS <===========================================
		
		#===================================================> PACIENTE 
		self.connect( self.commandLinkButtonNuevoPaciente, SIGNAL( "clicked()" ), self.nuevoPaciente )
		self.connect( self.commandLinkButtonModificarPaciente, SIGNAL( "clicked()" ), self.modificarPaciente )
		self.connect( self.commandLinkButtonEliminarPaciente, SIGNAL( "clicked()" ), self.eliminarPaciente )
		self.connect( self.commandLinkButtonListarPacientes, SIGNAL( "clicked()" ), self.listarPacientes )
		#===================================================> CAMAS 
		self.connect( self.commandLinkButtonAsignarCama, SIGNAL( "clicked()" ), self.asignarCama )
		self.connect( self.commandLinkButtonLiberarCama, SIGNAL( "clicked()" ), self.liberarCama )
		self.connect( self.commandLinkButtonListarCamas, SIGNAL( "clicked()" ), self.listarCamas )


	#===================================================> METODOS <=====================================================
	
	#===================================================> PACIENTE
	def nuevoPaciente( self ):

		dialogNuevoPaciente = DialogPaciente( controlador=self.controladorPaciente , parent=self )
		dialogNuevoPaciente.exec_()

	def modificarPaciente( self ):

		fila_seleccionada = self.widgetListarPacientes.tableWidgetPacientes.currentRow()
		if self.widgetListarPacientes.hide() or fila_seleccionada == -1:

			self.dialogInformacion.showMensaje(
			 "Modificar Paciente", 
				"Por favor liste los pacientes, seleccione de la tabla el que desea modificar"
				", luego presione 'Modificar Paciente'" )
			
		else:

			id_paciente = self.widgetListarPacientes.tableWidgetPacientes.item( fila_seleccionada, 0 ).text()
			dialogModificarPaciente = DialogPaciente( id_paciente=id_paciente, controlador=self.controladorPaciente, parent=self )
			dialogModificarPaciente.exec_()

	

	def eliminarPaciente( self ):

		fila_seleccionada = self.widgetListarPacientes.tableWidgetPacientes.currentRow()
		if self.widgetListarPacientes.hide() or fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Modificar Paciente", 
				"Por favor liste los pacientes, seleccione de la tabla el que desea modificar"
				", luego presione 'Modificar Paciente'" )
			
		else:

			id_paciente_eliminar = self.widgetListarPacientes.tableWidgetPacientes.item.text()
			print( "PACEINTE ELIMINADO: " + id_paciente_eliminar )

			
	def listarPacientes( self ):

		self.widgetListarPacientes.show()

	#===================================================> CAMAS 
	def asignarCama( self ):

		#dialogAsignarCama = DialogAsignarCama( self )
		pass

	def liberarCama( self ):

		fila_seleccionada = self.widgetListarCamas.tableWidgetCamas.currentRow()
		if self.widgetListarCamas.isHidden() or fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Liberar Cama", 
				"Por favor liste las camas, seleccione de la tabla la que desea liberar,"
				" luego presione 'Liberar Cama'" )
			
		else:

			print( "CAMA LIBERADA" )

	def listarCamas( self ):

		self.widgetListarCamas.show()



	#===================================================> CITAS <=======================================================
		






