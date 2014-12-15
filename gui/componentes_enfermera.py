from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from componentes_administrador import DialogInformacion

#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazEnfermera


#====================================================> PACIENTE <=======================================================

D_Paciente_class , D_PacienteBase_clas = uic.loadUiType('gui/enfermera_uis/DialogPaciente.ui')

class DialogPaciente( QDialog, D_Paciente_class ):
	
	def __init__( self, nuevo_registro=None, controlador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracio interfaz
		self.setupUi( self )
		
		#=================================================> VARIABLES
		self.controladorPaciente = controlador
		self.nuevo_registro = nuevo_registro
		#================================================> MODIFICACIONES 
		if self.nuevo_registro:
			
			
			self.pushButtonInsertar.setText( "Actualizar" )
			self.actualizar = True

		elif controlador:

			self.pushButtonInsertar.setText( "Insertar" )


	def insertarActualizarPaciente( self ):

		if self.actualizar:

			print("PACIENETE ACTAULIZADO")

		else:

			print("PACIENTE MODIFICADO")
		
		
#===================================================> Listar Pacientes 

W_ListarPacientes_class , W_LsitarPacientesBase_class = uic.loadUiType( 'gui/enfermera_uis/WidgetListarPacientes.ui' )

class WidgetListarPacientes( QWidget, W_ListarPacientes_class ):

	def __init__( self, controlador, parent=None ):

		QWidget.__init__( self, parent )
		self.setupUi( self )

		self.controladorPaciente = controlador

	def actualizar( self ):

		#Insertar nueva fila
		#self.tableWidget.insertRow( 0 )
		#Insertar sdato fila, columna
		#self.tableWidget.setItem( 0, 0, QTableWidgetItem( 'rellenar string ' ) ) )
		pass


#====================================================> CAMAS <==========================================================

D_AsignarCama_class , D_AsignarCamaBase_class = uic.loadUiType( 'gui/enfermera_uis/DialogAsignarCama.ui' )

class DialogAsignarCama( QDialog, D_AsignarCama_class ):

	def __init__( self, id_paciente, nombre_paciente, controlador, parent=None):

		QDialog.__init__( self, parent )
		self.setupUi( self )

		self.dialogInformacion  = DialogInformacion( self )

		self.lineEditIdentificacion.setText( id_paciente )
		self.lineEditNombre.setText( nombre_paciente )

		self.connect( self.pushButtonAsignar, SIGNAL( "clicked()" ), self.asignarCama )

	def asignarCama( self ):

		fila_seleccionada = self.tableWidgetCamas.currentRow()
		if fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Asignar Cama",
			 "Por favor seleccione la cama que desea asignar al paciente seleccionado" )

		else:

			print( "CAMA ASIGNADA" )

#====================================================> CITAS <==========================================================

D_CitaInterfaz_class , D_CitaInterfazBase_class = uic.loadUiType( 'gui/enfermera_uis/DialogCita.ui' )

class DialogCita( QDialog, D_CitaInterfaz_class ):

	def __init__( self, id_paciente, nombre_paciente , parent ):

		QDialog.__init__( self, parent )
		self.setupUi( self )


		self.dialogInformacion = DialogInformacion( self )

		self.lineEditIdentificacion.setText( id_paciente )
		self.lineEditNombre.setText( nombre_paciente )

		self.connect( self.pushButtonAsignarCita, SIGNAL( "clicked()" ), self.asignarCitaPaciente )

	def asignarCitaPaciente( self ):

		fila_seleccionada = self.tableWidgetHorarios.currentRow()
		if fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Asignar Cita", 
				"Por favor selcciones el horario en el cual desea que se realice la cita" )

		else:

			print("CITA ASIGNADA")
