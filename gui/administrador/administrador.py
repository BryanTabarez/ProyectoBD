import os
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from componentes import DialogInformacion

from componentes import DialogNuevoEmpleado
from componentes import DialogModificarEmpleado
from componentes import WidgetEmpleadosPorArea

from componentes import DialogNuevaArea
from componentes import DialogModificarArea
from componentes import WidgetListarAreas

from componentes import DialogNuevaCama
from componentes import DialogModificarCama
from componentes import WidgetListarCamas

from componentes import DialogNuevoMedicamento
from componentes import DialogModificarMedicamento
from componentes import WidgetListarMedicamentos

from componentes import DialogNuevaHabilidad
from componentes import DialogModificarHabilidad
from componentes import WidgetListarHabilidades



from componentes import WidgetAgendaMedicoMes
from componentes import WidgetHistoriaClinicaPaciente
from componentes import WidgetNumeroCitasMedico
from componentes import WidgetCostoPromedioPaciente


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
		self.dialogInformacion = DialogInformacion( self )

		self.widgetListarAreas = WidgetListarAreas( self.widgetCuerpo )
		self.widgetListarAreas.hide()

		self.widgetListarCamas = WidgetListarCamas( self.widgetCuerpo )
		self.widgetListarCamas.hide()

		self.widgetListarMedicamentos = WidgetListarMedicamentos( self.widgetCuerpo )
		self.widgetListarMedicamentos.hide()

		self.widgetListarHabilidades = WidgetListarHabilidades( self.widgetCuerpo )
		self.widgetListarHabilidades.hide()
		
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

		#PERSONAL
		self.connect( self.commandLinkButtonNuevoEmpleado, SIGNAL( "clicked()" ), self.nuevoEmpleado )
		self.connect( self.commandLinkButtonModificarEmpleado, SIGNAL( "clicked()" ), self.modificarEmpleado )
		self.connect( self.commandLinkButtonEliminarEmpleado, SIGNAL( "clicked()" ), self.eliminarEmpleado )
		self.connect( self.commandLinkButtonListarEmpleados, SIGNAL("clicked()"), self.listarEmpleados )
		#AREAS
		self.connect( self.commandLinkButtonNuevaArea, SIGNAL( "clicked()" ),  self.nuevaArea )
		self.connect( self.commandLinkButtonModificarArea, SIGNAL( "clicked()" ), self.modificarArea )
		self.connect( self.commandLinkButtonEliminarArea, SIGNAL( "clicked()" ), self.eliminarArea )
		self.connect( self.commandLinkButtonListarAreas, SIGNAL("clicked()"), self.listarAreas )
		#CAMAS
		self.connect( self.commandLinkButtonNuevaCama, SIGNAL("clicked()"), self.nuevaCama )
		self.connect( self.commandLinkButtonModificarCama, SIGNAL("clicked()"), self.modificarCama )
		self.connect( self.commandLinkButtonEliminarCama, SIGNAL( "clicked()" ), self.eliminarCama )
		self.connect( self.commandLinkButtonListarCamas, SIGNAL("clicked()"), self.listarCamas )
		#MEDICAMENTOS
		self.connect( self.commandLinkButtonNuevoMedicamento, SIGNAL("clicked()"), self.nuevoMedicamento )
		self.connect( self.commandLinkButtonModificarMedicamento, SIGNAL("clicked()"), self.modificarMedicamento )
		self.connect( self.commandLinkButtonEliminarMedicamento, SIGNAL( "clicked()" ), self.eliminarMedicamento )
		self.connect( self.commandLinkButtonListarMedicamentos, SIGNAL("clicked()"), self.listarMedicamentos )
		#HABILIDADES
		self.connect( self.commandLinkButtonNuevaHabilidad, SIGNAL("clicked()"),  self.nuevaHabilidad )
		self.connect( self.commandLinkButtonModificarHabilidad, SIGNAL("clicked()"), self.modificarHabilidad )
		self.connect( self.commandLinkButtonListarHabilidades, SIGNAL("clicked()"), self.listarHabilidades )
		#INFROMES
		self.connect( self.commandLinkButtonAgendaMedicoMes, SIGNAL("clicked()"), self.mostrarAgendaMedico )
		self.connect( self.commandLinkButtonHistoriaClinicaPaciente, SIGNAL("clicked()"), self.mostrarHistoriaClinicaPaciente )
		self.connect( self.commandLinkButtonCitasAtendidasMedicoMes, SIGNAL("clicked()"), self.mostrarCitasAtendidasMedicoMes )
		self.connect( self.commandLinkButtonCostoPaciente, SIGNAL("clicked()"), self.mostrarCostoPaciente )

	"""
		METODOS			
	"""

	#PERSONAL
	#Metodo: nuevoEmpleado
	#Funcion: Desplieqga el dialogo con la interfaz para ingresar un nuevo empleado
	def nuevoEmpleado( self ):
		
		dialogNuevoEmpleado = DialogNuevoEmpleado( self )
		dialogNuevoEmpleado.exec_()

	#Metodo: modificarEmpleado
	#Funcion: Despliega el dialogo con la interfaz que permite modificar y eliminar un empleado
	def modificarEmpleado( self ):


		fila_seleccinada_tabla = self.widgetEmpleadosPorArea.tableWidgetEmpleados.currentRow()	
		if self.widgetEmpleadosPorArea.isHidden() or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Modificar Empleado", 
				"Por favor liste los empleados, seleccione de la tabla el que desea modificar, luego presione 'Modificar Empleado'" )
			
		else:

			fila_seleccinada_tabla = self.widgetEmpleadosPorArea.tableWidgetEmpleados.currentRow()
			dialogModificarEmpleado = DialogModificarEmpleado( "123456", "controlador" , self )
			dialogModificarEmpleado.exec_()

	#Metodo: eliminarEmpleado
	#Funcion: permite eliminar un empleado de la base de datos
	def eliminarEmpleado( self ):

		
		fila_seleccinada_tabla = self.widgetEmpleadosPorArea.tableWidgetEmpleados.currentRow()	
		if self.widgetEmpleadosPorArea.isHidden() or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Empleado", 
				"Por favor liste los empleados, seleccione de la tabla el que desea eliminar, luego presione 'Eliminar Empleado'" )
			
		else:
			print("EMPEADO ELIMINADO")


	#Metodo: listarEmpleados
	#Funcion: permite mostrar el listado de empleados de la clinica por area
	def listarEmpleados( self ):
		
		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		self.widgetEmpleadosPorArea.show()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()
		
		

	#AREA
	#Metodo: nuevaArea
	#Funcion: Despliega la interfaz para la creacion de areas en el hospital
	def nuevaArea( self ):

		dialogNuevaArea = DialogNuevaArea( self )
		dialogNuevaArea.exec_()


	#Metodo: modificarArea
	#Funcion: Despliega la interfaz que permite la modificacion de un area
	def modificarArea( self ):

		fila_seleccinada_tabla = self.widgetListarAreas.tableWidgetAreas.currentRow()	
		if self.widgetListarAreas.isHidden() or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Area", 
				"Por favor liste las areas, seleccione de la tabla la que desea modificar, luego presione 'Modificar Area' " )
			
		else:
			dialogModificarArea = DialogModificarArea( "codigo_area", "controlador", self )
			dialogModificarArea.exec_()

	#Metodo: eliminarArea
	#Funcion: permite eliminar areas de la clinica de la base de datos
	def eliminarArea( self ):

		fila_seleccinada_tabla = self.widgetListarAreas.tableWidgetAreas.currentRow()	
		if self.widgetListarAreas.isHidden() or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Area", 
				"Por favor liste las areas, seleccione de la tabla la que desea eliminar, luego presione 'Eliminar Area' " )
			
		else:
			print("AREA ELIMINADA")


	#Metodo: listarAreas
	#Funcion: permite mostrar las areas de la clinica
	def listarAreas( self ):
		
		self.widgetListarAreas.show()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#CAMA
	#Metodo: nuevaCama
	#Funcion: Despliega la interfaz que permite crear un nueva cama 
	def nuevaCama( self ):

		dialogNuevaCama = DialogNuevaCama( self )
		dialogNuevaCama.exec_()

	#Metodo: modificarCama
	#Funcion: Despliega la interfaz que permite modificar una cama 
	def modificarCama( self ):

		fila_seleccinada_tabla = self.widgetListarCamas.tableWidgetCamas.currentRow()
		if self.widgetListarCamas.isHidden() or fila_seleccinada_tabla == -1:

			self.dialogInformacion.showMensaje( "Modificar Cama", 
				"Por favor liste las camas, seleccione de la tabla la que desea modificar, luego presione 'Modificar Cama' " )

		else:

			dialogModificarCama = DialogModificarCama( "codigo_cama", "controlador", self )
			dialogModificarCama.exec_()

	#Metodo: elimarCama
	#Funcion: permite elimnar camas de la base de datos
	def eliminarCama( self ):

		fila_seleccinada_tabla = self.widgetListarCamas.tableWidgetCamas.currentRow()
		if self.widgetListarCamas.isHidden() or fila_seleccinada_tabla == -1:

			self.dialogInformacion.showMensaje( "Eliminar Cama", 
				"Por favor liste las camas, seleccione de la tabla la que desea eliminar, luego presione 'eliminar Cama' " )

		else:

			print("CAMA ELIMINADA")


	#Metodo: listarCamas
	#Funcion: permite mostrar un listado de camas del hospital
	def listarCamas( self ):
		
		self.widgetListarAreas.hide()
		self.widgetListarCamas.show()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#MEDICAMENTO
	#Metodo: nuevoMedicamento
	#Funcion: Despliega la interfaz que permite insertar medicamentos
	def nuevoMedicamento( self ):

		dialogNuevoMedicamento = DialogNuevoMedicamento( self )
		dialogNuevoMedicamento.exec_()

	#Metodo: modificarMedicamento
	#Funcion: Despliega la interfaz que permite modificar medicamentos medicamento
	def modificarMedicamento( self ):

		fila_seleccinada_tabla = self.widgetListarMedicamentos.tableWidgetMedicamentos.currentRow()
		if self.widgetListarMedicamentos.isHidden or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Modificar Medicamento", 
				"Por favor liste los medicamento, seleccione de la tabla la que desea modificar, luego presione 'Modificar Medicamento' " )
			
		else:

			dialogModificarMedicamento = DialogModificarMedicamento( "codigo_medicamento", "controlador",  self )
			dialogModificarMedicamento.exec_()



	#Metodo: eliminarMedicamento
	#Funcion: permite eliminar el medicamento seleccinado de la base de datos 
	def eliminarMedicamento( self ):

		fila_seleccinada_tabla = self.widgetListarMedicamentos.tableWidgetMedicamentos.currentRow()
		if self.widgetListarMedicamentos.isHidden or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Medicamento", 
				"Por favor liste los medicamento, seleccione de la tabla la que desea eliminar, luego presione 'Eliminar Medicamento' " )
			
		else:

			print( "MEDICAMENTO ELIMINADO" )



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
		
		
