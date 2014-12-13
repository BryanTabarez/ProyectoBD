import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from gui.administrador.administrador import InterfazAdministrador

IniciarSesionInterfaz_class , InterfazAdministradorInterfazBase_class = uic.loadUiType('gui/uis/Login.ui')

class InterfazIniciarSesion( QMainWindow, IniciarSesionInterfaz_class ):

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


		self.connect( self.pushButtonIngresar, SIGNAL("clicked()"), self.buscarUsuario)
		self.connect( self.pushButtonOlvideLaContrasenia, SIGNAL("clicked()"), self.recuperarContrasenia )



	def recuperarContrasenia( self ):
		print "Recuperar Contrasenia"

	def buscarUsuario( self ):
		print "Buscar Usuario"

		if self.lineEditUsuario.text() == "1":

			self.close()
			interfazAdministrador = InterfazAdministrador( self )
			interfazAdministrador.show()

		
		elif self.lineEditUsuario.text() == "2":
		
			self.abrirVentanaEnfermera()
		
		elif self.ui.lineEditUsuario.text() == "3":
		
			self.abrirVentanaMedico()
		
		else:
			print "Usuario no econtrado"



		
		
		

