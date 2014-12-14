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

#=======================================================================================================================

#====================================================> PACIENTE <=======================================================

#=======================================> Nuevo paciente , Actualizar pacinete
D_Paciente_class , D_PacienteBase_clas = uic.loadUiType('gui/enfermera_uis/DialogPaciente.ui')

class DialogPaciente( QDialog, D_Paciente_class ):
	
	
	def __init__( self, id_paciente=None, controlador=None, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )
		self.actualizar = False

		

		if id_paciente and controlador:
			
			self.lineEditIdentificacion.setText(id_paciente)
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

	def __init__( self, parent=None ):

		QWidget.__init__( self, parent )
		self.setupUi( self )


#====================================================> CAMAS <==========================================================

D_AsignarCama_class , D_AsignarCamaBase_class = uic.loadUiType( 'gui/enfermera_uis/DialogAsignarCama.ui' )

class DialogAsignarCama( QDialog, D_AsignarCama_class ):

	def __init__( self, id_paciente, nombre_paciente, controlador, parent=None):

		QDialog.__init__( self, parent )
		setupUi( self )

		self.dialogInformacion  = DialogInformacion( self )

		self.connect( self.pushButtonAsignar, SIGNAL( "clicked()" ), self.asignarCama )

	def asignarCama( self ):

		fila_seleccionada = self.tableWidgetCamas.currentRow()
		if fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Asignar Cama",
			 "Por favor seleccione la cama que desea asignar al paciente seleccionado" )

		else:

			print( "CAMA ASIGNADA" )

