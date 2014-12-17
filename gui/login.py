import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from administrador import InterfazAdministrador
from medico import InterfazMedico
from enfermera import InterfazEnfermera
from gui import *
from control import *
from accesoDatos import *

IniciarSesionInterfaz_class , InterfazAdministradorInterfazBase_class = uic.loadUiType('gui/login_uis/Login.ui')

class InterfazIniciarSesion( QMainWindow, IniciarSesionInterfaz_class ):

	def __init__( self, parent=None ):


		#************************************************************************
		# ABRIR CONEXION EN LA BASE DE DATOS
		self.fachada = FachadaDB()
		conexion = self.fachada.obtenerConexion()
		#************************************************************************
		

		#Constructor padre
		QMainWindow.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )
						
		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )

		#================================================> VARIABLES
		self.dialogInformacion = DialogInformacion( self )
		self.controladorLogin = ControlDaoLogin( conexion )

		
		#=================================================> SENIALES Y SLOTS 
		self.connect( self.pushButtonIngresar, SIGNAL("clicked()"), self.buscarUsuario)
		self.connect( self.pushButtonOlvideLaContrasenia, SIGNAL("clicked()"), self.recuperarContrasenia )



	def recuperarContrasenia( self ):
		print "Recuperar Contrasenia"

		
	def buscarUsuario( self ):

		identificacion  = str( self.lineEditContrasenia.text() )
		nombre_usuario = str(self.lineEditUsuario.text())

		if self.comboBoxTipoUsuario.currentIndex() == 0:

			resultado = self.controladorLogin.iniciarSesionAdministrador( identificacion, nombre_usuario )

			if isinstance (resultado,Exception):
				self.dialogInformacion.showMensaje( "Iniciar Sesion",
				resultado.pgerror )
			else:

				if resultado[0] == 1:

					self.close()
					interfazAdministrador = InterfazAdministrador( self )
					interfazAdministrador.show()
				else:

					self.dialogInformacion.showMensaje( "Iniciar Sesion",
				  	"por favor revise su usuario o password" )

		elif  self.comboBoxTipoUsuario.currentIndex() == 1:

			resultado = self.controladorLogin.iniciarSesionEnfermera( identificacion, nombre_usuario )

			if isinstance (resultado,Exception):
				self.dialogInformacion.showMensaje( "Iniciar Sesion",
				resultado.pgerror )
			else:

				if resultado[0] == 1:

					self.close()
					interfazEnfermera = InterfazEnfermera( self )
					interfazEnfermera.show()
				else:

					self.dialogInformacion.showMensaje( "Iniciar Sesion",
				  	"por favor revise su usuario o password" )

		else:

			resultado = self.controladorLogin.iniciarSesionAdministrador( identificacion, nombre_usuario )

			if isinstance (resultado,Exception):
				self.dialogInformacion.showMensaje( "Iniciar Sesion",
				resultado.pgerror )
			else:

				if resultado[0] == 1:

					self.close()
					interfazMedico = InterfazMedico( self )
					interfazMedico.show()
					
				else:

					self.dialogInformacion.showMensaje( "Iniciar Sesion",
				  	"por favor revise su usuario o password" )

			




	def closeEvent(self, event):
		#************************************************************************
		# CERRAR LA CONEXION EN LA BASE DE DATOS
		self.fachada.cerrarConexion()
		#************************************************************************
		event.accept()




		
		
		

