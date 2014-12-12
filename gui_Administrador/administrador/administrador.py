from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from dialogs import DialogNuevoEmpleado
from dialogs import DialogModificarEmpleado
from widgets import WidgetEmpleadosPorArea

from dialogs import DialogNuevaArea
from dialogs import DialogModificarArea
from widgets import WidgetListarAreas

from dialogs import DialogNuevaCama
from dialogs import DialogModificarCama
from widgets import WidgetListarCamas

from dialogs import DialogNuevoMedicamento
from dialogs import DialogModificarMedicamento
from widgets import WidgetListarMedicamentos

from dialogs import DialogNuevaHabilidad
from dialogs import DialogModificarHabilidad
from widgets import WidgetListarHabilidades

InterfazAdministradorInterfaz_class , InterfazAdministradorInterfazBase_class = uic.loadUiType('administrador/uis/MainWindowAdministrador.ui')


class InterfazAdministrador( QMainWindow, InterfazAdministradorInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QMainWindow.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )


		#Se cargan los widgets o panales que usa el administrador
		self.widgetEmpleadosPorArea  = WidgetEmpleadosPorArea( self.widgetCuerpo )
		self.widgetEmpleadosPorArea.hide()

		self.widgetListarAreas = WidgetListarAreas( self.widgetCuerpo )
		self.widgetListarAreas.hide()

		self.widgetListarCamas = WidgetListarCamas( self.widgetCuerpo )
		self.widgetListarCamas.hide()

		self.widgetListarMedicamentos = WidgetListarMedicamentos( self.widgetCuerpo )
		self.widgetListarMedicamentos.hide()

		self.widgetListarHabilidades = WidgetListarHabilidades( self.widgetCuerpo )
		self.widgetListarHabilidades.hide()
		
		"""
			SENIALES Y SLOTS			
		"""

		self.connect( self.commandLinkButtonNuevoEmpleado, SIGNAL("clicked()"), self.nuevoEmpleado )
		self.connect( self.commandLinkButtonModificarEmpleado, SIGNAL("clicked()"), self.modificarEmpleado )
		self.connect( self.commandLinkButtonListarEmpleados, SIGNAL("clicked()"), self.listarEmpleados )

		self.connect( self.commandLinkButtonNuevaArea, SIGNAL("clicked()"),  self.nuevaArea )
		self.connect( self.commandLinkButtonModificarArea, SIGNAL("clicked()"), self.modificarArea )
		self.connect( self.commandLinkButtonListarAreas, SIGNAL("clicked()"), self.listarAreas )

		self.connect( self.commandLinkButtonNuevaCama, SIGNAL("clicked()"), self.nuevaCama )
		self.connect( self.commandLinkButtonModificarCama, SIGNAL("clicked()"), self.modificarCama )
		self.connect( self.commandLinkButtonListarCamas, SIGNAL("clicked()"), self.listarCamas )

		self.connect( self.commandLinkButtonNuevoMedicamento, SIGNAL("clicked()"), self.nuevoMedicamento )
		self.connect( self.commandLinkButtonModificarMedicamento, SIGNAL("clicked()"), self.modificarMedicamento )
		self.connect( self.commandLinkButtonListarMedicamentos, SIGNAL("clicked()"), self.listarMedicamentos )

		self.connect( self.commandLinkButtonNuevaHabilidad, SIGNAL("clicked()"),  self.nuevaHabilidad )
		self.connect( self.commandLinkButtonModificarHabilidad, SIGNAL("clicked()"), self.modificarHabilidad )
		self.connect( self.commandLinkButtonListarHabilidades, SIGNAL("clicked()"), self.listarHabilidades )


		"""
			METODOS			
		"""


	#Metodo: nuevoEmpleado
	#Funcion: Desplieqga el dialogo con la interfaz para ingresar un nuevo empleado
	def nuevoEmpleado( self ):
		
		dialogNuevoEmpleado = DialogNuevoEmpleado( self )
		dialogNuevoEmpleado.exec_()

	#Metodo: modificarEmpleado
	#Funcion: Despliega el dialogo con la interfaz que permite modificar y eliminar un empleado
	def modificarEmpleado( self ):

		dialogModificarEmpleado = DialogModificarEmpleado( self )
		dialogModificarEmpleado.exec_()

	#Metodo: listarEmpleados
	#Funcion: permite mostrar el listado de empleados de la clinica por area
	def listarEmpleados( self ):

		self.widgetEmpleadosPorArea.show()
		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		
		

	#Metodo: nuevaArea
	#Funcion: Despliega la interfaz para la creacion de areas en el hospital
	def nuevaArea( self ):

		dialogNuevaArea = DialogNuevaArea( self )
		dialogNuevaArea.exec_()


	#Metodo: modificarArea
	#Funcion: Despliega la interfaz que permite la modificacion de un area
	def modificarArea( self ):

		dialogModificarArea = DialogModificarArea( self )
		dialogModificarArea.exec_()

	#Metdo: listarAreas
	#Funcion: permite mostrar las areas de la clinica
	def listarAreas( self ):

		self.widgetEmpleadosPorArea.hide()
		self.widgetListarAreas.show()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

	#Metodo: listarAreas
	#Funcion: Despliega la interfaz que permite crear un nueva cama 
	def nuevaCama( self ):

		dialogNuevaCama = DialogNuevaCama( self )
		dialogNuevaCama.exec_()

	#Metodo: modificarCama
	#Funcion: Despliega la interfaz que permite modificar una cama 
	def modificarCama( self ):

		dialogModificarCama = DialogModificarCama( self )
		dialogModificarCama.exec_()

	#Metodo: listarCamas
	#Funcion: permite mostrar un listado de camas del hospital
	def listarCamas( self ):

		self.widgetEmpleadosPorArea.hide()
		self.widgetListarAreas.hide()
		self.widgetListarCamas.show()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

	#Metodo: nuevoMedicamento
	#Funcion: Despliega la interfaz que permite insertar medicamentos
	def nuevoMedicamento( self ):

		dialogNuevoMedicamento = DialogNuevoMedicamento( self )
		dialogNuevoMedicamento.exec_()

	#Metodo: modificarMedicamento
	#Funcion: Despliega la interfaz que permite modificar medicamentos medicamento
	def modificarMedicamento( self ):

		dialogModificarMedicamento = DialogModificarMedicamento( self )
		dialogModificarMedicamento.exec_()

	#Metodo: listarMedicamentos
	#Funcion: permite mostrar el listado de medicamentos disponibles en la clinica
	def listarMedicamentos( self ):

		self.widgetEmpleadosPorArea.hide()
		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.show()
		self.widgetListarHabilidades.hide()

	#Metodo: nuevaHabilidad
	#Funcion: Despliega el dialog que permite ingresar habilidades a la base de datos
	def nuevaHabilidad( self ):

		dialogNuevaHabilidad = DialogNuevaHabilidad( self )
		dialogNuevaHabilidad.exec_()

	#Metodo: modificarHabilidad
	#Funcion: Despliega el dialog que permite modificar las habilidades
	def modificarHabilidad( self ):

		dialogModificarHabilidad = DialogModificarHabilidad( self )
		dialogModificarHabilidad.exec_()

	def listarHabilidades( self ):

		self.widgetEmpleadosPorArea.hide()
		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.show()