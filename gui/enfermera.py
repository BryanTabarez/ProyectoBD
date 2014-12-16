from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

#from componentes_enfermera import *

from componentes_administrador import WidgetListarCamas

from componentes_enfermera import DialogPaciente
from componentes_enfermera import WidgetListarPacientes

from componentes_enfermera import DialogCama
from componentes_administrador import WidgetListarCamas

from componentes_enfermera import DialogCita

from componentes_administrador import DialogInformacion
from componentes_enfermera import DialogAgendaMedico

from accesoDatos import *
from control import *



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


		#************************************************************************
		# ABRIR CONEXION EN LA BASE DE DATOS
		self.fachada = FachadaDB()
		conexion = self.fachada.obtenerConexion()
		#************************************************************************
		

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
		self.controladorPaciente = ControlDaoPaciente( conexion )
		self.controladorCama = "controladorCama"
		self.controladorCita = "controladorCita"
		self.controladorAgenda = "controladorAgenda"
		#================================================> WIDGETS  
		self.dialogInformacion = DialogInformacion( self )
		self.widgetListarPacientes = WidgetListarPacientes( controlador=self.controladorPaciente, parent=self.widgetCuerpo )
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
		#====================================================> CITAS
		self.connect( self.commandLinkButtonAsignarCita, SIGNAL( "clicked()" ), self.asignarCita )
		self.connect( self.commandLinkButtonCancelarCita, SIGNAL( "clicked()" ), self.cancelarCita )
		#===================================================> AGENDA MEDICO
		self.connect( self.commandLinkButtonAgendarCita, SIGNAL( "clicked()" ), self.agendaMedico )



	#===================================================> METODOS <=====================================================
	
	#===================================================> PACIENTE
	def nuevoPaciente( self ):

		dialogNuevoPaciente = DialogPaciente( controlador=self.controladorPaciente , parent=self )
		dialogNuevoPaciente.exec_()
		self.widgetListarPacientes.actualizar()

	def modificarPaciente( self ):

		dialogModificarPaciente = DialogPaciente( nuevo_registro=False, controlador=self.controladorPaciente, parent=self)
		dialogModificarPaciente.exec_()	
		self.widgetListarPacientes.actualizar()

	def eliminarPaciente( self ):

		fila_seleccionada = self.widgetListarPacientes.tableWidgetPacientes.currentRow()
		if self.widgetListarPacientes.isHidden() or fila_seleccionada == -1:
			
			self.dialogInformacion.showMensaje( "Modificar Paciente", 
				"Por favor liste los pacientes, seleccione de la tabla el que desea modificar"
				", luego presione 'Modificar Paciente'" )
			
		else:

			#AQUI SE ELIMINA EL PACIENTE
			id_paciente_eliminar = str(self.widgetListarPacientes.tableWidgetPacientes.item(fila_seleccionada, 0).text())
			resultado = self.controladorPaciente.borrarPaciente( id_paciente_eliminar )

			self.dialogInformacion.showMensaje( "Eliminar Paciente", resultado )
			self.widgetListarPacientes.actualizar()

			
	def listarPacientes( self ):

		self.widgetListarPacientes.show()
		self.widgetListarPacientes.actualizar()
		self.widgetListarCamas.hide()

	#===================================================> CAMAS 
	def asignarCama( self ):

		dialogAsignarCama = DialogCama( 
			controladorPaciente= self.controladorPaciente,
			controladorCama=self.controladorCama, parent=self )
		dialogAsignarCama.exec_()

	def liberarCama( self ):

		dialogLiberarCama = DialogCama( asignar=False, 
			controladorPaciente= self.controladorPaciente,
			controladorCama=self.controladorCama, parent=self )
		dialogLiberarCama.exec_()

	def listarCamas( self ):

		self.widgetListarPacientes.hide()
		self.widgetListarCamas.show()


	#===================================================> CITAS

	def asignarCita( self ):

		dialogAsignarCita = DialogCita( controlador=self.controladorCita, parent=self )
		dialogAsignarCita.exec_()


	def cancelarCita( self ):

		dialogCancelarCita = DialogCita( nuevo_registro=False, controlador=self.controladorCita, parent=self )
		dialogCancelarCita.exec_() 


	#======================================================> AGENDA MEDICO
	
	def agendaMedico( self ):

		dialogAgenda = DialogAgendaMedico( controlador=self.controladorAgenda, parent=self )
		dialogAgenda.exec_()


	def closeEvent(self, event):
		#************************************************************************
		# CERRAR LA CONEXION EN LA BASE DE DATOS
		self.fachada.cerrarConexion()
		#************************************************************************
		event.accept()