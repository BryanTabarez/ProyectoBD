from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


#_______________________________ DIALOGO DE INFORMACION __________________________________

DialogInformacionInterfaz_class , DialogInformacionInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogInformacion.ui' )

class DialogInformacion( QDialog, DialogInformacionInterfaz_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )

	def showMensaje( self, encabezado, mensaje ):

		self.labelEncabezado.setText( encabezado )
		self.plainTextEditCuerpo.setPlainText( mensaje )
		self.show()



#_______________________________ Nuevo Empleado __________________________________________

DialogNuevoEmpleadoInterfaz_class , DialogNuevoEmepladoInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogNuevoEmpleado.ui' )

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

#_________________________________ Tipo empleado enfermera  __________________________________________ 

WidgetTipoEmpleadoEnfermeraInterfaz_class , WidgetTipoEmpleadoEnfermeraInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetTipoEmpleadoEnfermera.ui')

class WidgetTipoEmpleadoEnfermera( QWidget, WidgetTipoEmpleadoEnfermeraInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro		
		self.setupUi( self )
	


#_________________________________ Tipo empleado medico  __________________________________________ 

WidgetTipoEmpleadoMedicoInterfaz_class , WidgetTipoEmpleadoMedicoInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetTipoEmpleadoMedico.ui')


class WidgetTipoEmpleadoMedico( QWidget, WidgetTipoEmpleadoMedicoInterfaz_class ):

	def __init__( self, parent=None ):

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	
#_______________________________ Modificar Empleados __________________________________________

DialogModificarEmpleadoInterfaz_class , DialogModificarEmpleadoInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogModificarEmpleado.ui' )

class DialogModificarEmpleado( QDialog, DialogModificarEmpleadoInterfaz_class ):

	#Metodo: __init___
	#Funcion: Permite cargar un dialog con la infromacion del del empleado a modificar
	#indentificacion: identificacion del empleado a modificar
	#controlador: el controlador que permite la conexion a la base de datos 
	def __init__( self, identificacion_empleado, controlador ,parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

		"""
			SENIALES Y SLOTS
		"""

		self.connect( self.pushButtonActualizar, SIGNAL( "clicked()" ), self.actualizarEmpleado )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), SLOT("close()") )

		"""
			SE CARGAN LOS DATOS DEL EMPLEADO A MODIFCIAR USANDO EL CONTROLADOR
		"""

		print('Cargar datos empleado: ' + str( identificacion_empleado ) )


	#Metodo: actualizarEmpleado
	#Funcion: Permite actualizar un empleado por medio del controlador
	def actualizarEmpleado( self ):
		print("ACTUALIZAR EMPLEADO")


			

#_________________________________ Empleados por areas __________________________________________ 


WidgetEmpleadosPorAreaInterfaz_class , WidgetEmpleadosPorAreaInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetEmpleadosPorArea.ui')

class WidgetEmpleadosPorArea( QWidget , WidgetEmpleadosPorAreaInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

		
		












#_______________________________ Nueva Area __________________________________________

DialogNuevaAreaInterfaz_class , DialogNuevaAreaInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogNuevaArea.ui' )

class DialogNuevaArea( QDialog, DialogNuevaAreaInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
			



#_______________________________ Modificar Area __________________________________________

DialogModificarAreaInterfaz_class , DialogModificarAreaInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogModificarArea.ui' )

class DialogModificarArea( QDialog, DialogModificarAreaInterfaz_class ):

	def __init__( self, codigo_area, controlador, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

		
#_________________________________ Listar areas __________________________________________

WidgetListarAreasInterfaz_class , WidgetListarAreasInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetListarAreas.ui')


class WidgetListarAreas( QWidget, WidgetListarAreasInterfaz_class ):
	
	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
	







#_______________________________ Nueva Cama __________________________________________

DialogNuevaCamaInterfaz_class , DialogNuevaCamaInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogNuevaCama.ui' )

class DialogNuevaCama( QDialog, DialogNuevaCamaInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		


#_______________________________ Modificar Cama __________________________________________

DialogModificarCamaInterfaz_class , DialogModificarCamaInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogModificarCama.ui' )

class DialogModificarCama( QDialog, DialogModificarCamaInterfaz_class ):

	
	def __init__( self, codigo_cama, controlador, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )



#_________________________________ Listar camas __________________________________________ 

WidgetListarCamasInterfaz_class , WidgetListarCamasInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetListarCamas.ui')


class WidgetListarCamas( QWidget, WidgetListarCamasInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
			











#_______________________________ Nuevo Medicamento __________________________________________

DialogNuevoMedicamentoInterfaz_class , DialogNuevoMedicamentoInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogNuevoMedicamento.ui' )

class DialogNuevoMedicamento( QDialog, DialogNuevoMedicamentoInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )


#_______________________________ Modificar Medicamentos __________________________________________

DialogModificarMedicamnetoInterfaz_class , DialogModificarMedicamentoInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogModificarMedicamento.ui' )

class DialogModificarMedicamento( QDialog, DialogModificarMedicamnetoInterfaz_class ):

	def __init__( self, codigo_medicamento, controlador, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )


#_________________________________ Listar medicamentos __________________________________________ 

WidgetListarMedicamentosInterfaz_class , WidgetListarMedicamentosInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetListarMedicamentos.ui')


class WidgetListarMedicamentos( QWidget, WidgetListarMedicamentosInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""

		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )	









#_______________________________ Nueva Habilidad __________________________________________

DialogNuevaHabilidadInterfaz_class , DialogNuevaHabilidadInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogNuevaHabilidad.ui' )


class DialogNuevaHabilidad( QDialog, DialogNuevaHabilidadInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		

#_______________________________ Modificar Habilidades __________________________________________

DialogModificarHabilidadInterfaz_class , DialogModificarHabilidadInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogModificarHabilidad.ui' )

class DialogModificarHabilidad( QDialog, DialogModificarHabilidadInterfaz_class  ):

	def __init__( self, codigo_habilidad, controlador,  parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

#_________________________________ Listar Habilidades __________________________________________ 

WidgetListarHabilidadesInterfaz_class , WidgetListarHabilidadesInterfazBase_class = uic.loadUiType('gui/administrador_uis/WidgetListarHabilidades.ui')


class WidgetListarHabilidades( QWidget, WidgetListarHabilidadesInterfaz_class ):

	def __init__( self, parent=None ):
		
		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
		





	
#_________________________________ Nueva Causa ________________________________________________

DialogNuevaCausaInterfaz_class , DialogNuevaCausaInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogNuevaCausa.ui' )

class DialogNuevaCausa( QDialog, DialogNuevaCausaInterfaz_class ):

	def __init__( self, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""

		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )




#_________________________________ Modificar Causa ________________________________________________

DialogModificarCausaInterfaz_class , DialogNuevaCausaInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/DialogModificarCausa.ui' )

class DialogModificarCausa( QDialog, DialogModificarCausaInterfaz_class ):

	def __init__( self, codigo_causa, controlador, parent=None ):


		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""
		QDialog.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )



#_________________________________ Listar Causas ________________________________________________

WidgetListarCausasInterfaz_class , WidgetListarCausasInterfazBase_class = uic.loadUiType( 'gui/administrador_uis/WidgetListarCausas.ui' )

class WidgetListarCausas( QWidget, WidgetListarCausasInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL CONTENEDOR DE ESTE DIALOG
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )




#______________________________________ INFORMES ____________________________________________________


#_________________________________ Agenda Medico Mes __________________________________________ 

WidgetAgendaMedicoMesInterfaz_class , WidgetAgendaMedicoMesInterfaBase_class = uic.loadUiType("gui/administrador_uis/WidgetAgendaMedico.ui");

class WidgetAgendaMedicoMes( QWidget, WidgetAgendaMedicoMesInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )


#_________________________________ Historia Clinica Paciente __________________________________________ 

WidgetHistoriaClinicaPacienteInterfaz_class , WidgetHistoriaClinicaPacienteInterfaBase_class = uic.loadUiType("gui/administrador_uis/WidgetHistoriaClinica.ui");

class WidgetHistoriaClinicaPaciente( QWidget, WidgetHistoriaClinicaPacienteInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

#_________________________________ Citas Atendidas Medico Por Mes __________________________________________ 

WidgetNumeroCitasMedicoInterfaz_class , WidgetNumeroCitasMedicoInterfaBase_class = uic.loadUiType("gui/administrador_uis/WidgetNumeroCitasMedico.ui");

class WidgetNumeroCitasMedico( QWidget, WidgetNumeroCitasMedicoInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )

#_________________________________ Costo Paciente Mes Anio  __________________________________________ 

WidgetCostoPromedioPacienteInterfaz_class , WidgetCostoPromedioPacienteInterfaBase_class = uic.loadUiType("gui/administrador_uis/WidgetCostoPromedioPaciente.ui");

class WidgetCostoPromedioPaciente( QWidget, WidgetCostoPromedioPacienteInterfaz_class ):

	def __init__( self, parent=None ):

		"""
			SE LLAMA AL CONTRUCTOR DE LA CLASE PADRE Y SE LE PASA EL WIDGETPADRE QUE ES EL QUE CONTIENDE ESTE WIDGET
		"""
		QWidget.__init__( self, parent )
		#setupUi es el metodo que se encarga de colocar y organizar los componentes del objeto que se le pasa como parametro
		self.setupUi( self )
