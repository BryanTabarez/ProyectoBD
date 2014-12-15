from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

from componentes_administrador import *
from accesoDatos import *
from control import *

#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazAdministrador
#PERSONAL --> EMPLEADOS
#AREAS
#CAMAS 
#MEDICAMENTOS
#HABILIDADES
#CAUSAS
#INFORMES
#=======================================================================================================================

#========================================> INTERFAZ ADMINISTRADOR <=====================================================
I_Administrador_class , I_Administrador_Base_class = uic.loadUiType('gui/administrador_uis/MainWindowAdministrador.ui')


class InterfazAdministrador( QMainWindow, I_Administrador_class ):

	def __init__( self, parent=None ):
		#************************************************************************
		# ABRIR CONEXION EN LA BASE DE DATOS
		self.fachada = FachadaDB()
		conexion = self.fachada.obtenerConexion()
		#************************************************************************
		
		#Constructor padre
		QMainWindow.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#CENTRAR EL QMainWindow
		pantalla = QDesktopWidget().screenGeometry()
		interfaz = self.geometry()

		pos_horizontal = ( pantalla.width() - interfaz.width() ) / 2
		pos_vertical = ( pantalla.height() - interfaz.height() ) / 2
		self.move( pos_horizontal, pos_vertical )
		
		#=====================================================> VARIABLES 
		# PERSONAL --> EMPLEADO
		self.controladorPersonal = " " #AQUI VA EL CONTROLADOR NO CAMBIAR NOMBRE DE VARIABLE  
		self.controladorArea = ControlDaoArea(conexion)
		self.controladorCama = " "
		self.controladorMedicamento = " "
		self.controladorHabilidad = " "
		self.controladorCausa = " "
		self.controladorInformes = " "


		#====================================================> WIDGETS
		self.dialogInformacion = DialogInformacion( self )

		self.widgetListarAreas = WidgetListarAreas( self.widgetCuerpo )
		self.widgetListarAreas.hide()

		self.widgetListarCamas = WidgetListarCamas( self.widgetCuerpo )
		self.widgetListarCamas.hide()

		self.widgetListarMedicamentos = WidgetListarMedicamentos( self.widgetCuerpo )
		self.widgetListarMedicamentos.hide()

		self.widgetListarHabilidades = WidgetListarHabilidades( self.widgetCuerpo )
		self.widgetListarHabilidades.hide()

		self.widgetListarCausas = WidgetListarCausas( self.widgetCuerpo )
		self.widgetListarCausas.hide()
		
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

		

		#===========================================> SENIALES Y SLOTS <================================================

		#==========================================> PERSONAL 
		self.connect( self.commandLinkButtonNuevoEmpleado, SIGNAL( "clicked()" ), self.nuevoEmpleado )
		self.connect( self.commandLinkButtonModificarEmpleado, SIGNAL( "clicked()" ), self.modificarEmpleado )
		self.connect( self.commandLinkButtonEliminarEmpleado, SIGNAL( "clicked()" ), self.eliminarEmpleado )
		self.connect( self.commandLinkButtonListarEmpleados, SIGNAL("clicked()"), self.listarEmpleados )
		#===========================================> AREAS 
		self.connect( self.commandLinkButtonNuevaArea, SIGNAL( "clicked()" ),  self.nuevaArea )
		self.connect( self.commandLinkButtonModificarArea, SIGNAL( "clicked()" ), self.modificarArea )
		self.connect( self.commandLinkButtonEliminarArea, SIGNAL( "clicked()" ), self.eliminarArea )
		self.connect( self.commandLinkButtonListarAreas, SIGNAL("clicked()"), self.listarAreas )
		#===========================================> CAMAS 
		self.connect( self.commandLinkButtonNuevaCama, SIGNAL("clicked()"), self.nuevaCama )
		self.connect( self.commandLinkButtonModificarCama, SIGNAL("clicked()"), self.modificarCama )
		self.connect( self.commandLinkButtonEliminarCama, SIGNAL( "clicked()" ), self.eliminarCama )
		self.connect( self.commandLinkButtonListarCamas, SIGNAL("clicked()"), self.listarCamas )
		#=========================================> MEDICAMENTOS 
		self.connect( self.commandLinkButtonNuevoMedicamento, SIGNAL("clicked()"), self.nuevoMedicamento )
		self.connect( self.commandLinkButtonModificarMedicamento, SIGNAL("clicked()"), self.modificarMedicamento )
		self.connect( self.commandLinkButtonEliminarMedicamento, SIGNAL( "clicked()" ), self.eliminarMedicamento )
		self.connect( self.commandLinkButtonListarMedicamentos, SIGNAL("clicked()"), self.listarMedicamentos )
		#=========================================> HABILIDADES 
		self.connect( self.commandLinkButtonNuevaHabilidad, SIGNAL("clicked()"),  self.nuevaHabilidad )
		self.connect( self.commandLinkButtonModificarHabilidad, SIGNAL("clicked()"), self.modificarHabilidad )
		self.connect( self.commandLinkButtonEliminarHabilidad, SIGNAL( "clicked()" ), self.eliminarHabilidad )
		self.connect( self.commandLinkButtonListarHabilidades, SIGNAL("clicked()"), self.listarHabilidades )
		#===========================================> CAUSAS 
		self.connect( self.commandLinkButtonNuevaCausa, SIGNAL( "clicked()" ), self.nuevaCausa )
		self.connect( self.commandLinkButtonModificarCausa, SIGNAL( "clicked()" ), self.modificarCausa )
		self.connect( self.commandLinkButtonEliminarCausa, SIGNAL( "clicked()" ), self.eliminarCausa )
		self.connect( self.commandLinkButtonListarCausas, SIGNAL( "clicked()" ), self.listarCausas )
		#==========================================> INFROMES 
		self.connect( self.commandLinkButtonAgendaMedicoMes, SIGNAL("clicked()"), self.agendaMedico )
		self.connect( self.commandLinkButtonHistoriaClinicaPaciente, SIGNAL("clicked()"), self.historiaClinicaPaciente )
		self.connect( self.commandLinkButtonCitasAtendidasMedicoMes, SIGNAL("clicked()"), self.citasAtendidasMedicoMes )
		self.connect( self.commandLinkButtonCostoPaciente, SIGNAL("clicked()"), self.costoPaciente )

	

	#============================================> METODOS <============================================================


	#==========================================> PERSONAL
	#Metodo: nuevoEmpleado
	#Funcion: Desplieqga el dialogo con la interfaz para ingresar un nuevo empleado
	def nuevoEmpleado( self ):
		
		dialogEmpleado = DialogEmpleado( controlador=self.controladorPersonal,  parent=self )
		dialogEmpleado.exec_()

	#Metodo: modificarEmpleado
	#Funcion: Despliega el dialogo con la interfaz que permite modificar y eliminar un empleado
	def modificarEmpleado( self ):

		dialogEmpleado = DialogEmpleado( nuevo_registro=False,  controlador=self.controladorPersonal, parent=self )
		dialogEmpleado.exec_()

	#Metodo: eliminarEmpleado
	#Funcion: permite eliminar un empleado de la base de datos
	def eliminarEmpleado( self ):

		
		fila_seleccinada_tabla = self.widgetEmpleadosPorArea.tableWidgetEmpleados.currentRow()	
		if self.widgetEmpleadosPorArea.isHidden() or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Empleado", 
				"Por favor liste los empleados, seleccione de la tabla el que desea eliminar, luego presione 'Eliminar Empleado'" )
			
		else:
			
			id_empleado_eliminar = self.widgetEmpleadosPorArea.tableWidgetEmpleados.item(fila_seleccinada_tabla, 0).text()
			print( "eliminar empleado: " + id_empleado_eliminar )
			#AQUI SE ELIMINA EL EMPLEADO CON EL CODIGO RECIBIDO


	#Metodo: listarEmpleados
	#Funcion: permite mostrar el listado de empleados de la clinica por area
	def listarEmpleados( self ):
		
		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.show()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()
		
		

	#===========================================> AREAS <===================================================
	#Metodo: nuevaArea
	#Funcion: Despliega la interfaz para la creacion de areas en el hospital
	def nuevaArea( self ):

		dialogArea = DialogArea( tipo_operacion=1, controlador=self.controladorArea ,parent=self )
		dialogArea.exec_()

	#Metodo: modificarArea
	#Funcion: Despliega la interfaz que permite la modificacion de un area
	def modificarArea( self ):

		dialogArea = DialogArea( tipo_operacion=2, controlador=self.controladorArea ,parent=self )
		dialogArea.exec_()


	def eliminarArea( self ):

		dialogArea = DialogArea( tipo_operacion=3, controlador=self.controladorArea ,parent=self )
		dialogArea.exec_()	

	# #Metodo: eliminarArea
	# #Funcion: permite eliminar areas de la clinica de la base de datos
	# def eliminarArea( self ):

	# 	fila_seleccinada_tabla = self.widgetListarAreas.tableWidgetAreas.currentRow()	
	# 	if self.widgetListarAreas.isHidden() or fila_seleccinada_tabla == -1:
			
	# 		self.dialogInformacion.showMensaje( "Eliminar Area", 
	# 			"Por favor liste las areas, seleccione de la tabla la que desea eliminar, luego presione 'Eliminar Area' " )
			
	# 	else:
	# 		cod_area_eliminar = self.widgetListarAreas.tableWidgetAreas.item(fila_seleccinada_tabla, 0).text()
	# 		print( "eliminar area: " + cod_area_eliminar )
	# 		#AQUI SE ELIMINA EL AREA CON EL CODIGO RECIBIDO



	#Metodo: listarAreas
	#Funcion: permite mostrar las areas de la clinica
	def listarAreas( self ):
		
		self.widgetListarAreas.show()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#===========================================> CAMAS <===================================================
	#Metodo: nuevaCama
	#Funcion: Despliega la interfaz que permite crear un nueva cama 
	def nuevaCama( self ):

		dialogCama = DialogCama( controlador=self.controladorCama, parent=self )
		dialogCama.exec_()

	#Metodo: modificarCama
	#Funcion: Despliega la interfaz que permite modificar una cama 
	def modificarCama( self ):

		dialogCama = DialogCama( nuevo_registro=False, controlador=self.controladorCama, parent=self )
		dialogCama.exec_()
		

	#Metodo: elimarCama
	#Funcion: permite elimnar camas de la base de datos
	def eliminarCama( self ):

		fila_seleccinada_tabla = self.widgetListarCamas.tableWidgetCamas.currentRow()
		if self.widgetListarCamas.isHidden() or fila_seleccinada_tabla == -1:

			self.dialogInformacion.showMensaje( "Eliminar Cama", 
				"Por favor liste las camas, seleccione de la tabla la que desea eliminar, luego presione 'eliminar Cama' " )

		else:
			cod_cama_eliminar = self.widgetListarCamas.tableWidgetCamas.item(fila_seleccinada_tabla, 0).text()
			print( "eliminar cama: " + cod_cama_eliminar )
			#AQUI SE ELIMINA LA CAMA CON EL CODIGO RECIBIDO


	#Metodo: listarCamas
	#Funcion: permite mostrar un listado de camas del hospital
	def listarCamas( self ):
		
		self.widgetListarAreas.hide()
		self.widgetListarCamas.show()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()


	#=========================================> MEDICAMENTOS <==============================================
	#MEDICAMENTO
	#Metodo: nuevoMedicamento
	#Funcion: Despliega la interfaz que permite insertar medicamentos
	def nuevoMedicamento( self ):

		dialogMedicamento = DialogMedicamento( controlador=self.controladorMedicamento, parent=self )
		dialogMedicamento.exec_()

	#Metodo: modificarMedicamento
	#Funcion: Despliega la interfaz que permite modificar medicamentos medicamento
	def modificarMedicamento( self ):

		dialogMedicamento = DialogMedicamento( nuevo_registro=False, controlador=self.controladorMedicamento, parent=self )
		dialogMedicamento.exec_()



	#Metodo: eliminarMedicamento
	#Funcion: permite eliminar el medicamento seleccinado de la base de datos 
	def eliminarMedicamento( self ):

		fila_seleccinada_tabla = self.widgetListarMedicamentos.tableWidgetMedicamentos.currentRow()
		if self.widgetListarMedicamentos.isHidden or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Medicamento", 
				"Por favor liste los medicamento, seleccione de la tabla la que desea eliminar,"
				"luego presione 'Eliminar Medicamento' " )
			
		else:
			cod_med_eliminar = self.widgetListarMedicamentos.tableWidgetMedicamentos.item(fila_seleccinada_tabla, 0).text()
			print( "eliminar medicameto: " + cod_med_eliminar )
			#AQUI SE ELIMINA EL MEDICAMENTO CON EL CODIGO RECIBIDO



	#Metodo: listarMedicamentos
	#Funcion: permite mostrar el listado de medicamentos disponibles en la clinica
	def listarMedicamentos( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.show()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()


	#=========================================> HABILIDADES <===============================================
	#Metodo: nuevaHabilidad
	#Funcion: Despliega el dialog que permite ingresar habilidades a la base de datos
	def nuevaHabilidad( self ):

		dialogHabilidad = DialogHabilidad( controlador=self.controladorHabilidad, parent=self )
		dialogHabilidad.exec_()

	#Metodo: modificarHabilidad
	#Funcion: Despliega el dialog que permite modificar las habilidades
	def modificarHabilidad( self ):

		dialogHabilidad = DialogHabilidad( nuevo_registro=False, controlador=self.controladorHabilidad, parent=self )
		dialogHabilidad.exec_()



	#Metodo: eliminarHabilidad
	#Funcion: Permite eliminar la habilidad seleccionada de la base de datos
	def eliminarHabilidad( self ):

		fila_seleccinada_tabla = self.widgetListarHabilidades.tableWidgetHabilidades.currentRow()
		if self.widgetListarHabilidades.isHidden() or fila_seleccinada_tabla == -1:
			
			self.dialogInformacion.showMensaje( "Eliminar Habilidad", 
				"Por favor liste las habilidades, seleccione de la tabla la que desea eliminar, luego presione 'Eliminar habilidad' " )

		else:
			cod_hab_eliminar = self.widgetListarHabilidades.tableWidgetHabilidades.item(fila_seleccinada_tabla, 0).text()
			print( "eliminar habilidad: " + cod_hab_eliminar )
			#AQUI SE ELIMINA LA HABILIDAD CON EL CODIGO RECIBIDO



	#Metodo: listarHabilidades
	#Funcion: Permite listar las habilidades de una enfermera registradas en la base de datos
	def listarHabilidades( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.show()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#===========================================> CAUSAS <==================================================
	#Metodo: nuevaCausa
	#Funcion: Permite mostrar la interfaz de ingreso de causas a la base de datos
	def nuevaCausa( self ):

		dialogCausa = DialogCausa( controlador=self.controladorCausa ,parent=self )
		dialogCausa.exec_()

	#Metodo: modificarCausa
	#Funcion: Permite modificar la causa seleccionada 
	def modificarCausa( self ):

		dialogCausa = DialogCausa( nuevo_registro=False, controlador=self.controladorCausa ,parent=self )
		dialogCausa.exec_()
		

	#Metodo: eliminarCausa
	#Funcion: Permite eliminar causas de la base de datos
	def eliminarCausa( self ):

		fila_seleccinada_tabla = self.widgetListarCausas.tableWidgetListarCausas.currentRow()
		if self.widgetListarCausas.isHidden() or fila_seleccinada_tabla == -1:

			self.dialogInformacion.showMensaje( "Eliminar Causa", 
				"Por favor liste las causas, seleccione de la tabla la que desea eliminar, luego presione 'Eliminar Causa' " )

		else:

			cod_cau_eliminar = self.widgetListarCausas.tableWidgetListarCausas.item(fila_seleccinada_tabla, 0).text()
			print( "eliminar medicameto: " + cod_cau_eliminar )
			#AQUI SE ELIMINA LA CAUSA CON EL CODIGO RECIBIDO

	def listarCausas( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.show()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()


	#==========================================> INFROMES <=================================================
	#Metodo: mostrarAgendaMedico
	#Funcion: Permite visualizar la agenda programada del medico en un mes determinado
	def agendaMedico( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.show()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#Metodo: mostrarHistoriaClinicaPaciente
	#Funcion: Permite visualizar la historia clinica de un paciente
	def historiaClinicaPaciente( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.show()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.hide()

	#Metodo: mostrarCitasAtendidasMedicoMes
	#Funcion: Permite visualizar las citas que ha atendido un medico en determinado mes
	def citasAtendidasMedicoMes( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()
		
		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.show()
		self.widgetCostoPromedioPaciente.hide()
	
	#Metodo: mostrarCostoPaciente
	#Funcion: Permite visualizar el costo de un paciente
	def costoPaciente( self ):

		self.widgetListarAreas.hide()
		self.widgetListarCamas.hide()
		self.widgetListarMedicamentos.hide()
		self.widgetListarHabilidades.hide()
		self.widgetListarCausas.hide()

		self.widgetEmpleadosPorArea.hide()
		self.widgetAgendaMedicoMes.hide()
		self.widgetHistoriaClinicaPaciente.hide()
		self.widgetNumeroCitasMedico.hide()
		self.widgetCostoPromedioPaciente.show()
	

	def closeEvent(self, event):
		#************************************************************************
		# CERRAR LA CONEXION EN LA BASE DE DATOS
		self.fachada.cerrarConexion()
		#************************************************************************
		event.accept()
