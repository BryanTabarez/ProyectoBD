from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from componentes_administrador import DialogInformacion

#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazEnfermera

#=======================================================================================================================

#====================================================> PACIENTE <=======================================================

D_Paciente_class , D_PacienteBase_clas = uic.loadUiType('gui/enfermera_uis/DialogPaciente.ui')

class DialogPaciente( QDialog, D_Paciente_class ):
	
	
	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Consfiguracion interfaz
		self.setupUi( self )
		
		#=============================================> VARIABLES 
		self.controladorPaciente = controlador
		self.nuevo_registro = nuevo_registro		

		#============================================> SENIALES Y SLOTS 
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarPaciente )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked" ), self.consultar ) 
		
		#============================================> MODIFICACIONES 

		self.lineEditIdentificacionPaciente.setReadOnly( True )
		self.lineEditNumeroDeHistoria.setReadOnly( True )
		self.dateEditFechaApertura.setReadOnly( True )

		if self.nuevo_registro:
			
			self.setWindowTitle( "Nuevo Paciente" )
			self.pushButtonInsertar.setText( "Insertar" )
			self.pushButtonConsultar.hide()
			
		else:

			self.setWindowTitle( "Modificar Paciente" )
			self.pushButtonInsertar.setText( "Actualizar" )
			self.pushButtonConsultar.show()

	#=====================================================> METODOS
	def insertarActualizarPaciente( self ):

		identificacion = str( self.lineEditIdentificacion.text() )
		nombre = str( self.lineEditNombre.text() )
		direcccion = str( self.lineEditDireccion.text() )
		telefono = str( self.lineEditTelefono.text() )
		fecha_nacimiento = str( self.dateEditFechaNacimiento.text() )
		actividad_economica = str( self.lineEditActividadEconomica.text() )
		nss = str( self.lineEditNumeroDeSeguridadSocial.text() )

		#La informacion de de historia clinica se crea por medio de un trigger en la base de datos

		#AQUI SE INSERTA EL PACIENTE A LA BASE DE DATOS
		if self.nuevo_registro:
			#EN CASO DE QUE SEA UN NUEVO REGISTRO 
			pass
			
		else:
			#EN CASO DE QUE SEA UNA ACTUALIZACION
			pass
		
		self.limpiarCampos()

	def limpiarCampos( self ):

		self.lineEditIdentificacion.setText( "" )
		self.lineEditNombre.setText( "" )
		self.lineEditDireccion.setText( "" )
		self.lineEditTelefono.setText( "" )
		self.lineEditActividadEconomica.setText( "" )
		self.lineEditNumeroDeSeguridadSocial.setText( "" )

	def consultar( self ):

		#AQUI VA LA CONSULTA ACERCA DE DEL PACIENTE
		pass





#===================================================> Listar Pacientes 

W_ListarPacientes_class , W_LsitarPacientesBase_class = uic.loadUiType( 'gui/enfermera_uis/WidgetListarPacientes.ui' )

class WidgetListarPacientes( QWidget, W_ListarPacientes_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )



		#======================================= VARIABLES
		self.controladorPaciente = " " #AQUI VA EL CONTROLADOR DE PACIENTE

	#==================================================> METODOS 

	def actualizar( self ):

		#AQUI SE LISTAN LOS PACIENTES DE LA BASE DE DATOS
		#self.tableWidget.clearContents()
		#self.tableWidget.insertRow( 0 )
		#self.tableWidget.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidget.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass

#====================================================> CAMAS <==========================================================

D_Asignar_Cama_class , D_Asignar_Cama_Base_class = uic.loadUiType( 'gui/enfermera_uis/DialogCama.ui' )

class DialogCama( QDialog, D_Asignar_Cama_class ):

	def __init__( self, asignar=True, controladorPaciente=None,controladorCama=None, parent=None):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#========================================> VARIABELS 
		self.dialogInformacion  = DialogInformacion( self )
		self.controladorPaciente = controladorPaciente
		self.contrladorCama = controladorCama
		self.asignar = asignar
		
		#=========================================> SENIALES Y SLOTS
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )
		self.connect( self.pushButtonAsignar, SIGNAL( "clicked()" ), self.asignarLiberarCama  )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )

		#=========================================> MODIFICACIONES 
		if self.asignar:

			self.setWindowTitle( "Asignar Cama Paciente" )
			self.pushButtonAsignar.setText( "Asignar" )
			
		else:

			self.setWindowTitle( "Liberar Cama Paciente" )
			self.pushButtonAsignar.setText( "Liberar" )
			

		
	#===========================================> METODOS

	def actualizar( self ):

		#AQUI SE ACTUALIZAN LOS DATOS DEL COMBO DE AREAS 

		#AQUI SE LISTAN LAS CAMAS DISPONIBLES
		#self.tableWidgetCamas.clearContents()
		#self.tableWidgetCamas.insertRow( 0 )
		#self.tableWidgetCamas.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetCamas.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass

	

	def consultar( self ):
		#AQUI SE CONSULTA LA IDENTIFICACION DEL PACIENTE AL QUIE SE LE VA ASIGNAR CAMA
		#identificacon_consultar = str( self.lineEditIndetificacion.text() )
		#self.lineEditNombre.setText( "Nombre paciente" )

		pass
	

	def asignarLiberarCama( self ):
		print("Asignar cama")
		fila_seleccionada = self.tableWidgetCamas.currentRow()
		if fila_seleccionada > -1:
			identificacon = str( self.lineEditIndetificacion.text() ) 
			area_cama = str( self.comboBoxArea.currentText() )
			num_cama = str ( self.tableWidgetCamas.item( fila_seleccionada, 0 ).text() )

			if self.asignar:
				#AQUI SE ASIGNA LA CAMA AL PACIENTE
				pass
				
				
			else:
				#AQUI SE LIBERA LA CAMA DEL PACIENTE
				pass			
		
		else:

			if self.asignar:
				self.dialogInformacion.showMensaje( "Asignar Cama",
					"Por favor seleccione la cama que desea asignar" )
			else:
				self.dialogInformacion.showMensaje( "Liberar Cama",
					"Por favor seleccione la cama que desea liberar" )

		self.limpiarCampos()
		

	def limpiarCampos( self ):

		self.lineEditIndetificacion.setText( "" )
		self.lineEditNombre.setText( "" )
		
		

#====================================================> CITAS <==========================================================

D_CitaInterfaz_class , D_CitaInterfazBase_class = uic.loadUiType( 'gui/enfermera_uis/DialogCita.ui' )

class DialogCita( QDialog, D_CitaInterfaz_class ):

	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#=================================================> VARIABLES
		self.dialogInformacion = DialogInformacion( self )
		self.nuevo_registro = nuevo_registro
		self.controladorCita = controlador

		#=================================================> SENIALES Y SLOTS
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )
		self.connect( self.pushButtonAsignar, SIGNAL( "clicked()" ), self.asignarCancelarCitas )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )
		

		#=================================================> MODIFICACIONES 

		
		if self.nuevo_registro:
		
			self.setWindowTitle( "Nueva Cita" )
			self.pushButtonAsignar.setText( "Asignar" )
			
			self.cargarHorariosMedicos()

		else: 

			self.setWindowTitle( "Cancelar Cita" )
			self.pushButtonAsignar.setText( "Cancelar Cita" )
			
			self.cargarCitasPaciente()


	#====================================================> METODOS

	def cargarHorariosMedicos( self ):

		encabezado = QStringList()
		encabezado << "Identificacion Horario" << "Identificacion Medico" << "Fecha y Hora"
		self.tableWidgetHorariosDisponibles.setHorizontalHeaderLabels( encabezado )

		#AQUI SE LISTAN LAS CAMAS EN LA TABLA DE CAMAS 
		#self.tableWidgetMedicamentos.clearContents()
		#self.tableWidgetMedicamentos.insertRow( 0 )
		#self.tableWidgetMedicamentos.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetMedicamentos.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		

	def cargarCitasPaciente( self ):

		encabezado = QStringList()
		encabezado << "Identificacion  medico" << "Fecha y Hora" << "Tipo solicitud"
		self.tableWidgetHorariosDisponibles.setHorizontalHeaderLabels( encabezado )
		#AQUI SE LISTAN LAS CAMAS EN LA TABLA DE CAMAS 
		#self.tableWidgetMedicamentos.clearContents()
		#self.tableWidgetMedicamentos.insertRow( 0 )
		#self.tableWidgetMedicamentos.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetMedicamentos.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		


	def consultar( self ):
		#AQUI SE VA A CONSULTAR LA INDENTIFICACION DEL PACIENTE 
		pass



	def asignarCancelarCitas( self ):

		id_pacaciente = str( self.lineEditIndetificacion.text() )
		#numero_historia = str( self.lineEditNumeroHistoria.text() )
		#id_horario = str( self.lineEditIdHorario.text() )
		#tipo_solicitud = str( self.comboBoxTipoSolicitud.currentText() )

		fila_seleccionada = self.tableWidgetHorariosDisponibles.currentRow()
		if fila_seleccionada > -1:
			#AQUI SE VA A ASIGNAR LAS CITAS PARA EL PACIENTE 
			if self.nuevo_registro:
				#EN CASO DE QUE SE DESEE HACE UNA CITA 
				id_pacaciente = str( self.lineEditIndetificacion.text() )
				id_horario = str( self.tableWidgetHorariosDisponibles.item( fila_seleccionada, 0).text() )
				pass


			else:
				#EN CASO DE QUE SE VALLA A CANCELAR UNA CITA 
				id_pacaciente = str( self.lineEditIndetificacion.text() )
				id_horario = str( self.tableWidgetHorariosDisponibles.item( fila_seleccionada, 0).text() )

				pass
		else:

			if self.nuevo_registro:
				self.dialogInformacion.showMensaje( "Nueva Cita" ,
					"Por favor seleccione de la tabla el horario de la cita" )
			else:
				self.dialogInformacion.showMensaje( "Cancelar Cita",
					"Por favor seleccione de la tabla la cita que desea cancelar" )

		self.limpiarCampos
			
	def limpiarCampos( self ):

		self.lineEditIndetificacion.setText( "" )
		self.lineEditNombre.setText( "" )
		

#========================================================> AGENDA MEDICO <==============================================

D_Agenda_Medico_class , D_Agenda_Medico_Base_class = uic.loadUiType( 'gui/enfermera_uis/DialogAgendaMedico.ui' )

class DialogAgendaMedico( QDialog,  D_Agenda_Medico_class):

	def __init__( self, controlador=None, parent=None,  ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#======================================> VARIABLES 
		self.dialogInformacion = DialogInformacion( self )
		self.controladorAgenda = controlador

		#======================================> SENIALES Y SLOTS
		self.connect( self.pushButtonConsultarMedico, SIGNAL( "clicked()" ), self.consultar )
		self.connect( self.pushButtonGenerarHorario, SIGNAL( "clicked()" ), self.generarHorario )
		self.connect( self.pushButtonEliminarRegistro, SIGNAL( "clicked()" ), self.eliminarRegistro )

	def consultar( self ):

		id_medico = str( self.lineEditIndentificacion.text() )
		#AQUI VA LA CONSULTA DEL MEDICO 

	def generarHorario( self ):

		time_ini_manana = self.dateTimeEditInicioM.time()
		time_fin_manana = self.dateTimeEditFinM.time()
		time_ini_tarde = self.dateTimeEditInicioT.time()
		time_fin_tarde = self.dateTimeEditFinT.time()

		self.generarHorariosMes( iniM=time_ini_manana, finM=time_fin_manana, iniT=time_ini_tarde, finT=time_fin_tarde  )

	def generarHorariosMes( self, iniM, finM, iniT, finT ):
		pass


	def eliminarRegistro( self ):
		fila_seleccionada = self.tableWidgetHorario.currentRow()
		if fila_seleccionada > -1:
			id_horario = str( self.tableWidgetHorario.item( fila_seleccionada, 0 ).text() )
			#AQUI SE ELIMINA EL HORARIO DE LA BASE DE DATOS 

		else:

			self.dialogInformacion.showMensaje( "Agenda Medico",
				"Por favor selecciones el horario que desea eliminar de la tabla" )


