from PyQt4.QtGui import *
from PyQt4.QtCore import *

from administradorUI import Ui_mainWindowAdministrador

from dialogs.nuevoEmpleadoFuncionalUI import DialogNuevoEmpleado
from dialogs.modificarEmpleadoFuncionalUI import DialogModificarEmpleado
from widgets.empleadosPorAreaFuncionalUI import WidgetEmpleadosPorArea

from dialogs.nuevaAreaFuncionalUI import DialogNuevaArea
from dialogs.modificarAreaFuncionalUI import DialogModificarArea
from widgets.listarAreasFuncionalUI import WidgetListarAreas

from dialogs.nuevaCamaFuncionalUI import DialogNuevaCama
from dialogs.modificarCamaFuncionalUI import DialogModificarCama
from widgets.listarCamasFuncionalUI import WidgetListarCamas

from dialogs.nuevoMedicamentoFuncionalUI import DialogNuevoMedicamento
from dialogs.modificarMedicamentoFuncionalUI import DialogModificarMedicamento
from widgets.listarMedicamentosFuncionalUI import WidgetListarMedicamentos


class InterfazAdministrador( QMainWindow ):

	def __init__( self, parent=None ):

		"""
			Se llama al contructor de la clase padre indicando que este es 
			el contenedor de mas alto nivel pasando como argumento parent = None 
			por defecto

			Pero en este caso el contenedor padre de este es InterfazIniciarSesion
			por lo tanto al momento de instanciar un objeto de tipo InterfazAdministrador,
			se debe pasar al contructor de este el objeto padre (InterfazIniciarSesion).

		"""
		QWidget.__init__( self, parent )


		"""
			Se usan los atributos y configuraciones hechas en Ui_MainWindowAdministrador
			y se le aniaden nuevas funcionalidades en esta clase
		"""

		self.ui = Ui_mainWindowAdministrador()
		self.ui.setupUi( self )

		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )

		"""
			SENIALES Y SLOTS
			Se definen las seniales y slots que van a administrar los eventos que se generen 
			en la interfaz de administrador
		"""

		self.connect( self.ui.commandLinkButtonNuevoEmpleado, SIGNAL("clicked()"), self.nuevoEmpleado )
		self.connect( self.ui.commandLinkButtonModificarEmpleado, SIGNAL("clicked()"), self.modificarEmpleado )
		self.connect( self.ui.commandLinkButtonListarEmpleados, SIGNAL("clicked()"), self.listarEmpleados )

		self.connect( self.ui.commandLinkButtonNuevaArea, SIGNAL("clicked()"),  self.nuevaArea )
		self.connect( self.ui.commandLinkButtonModificarArea, SIGNAL("clicked()"), self.modificarArea )
		self.connect( self.ui.commandLinkButtonListarAreas, SIGNAL("clicked()"), self.listarAreas )

		self.connect( self.ui.commandLinkButtonNuevaCama, SIGNAL("clicked()"), self.nuevaCama )
		self.connect( self.ui.commandLinkButtonModificarCama, SIGNAL("clicked()"), self.modificarCama )
		self.connect( self.ui.commandLinkButtonListarCamas, SIGNAL("clicked()"), self.listarCamas )

		self.connect( self.ui.commandLinkButtonNuevoMedicamento, SIGNAL("clicked()"), self.nuevoMedicamento )
		self.connect( self.ui.commandLinkButtonModificarMedicamento, SIGNAL("clicked()"), self.modificarMedicamento )
		self.connect( self.ui.commandLinkButtonListarMedicamentos, SIGNAL("clicked()"), self.listarMedicamentos )


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
	#Funcion: Despliega un widget con un listado de los empleados que estan en la base de datos
	def listarEmpleados( self ):
		print "Listar Empleados"

		"""  VERIFICAR SI SE CREAN MUTIPLES WIDGETS AL GENERAR EL EVENTO MUCHAS VECES"""
		widgetEmpleadosPorArea  = WidgetEmpleadosPorArea( self )
		widgetEmpleadosPorArea.setGeometry( QRect(210, 70, 581, 481) )
		widgetEmpleadosPorArea.show()
		

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
	#Funcion: Despliega una tabla con todas las areas almacenadas en la base de datos
	def listarAreas( self ):
		
		widgetListarAreas = WidgetListarAreas( self )
		widgetListarAreas.setGeometry( QRect(210, 70, 581, 481) )
		widgetListarAreas.show()

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
	#Funcion: Despliega el widget que permite ver todas las camas en la base de datos
	def listarCamas( self ):

		widgetListarCamas = WidgetListarCamas( self )
		widgetListarCamas.setGeometry( QRect(210, 70, 581, 481) )
		widgetListarCamas.show()

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
	#Funcion: Despliega la lista de los medicamentos en la base de datos 
	def listarMedicamentos( self ):

		widgetListarMedicamentos = WidgetListarMedicamentos( self )
		widgetListarMedicamentos.setGeometry( QRect(210, 70, 581, 481) )
		widgetListarMedicamentos.show()