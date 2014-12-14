from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazEnfermera

#=======================================================================================================================

#====================================================> Paciente <=======================================================

DialogPacienteInterfaz_clas , DialogPacienteInterfazBase_clas = uic.loadUiType('gui/enfermera_uis/DialogPaciente.ui')

class DialogPaciente( QDialog, DialogPacienteInterfaz_clas ):
	
	#Permite el inserso y actualizacion de pacientes
	def __init__( self, codigo_paciente=None, controlador=None, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )

		self.actualizar = False

		if codigo_paciente and controlador:
			
			self.pushButtonInsertar.setText( "Actualizar" )
			self.actualizar = True

		else:

			self.pushButtonInsertar.setText( "Insertar" )

	#Permite actualizar e insertar aspirantes a la base de datos
	def insertarActualizarPaciente( self ):

		if self.actualizar:

			print("PACIENETE ACTAULIZADO")

		else:

			print("PACIENTE MODIFICADO")
		
		
#===================================================> Listar Pacientes <================================================

WidgetListarPacientesInterfaz_class , WidgetLsitarPacientesInterfazBase_class = uic.loadUiType( 'gui/enfermera_uis/WidgetListarPacientes.ui' )

class WidgetListarPacientes( QWidget, WidgetListarPacientesInterfaz_class ):

	def __init__( self, parent=None ):

		QWidget.__init__( self, parent )
		self.setupUi( self )