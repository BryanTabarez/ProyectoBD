from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from componentes_enfermera import DialogPaciente
from componentes_enfermera import WidgetListarPacientes

from componentes_enfermera import DialogAsignarCama
from componentes_administrador import WidgetListarCamas

from componentes_administrador import DialogInformacion


#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazEnfermera

#==============================================> INETRAFZ ENFERMERA <===================================================

Interfaz_E_class , Interfaz_E_Base_class = uic.loadUiType( 'gui/enfermera_uis/MainWindowEnfermera.ui' )

class InterfazEnfermera( QMainWindow, Interfaz_E_class ):

	def __init__( self, parent=None ):


		#Constructor padre
		QMainWindow.__init__( self, parent )
		#Consfiguracion interfaz
		self.setupUi( self )


		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )


		#================================================> VARIABLES 
		self.controladorPaciente = "controladorPacientes" #AQUI VAN LOS CONTROLADORES
		self.controladorCama = "controladorCama"
		#================================================> WIDGETS  
		self.dialogInformacion = DialogInformacion( self )
		self.widgetListarPacientes = WidgetListarPacientes( self.widgetCuerpo )
		self.widgetListarPacientes.hide()

		self.widgetListarCamas = WidgetListarCamas( self.widgetCuerpo )
		self.widgetListarCamas.hide()
		
	
		#================================================> SENIALES Y SLOTS <===========================================
		
		#===================================================> PACIENTE 
		self.connect( self.commandLinkButtonNuevoPaciente, SIGNAL( "clicked()" ), self.nuevoPaciente )
		self.connect( self.commandLinkButtonModificarPaciente, SIGNAL( "clicked()" ), self.modificarPaciente )
		self.connect( self.commandLinkButtonEliminarPaciente, SIGNAL( "clicked()" ), self.eliminarPaciente )
		self.connect( self.commandLinkButtonListarPacientes, SIGNAL( "clicked()" ), self.listarPacientes )
		#===================================================> CAMAS 
		self.connect( self.commandLinkButtonAsignarCama, SIGNAL( "clicked()" ), self.asignarCama )
		self.connect( self.commandLinkButtonLiberarCama, SIGNAL( "clicked()" ), self.liberarCama )
		#===================================================> CAMAS 


	#===================================================> METODOS <=====================================================
	
	#===================================================> PACIENTE
	def nuevoPaciente( self ):

		dialogNuevoPaciente = DialogPaciente( controlador=self.controladorPaciente , parent=self )
		dialogNuevoPaciente.exec_()

	def modificarPaciente( self ):

		dialogModificarPaciente = DialogPaciente( nuevo_registro=False, controlador=self.controladorPaciente, parent=self)
		dialogModificarPaciente.exec_()	

	def eliminarPaciente( self ):

		fila_seleccionada = self.widgetListarPacientes.tableWidgetPacientes.currentRow()
		if self.widgetListarPacientes.isHidden() or fila_seleccionada == -1:
			
			self.dialogInformacion.showMensaje( "Modificar Paciente", 
				"Por favor liste los pacientes, seleccione de la tabla el que desea modificar"
				", luego presione 'Modificar Paciente'" )
			
		else:

			#AQUI SE ELIMINA EL PACIENTE
			id_paciente_eliminar = self.widgetListarPacientes.tableWidgetPacientes.item(fila_seleccionada, 0).text()
			print( "PACEINTE ELIMINADO: " + id_paciente_eliminar )

			
	def listarPacientes( self ):

		self.widgetListarPacientes.show()
		self.widgetListarCamas.hide()

	#===================================================> CAMAS 
	def asignarCama( self ):

		dialogAsignarCama = DialogAsignarCama( 
			controladorPaciente= self.controladorPaciente,
			controladorCama=self.controladorCama, parent=self )
		dialogAsignarCama.exec_()

	def liberarCama( self ):

		dialogLiberarCama = DialogAsignarCama( asignar=False, 
			controladorPaciente= self.controladorPaciente,
			controladorCama=self.controladorCama, parent=self )
		dialogLiberarCama.exec_()

	def listarCamas( self ):

		self.widgetListarPacientes.hide()
		self.widgetListarCamas.show()


	#===================================================> CITAS <=======================================================
		






