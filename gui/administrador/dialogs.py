from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from gui.administrador.adminidtrador.widgets import WidgetTipoEmpleadoEnfermera
from gui.administrador.adminidtrador.widgets import WidgetTipoEmpleadoMedico


#_______________________________ Modificar Area __________________________________________

DialogModificarAreaInterfaz_class , DialogModificarAreaInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogModificarArea.ui')

class DialogModificarArea( QDialog, DialogModificarAreaInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

		
	

#_______________________________ Modificar Cama __________________________________________

DialogModificarCamaInterfaz_class , DialogModificarCamaInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogModificarCama.ui')

class DialogModificarCama( QDialog, DialogModificarCamaInterfaz_class ):

	
	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )



#_______________________________ Modificar Empleados __________________________________________

DialogModificarEmpleadoInterfaz_class , DialogModificarEmpleadoInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogModificarEmpleado.ui')

class DialogModificarEmpleado( QDialog, DialogModificarEmpleadoInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
			



#_______________________________ Modificar Medicamentos __________________________________________

DialogModificarMedicamnetoInterfaz_class , DialogModificarMedicamentoInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogModificarMedicamento.ui')

class DialogModificarMedicamento( QDialog, DialogModificarMedicamnetoInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		

	

#_______________________________ Modificar Medicamentos __________________________________________

DialogModificarHabilidadInterfaz_class , DialogModificarHabilidadInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogModificarHabilidad.ui')

class DialogModificarHabilidad( QDialog, DialogModificarHabilidadInterfaz_class  ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
			


#_______________________________ Nueva Area __________________________________________

DialogNuevaAreaInterfaz_class , DialogNuevaAreaInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogNuevaArea.ui')

class DialogNuevaArea( QDialog, DialogNuevaAreaInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
			

#_______________________________ Nueva Cama __________________________________________

DialogNuevaCamaInterfaz_class , DialogNuevaCamaInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogNuevaCama.ui')

class DialogNuevaCama( QDialog, DialogNuevaCamaInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		
		

#_______________________________ Nuevo Empleado __________________________________________

DialogNuevoEmpleadoInterfaz_class , DialogNuevoEmepladoInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogNuevoEmpleado.ui')

class DialogNuevoEmpleado( QDialog, DialogNuevoEmpleadoInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )


		#Creamos los widgets que van a ser usnados en este widget
		self.widgetTipoEmpleadoEnfermera = WidgetTipoEmpleadoEnfermera( self.widgetTipoEmpleado )
		self.widgetTipoEmpleadoEnfermera.hide()
		self.widgetTipoEmpleadoMedico = WidgetTipoEmpleadoMedico( self.widgetTipoEmpleado )
		self.widgetTipoEmpleadoMedico.hide()

		"""
			SENIALES Y SLOTS			
		"""

		self.connect( self.comboBoxTipoEmpleado, SIGNAL( "currentIndexChanged(int)" ), self.mostrarDatosAdicionalesTipoEmpleado )

		

	def mostrarDatosAdicionalesTipoEmpleado( self, indice ):

		if( indice == 0 ):

			self.widgetTipoEmpleadoEnfermera.show()
			self.widgetTipoEmpleadoMedico.hide()
		
		elif( indice == 1 ):
			
			self.widgetTipoEmpleadoMedico.show()
			self.widgetTipoEmpleadoEnfermera.hide()

		

#_______________________________ Nuevo Empleado __________________________________________

DialogNuevoMedicamentoInterfaz_class , DialogNuevoMedicamentoInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogNuevoMedicamento.ui')

class DialogNuevoMedicamento( QDialog, DialogNuevoMedicamentoInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

		
	

#_______________________________ Nueva Habilidad __________________________________________

DialogNuevaHabilidadInterfaz_class , DialogNuevaHabilidadInterfazBase_class = uic.loadUiType('gui/administrador/uis/DialogNuevaHabilidad.ui')


class DialogNuevaHabilidad( QDialog, DialogNuevaHabilidadInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		
	
	
