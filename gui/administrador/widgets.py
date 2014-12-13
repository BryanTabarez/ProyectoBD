from PyQt4.QtGui import *
from PyQt4.QtCore import * 
from PyQt4 import uic



#_________________________________ Listar areas __________________________________________

WidgetListarAreasInterfaz_class , WidgetListarAreasInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetListarAreas.ui')


class WidgetListarAreas( QWidget, WidgetListarAreasInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
	

#_________________________________ Listar camas __________________________________________ 

WidgetListarCamasInterfaz_class , WidgetListarCamasInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetListarCamas.ui')


class WidgetListarCamas( QWidget, WidgetListarCamasInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
			



#_________________________________ Listar medicamentos __________________________________________ 

WidgetListarMedicamentosInterfaz_class , WidgetListarMedicamentosInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetListarMedicamentos.ui')


class WidgetListarMedicamentos( QWidget, WidgetListarMedicamentosInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )		
		
	
#_________________________________ Listar Habilidades __________________________________________ 

WidgetListarHabilidadesInterfaz_class , WidgetListarHabilidadesInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetListarHabilidades.ui')


class WidgetListarHabilidades( QWidget, WidgetListarHabilidadesInterfaz_class ):

	def __init__( self, parent=None ):
		
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		self.ui = uic.loadUi('administrador/uis/WidgetListarHabilidades.ui')
	

#_________________________________ Tipo empleado enfermera  __________________________________________ 

WidgetTipoEmpleadoEnfermeraInterfaz_class , WidgetTipoEmpleadoEnfermeraInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetTipoEmpleadoEnfermera.ui')

class WidgetTipoEmpleadoEnfermera( QWidget, WidgetTipoEmpleadoEnfermeraInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro		
		self.setupUi( self )
	


#_________________________________ Tipo empleado medico  __________________________________________ 

WidgetTipoEmpleadoMedicoInterfaz_class , WidgetTipoEmpleadoMedicoInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetTipoEmpleadoMedico.ui')


class WidgetTipoEmpleadoMedico( QWidget, WidgetTipoEmpleadoMedicoInterfaz_class ):

	def __init__( self, parent=None ):

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
	



#______________________________________ INFORMES ____________________________________________________







#_________________________________ Empleados por areas __________________________________________ 


WidgetEmpleadosPorAreaInterfaz_class , WidgetEmpleadosPorAreaInterfazBase_class = uic.loadUiType('gui/administrador/uis/WidgetEmpleadosPorArea.ui')

class WidgetEmpleadosPorArea( QWidget , WidgetEmpleadosPorAreaInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )


#_________________________________ Agenda Medico Mes __________________________________________ 

WidgetAgendaMedicoMesInterfaz_class , WidgetAgendaMedicoMesInterfaBase_class = uic.loadUiType("gui/administrador/uis/WidgetAgendaMedico.ui");

class WidgetAgendaMedicoMes( QWidget, WidgetAgendaMedicoMesInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )


#_________________________________ Historia Clinica Paciente __________________________________________ 

WidgetHistoriaClinicaPacienteInterfaz_class , WidgetHistoriaClinicaPacienteInterfaBase_class = uic.loadUiType("gui/administrador/uis/WidgetHistoriaClinica.ui");

class WidgetHistoriaClinicaPaciente( QWidget, WidgetHistoriaClinicaPacienteInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

#_________________________________ Citas Atendidas Medico Por Mes __________________________________________ 

WidgetNumeroCitasMedicoInterfaz_class , WidgetNumeroCitasMedicoInterfaBase_class = uic.loadUiType("gui/administrador/uis/WidgetNumeroCitasMedico.ui");

class WidgetNumeroCitasMedico( QWidget, WidgetNumeroCitasMedicoInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

#_________________________________ Costo Paciente Mes Anio  __________________________________________ 

WidgetCostoPromedioPacienteInterfaz_class , WidgetCostoPromedioPacienteInterfaBase_class = uic.loadUiType("gui/administrador/uis/WidgetCostoPromedioPaciente.ui");

class WidgetCostoPromedioPaciente( QWidget, WidgetCostoPromedioPacienteInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
