from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
<<<<<<< HEAD
from accesoDatos import *
from control import *
from componentes_enfermera import DialogAgendaMedico

#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================

#==============================================> INETRAFZ MEDICO <======================================================

M_Admin_Interfaz_class , M_Administrador_Interfaz_Base_class = uic.loadUiType( 'gui/medico_uis/VentanaMedico.ui' ) 

class InterfazMedico( QMainWindow, M_Admin_Interfaz_class):

	def __init__( self, parent=None ):

		QMainWindow.__init__( self, parent )
		self.setupUi( self )

		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )

		#===============================================> SENIALES Y SLOTS
		self.connect( self.commandLinkButtonAtenderCita, SIGNAL( "clicked()" ), self.atenderCita )
		self.connect( self.commandLinkButtonVerAgenda, SIGNAL( "clicked()" ), self.agenda )
		self.connect( self.commandLinkButtonNuevaCampana, SIGNAL( "clicked()" ), self.nuevaCampana )
		self.connect( self.commandLinkButtonModificarCampana, SIGNAL( "clicked()" ), self.modificarCampana )
		#self.connect( self.commandLinkButtonListarCampanas, SIGNAL( "clicked()" ), self.listarCampanas )
		self.connect( self.commandLinkButtonVincularPaciente, SIGNAL( "clicked()" ), self.vincularPaciente )
		self.connect( self.commandLinkButtonDesvincularPaciente, SIGNAL( "clicked()" ), self.desVincularPaciente )
		#self.connect( self.commandLinkButtonPacientesCampanas, SIGNAL( "clicked()" ), self.pacientesCampanas )


		#=================================================> METODOS

	def atenderCita( self ):
		
		dialogAtenderCita = DialogAtenderCita( self )
		dialogAtenderCita.exec_()

	def agenda( self ):

		dialogAgenda = DialogAgendaMedico( self )
		dialogAgenda.exec_()

	def nuevaCampana( self ):

		dialogCampanaPrevencion = DialogCampanaPrevencion( self )
		dialogCampanaPrevencion.exec_()

	def modificarCampana( self ):

		dialogModificarCampana = DialogModificarCampana( self )
		dialogModificarCampana.exec_()

	def vincularPaciente( self ):

		dialogVincularPaciente = DialogVincularPaciente( self )
		dialogVincularPaciente.exec_()

	def desVincularPaciente( self ):

		dialogDesVincularPaciente = DialogDesVincularPaciente( self )
		dialogDesVincularPaciente.exec_()



#=========================================================> DIALOG ATENDER CITA <=======================================

D_AtenderCita_class , D_AtenderCita_Base_class = uic.loadUiType( 'gui/medico_uis/DialogAtenderCita.ui' )

class DialogAtenderCita( QDialog,  D_AtenderCita_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )


		#================================================> SENIALES Y SLOTS 
		self.connect( self.lineEditIndentificacion, SIGNAL( "clicked()" ), self.consultar )


		#================================================> METODOS 

	def consultar( self ):
		pass


#=================================================> CAMPANA DE PREVENCION <=============================================

D_Campana_class , D_Campana_Base_class = uic.loadUiType( 'gui/medico_uis/DialogNuevaCampana.ui' )

class DialogCampanaPrevencion( QDialog, D_Campana_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )

#=================================================> CAMPANA DE PREVENCION <=============================================

D_Modificar_Campana_class , D_Modificar_Campana_Base_class = uic.loadUiType( 'gui/medico_uis/DialogModificarCampana.ui')

class DialogModificarCampana( QDialog, D_Modificar_Campana_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )

#=================================================> CAMPANA DE PREVENCION <=============================================

D_Vincular_class , D_Vincular_class_Base_class = uic.loadUiType( 'gui/medico_uis/DialogVincularPaciente.ui' )

class DialogVincularPaciente( QDialog, D_Vincular_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )


#=================================================> CAMPANA DE PREVENCION <=============================================

D_DesVincular_class , D_DesVincular_class_Base_class = uic.loadUiType( 'gui/medico_uis/DialogDesvincularPacientes.ui' )

class DialogDesVincularPaciente( QDialog, D_DesVincular_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )
=======

#from componentes_enfermera import *

from componentes_administrador import WidgetListarCamas

from componentes_enfermera import DialogPaciente


from componentes_enfermera import DialogCama
from componentes_administrador import WidgetListarCamas

from componentes_enfermera import DialogCita

from componentes_administrador import DialogInformacion
from componentes_enfermera import DialogAgendaMedico

from accesoDatos import *
from control import *
>>>>>>> 48296d11b46488713f0ac8e2d1fea227111e9a97
