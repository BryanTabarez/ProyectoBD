from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from PyQt4 import uic



#_________________________________ Empleados por areas__________________________________________ 


WidgetEmpleadosPorAreaInterfaz_class , WidgetEmpleadosPorAreaInterfazBase_class = uic.loadUiType('administrador/uis/WidgetEmpleadosPorArea.ui')

class WidgetEmpleadosPorArea( QWidget , WidgetEmpleadosPorAreaInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
		


#_________________________________ Listar areas __________________________________________

WidgetListarAreasInterfaz_class , WidgetListarAreasInterfazBase_class = uic.loadUiType('administrador/uis/WidgetListarAreas.ui')


class WidgetListarAreas( QWidget, WidgetListarAreasInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
	

#_________________________________ Listar camas __________________________________________ 

WidgetListarCamasInterfaz_class , WidgetListarCamasInterfazBase_class = uic.loadUiType('administrador/uis/WidgetListarCamas.ui')


class WidgetListarCamas( QWidget, WidgetListarCamasInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
			



#_________________________________ Listar medicamentos __________________________________________ 

WidgetListarMedicamentosInterfaz_class , WidgetListarMedicamentosInterfazBase_class = uic.loadUiType('administrador/uis/WidgetListarMedicamentos.ui')


class WidgetListarMedicamentos( QWidget, WidgetListarMedicamentosInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )		
		
	
#_________________________________ Listar Habilidades __________________________________________ 

WidgetListarHabilidadesInterfaz_class , WidgetListarHabilidadesInterfazBase_class = uic.loadUiType('administrador/uis/WidgetListarHabilidades.ui')


class WidgetListarHabilidades( QWidget, WidgetListarHabilidadesInterfaz_class ):

	def __init__( self, parent=None ):
		
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		self.ui = uic.loadUi('administrador/uis/WidgetListarHabilidades.ui')
	

#_________________________________ Tipo empleado enfermera  __________________________________________ 

WidgetTipoEmpleadoEnfermeraInterfaz_class , WidgetTipoEmpleadoEnfermeraInterfazBase_class = uic.loadUiType('administrador/uis/WidgetTipoEmpleadoEnfermera.ui')

class WidgetTipoEmpleadoEnfermera( QWidget, WidgetTipoEmpleadoEnfermeraInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro		
		self.setupUi( self )
	


#_________________________________ Tipo empleado medico  __________________________________________ 

WidgetTipoEmpleadoMedicoInterfaz_class , WidgetTipoEmpleadoMedicoInterfazBase_class = uic.loadUiType('administrador/uis/WidgetTipoEmpleadoMedico.ui')


class WidgetTipoEmpleadoMedico( QWidget, WidgetTipoEmpleadoMedicoInterfaz_class ):

	def __init__( self, parent=None ):

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
	


	
	