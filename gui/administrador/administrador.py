from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from gui.administrador.adminidtrador.dialogs import DialogNuevoEmpleado
from gui.administrador.adminidtrador.dialogs import DialogModificarEmpleado
from gui.administrador.adminidtrador.widgets import WidgetEmpleadosPorArea

from gui.administrador.adminidtrador.dialogs import DialogNuevaArea
from gui.administrador.adminidtrador.dialogs import DialogModificarArea
from gui.administrador.adminidtrador.widgets import WidgetListarAreas

from gui.administrador.adminidtrador.dialogs import DialogNuevaCama
from gui.administrador.adminidtrador.dialogs import DialogModificarCama
from gui.administrador.adminidtrador.widgets import WidgetListarCamas

from gui.administrador.adminidtrador.dialogs import DialogNuevoMedicamento
from gui.administrador.adminidtrador.dialogs import DialogModificarMedicamento
from gui.administrador.adminidtrador.widgets import WidgetListarMedicamentos

from gui.administrador.adminidtrador.dialogs import DialogNuevaHabilidad
from gui.administrador.adminidtrador.dialogs import DialogModificarHabilidad
from gui.administrador.adminidtrador.widgets import WidgetListarHabilidades

from gui.administrador.adminidtrador.widgets import WidgetAgendaMedicoMes
from gui.administrador.adminidtrador.widgets import WidgetHistoriaClinicaPaciente
from gui.administrador.adminidtrador.widgets import WidgetNumeroCitasMedico
from gui.administrador.adminidtrador.widgets import WidgetCostoPromedioPaciente






InterfazAdministradorInterfaz_class , InterfazAdministradorInterfazBase_class = uic.loadUiType('gui/administrador/uis/MainWindowAdministrador.ui')


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
		self.widgetListarAreas = WidgetListarAreas( self.widgetCuerpo )
		self.widgetListarAreas.hide()

		self.widgetListarCamas = WidgetListarCamas( self.widgetCuerpo )
		self.widgetListarCamas.hide()

		self.widgetListarMedicamentos = WidgetListarMedicamentos( self.widgetCuerpo )
		self.widgetListarMedicamentos.hide()

		self.widgetListarHabilidades = WidgetListarHabilidades( self.widgetCuerpo )
		self.widgetListarHabilidades.hide()
		
		#_____________________________________________________________________________
		self.widgetEmpleadosPorArea  = WidgetEmpleadosPorArea( self.widgetCuerpo )
		self.widgetEmpleadosPorArea.hide()

		self.widgetAgendaMedicoMes = WidgetAgendaMedicoMes( self.widgetCuerpo );
		self.widgetAgendaMedicoMes.hide()

		self.widgetHistoriaClinicaPaciente = WidgetHistoriaClinicaPaciente( self.widgetCuerpo )
		self.widgetHistoriaClinicaPaciente.hide()

		self.widgetNumeroCitasMedico = WidgetNumeroCitasMedico( self.widgetCuerpo )
		self.widgetNumeroCitasMedico.hide()

		self.widgetCostoPromedioPaciente = WidgetCostoPromedioPaciente( self.widgetCuerpo )
		self.widgetCostoPromedioPaciente.hide()

		

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

		#_______________________________________________________________________________________________________

		self.connect( self.commandLinkButtonAgendaMedicoMes, SIGNAL("clicked()"), self.mostrarAgendaMedico )
		self.connect( self.commandLinkButtonHistoriaClinicaPaciente, SIGNAL("clicked()"), self.mostrarHistoriaClinicaPaciente )
		self.connect( self.commandLinkButtonCitasAtendidasMedicoMes, SIGNAL("clicked()"), self.mostrarCitasAtendidasMedicoMes )
		self.connect( self.commandLinkButtonCostoPaciente, SIGNAL("clicked()"), self.mostrarCostoPaciente )

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
		
		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#___________________________________

		self.widgetEmpleadosPorArea.show()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()
		
		

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
		
		self.widgetListarAreas.show()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#______________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

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
		
		self.widgetListarAreas.hide()
		self.widgetListarCamas.show()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

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

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.show()
		self.widgetListarHabilidades.hide()

		#_________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()


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

	#Metodo: listarHabilidades
	#Funcion: Permite listar las habilidades de una enfermera registradas en la base de datos
	def listarHabilidades( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.show()

		#__________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#Metodo: mostrarAgendaMedico
	#Funcion: Permite visualizar la agenda programada del medico en un mes determinado
	def mostrarAgendaMedico( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#__________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.show()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#Metodo: mostrarHistoriaClinicaPaciente
	#Funcion: Permite visualizar la historia clinica de un paciente
	def mostrarHistoriaClinicaPaciente( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#__________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.show()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#Metodo: mostrarCitasAtendidasMedicoMes
	#Funcion: Permite visualizar las citas que ha atendido un medico en determinado mes
	def mostrarCitasAtendidasMedicoMes( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#__________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.show()
		self.widgetCostoPromedioPaciente.hide()
	
	#Metodo: mostrarCostoPaciente
	#Funcion: Permite visualizar el costo de un paciente
	def mostrarCostoPaciente( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		#__________________________________________

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.show()
		
		
