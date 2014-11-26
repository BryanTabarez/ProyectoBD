"""
	Se importa el modulo iniciarSesion que contiene la clase Ui_MainWindowIniciarSesion
	con el esquema de la interfaz grafica de inicio de sesion 
"""

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from iniciarSesionUI import Ui_MainWindowIniciarSesion
from administrador.administradorFuncionalUI import InterfazAdministrador


class InterfazIniciarSesion( QMainWindow ):

	def __init__( self, parent=None ):

		
		"""
			Se llama al contructor de la clase padre indicando que este es 
			el contenedor de mas alto nivel pasando el argumento  parent = None 
			por defecto cuando  se instancia un objeto de tipo InterfazIniciarSesion

			Esto es similar a decir que este contenedor no esta contenido
			en otro, por tanto es de mas alto nivel.

		"""
		QWidget.__init__( self, parent )

		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowIniciarSesion
			y se le aniaden nuevas funcionalidades en esta clase
		"""
		
		self.ui = Ui_MainWindowIniciarSesion()
		self.ui.setupUi( self )


		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )




		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar las seniales que se generen 
			en la interfaz de iniciar sesion
		"""


		self.connect( self.ui.pushButtonIngresar, SIGNAL("clicked()"), self.buscarUsuario)
		self.connect( self.ui.pushButtonOlvideLaContrasenia, SIGNAL("clicked()"), self.recuperarContrasenia )

	def recuperarContrasenia( self ):
		print "Recuperar Contrasenia"

	def buscarUsuario( self ):
		print "Buscar Usuario"

		if self.ui.lineEditUsuario.text() == "1":

			self.abrirVentanaAdministrador()
		
		elif self.ui.lineEditUsuario.text() == "2":
		
			self.abrirVentanaEnfermera()
		
		elif self.ui.lineEditUsuario.text() == "3":
		
			self.abrirVentanaMedico()
		
		else:
			print "Usuario no econtrado"

	def abrirVentanaAdministrador( self ):
		
			
		"""
			IMPORTANTE : Cuando se Abre un nuevo QMainWindow desde un QMainWindow
			se debe pasar al nuevo QMainWindow la ventana padre.
		"""	

		self.close()
		interfazAdministrador = InterfazAdministrador( self )
		interfazAdministrador.show()
		

		

	def abrirVentanaEnfermera( self ):
		print "Ventana Enfermera"

	def abrirVentanaMedico( self ):
		print "Ventana Medico"