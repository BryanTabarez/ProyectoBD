from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from componentes_administrador import *
import psycopg2

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
		self.dialogInformacion = DialogInformacion( self )
		self.controladorPaciente = controlador 
		self.nuevo_registro = nuevo_registro		

		#============================================> SENIALES Y SLOTS 
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarPaciente )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar ) 
		self.connect( self.pushButtonEliminar, SIGNAL( "clicked()" ), self.eliminar )
		
		#============================================> MODIFICACIONES 

		#self.lineEditIdentificacionPaciente.setReadOnly( True )
		self.lineEditNumeroDeHistoria.setReadOnly( True )
		self.dateEditFechaApertura.setReadOnly( True )

		if self.nuevo_registro:
			
			self.setWindowTitle( "Nuevo Paciente" )
			self.pushButtonInsertar.setText( "Insertar" )
			self.pushButtonConsultar.hide()
			self.pushButtonEliminar.hide()
			
		else:

			self.setWindowTitle( "Modificar Paciente" )
			self.pushButtonInsertar.setText( "Actualizar" )
			self.pushButtonConsultar.show()
			self.pushButtonEliminar.show()
			self.pushButtonEliminar.setEnabled (False)

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
			resultado = self.controladorPaciente.ingresarPaciente( identificacion, nombre, direcccion, telefono, 
				fecha_nacimiento, actividad_economica, nss )

			if isinstance ( resultado, Exception ):
				self.dialogInformacion.showMensaje( "Ingresar Paciente", resultado.pgerror )
			else:
				self.dialogInformacion.showMensaje( "Ingresar Paciente", "El paciente fue ingresado con exito" )
				self.limpiarCampos()
			
		else:
			#EN CASO DE QUE SEA UNA ACTUALIZACION
			resultado = self.controladorPaciente.modificarPacinete(identificacion, nombre, direcccion, telefono, 
				fecha_nacimiento, actividad_economica, nss )

			if isinstance ( resultado, Exception ):
				self.dialogInformacion.showMensaje( "Actualizar Paciente", resultado.pgerror )
			else:
				self.dialogInformacion.showMensaje( "Actualizar Paciente", "El Paciente fue actualizado con exito" )
				self.limpiarCampos()
	
		

	def limpiarCampos( self ):

		self.lineEditIdentificacion.setText( "" )
		self.lineEditNombre.setText( "" )
		self.lineEditDireccion.setText( "" )
		self.lineEditTelefono.setText( "" )
		self.lineEditActividadEconomica.setText( "" )
		self.lineEditNumeroDeSeguridadSocial.setText( "" )

	
	def consultar( self ):
		id_paciente = str( self.lineEditIdentificacion.text() )
		datos_paciente = self.controladorPaciente.consultar( id_paciente )
		
		if isinstance (datos_paciente, Exception):

			self.dialogInformacion.showMensaje( "Consultar Paciente", datos_paciente.pgerror )

		elif datos_paciente == 0:

			self.dialogInformacion.showMensaje( "Consultar Paciente", 
				"El paciente no se encuentra en la base de datos" )

		else:	

			self.pushButtonEliminar.setEnabled (True)
		
			self.lineEditIdentificacion.setText( str( datos_paciente[0] ) )
			self.lineEditNombre.setText( datos_paciente[1] )
			self.lineEditDireccion.setText( datos_paciente[2] )
			self.lineEditTelefono.setText( datos_paciente[3] )
			date = datos_paciente[4]
			anio = int(date.strftime("%Y"))
			mes = int(date.strftime("%m"))
			dia = int(date.strftime("%d"))
			fecha = QDate(2014,5,12)
			self.dateEditFechaNacimiento.setDate(fecha)
			self.lineEditActividadEconomica.setText( datos_paciente[5] )
			self.lineEditNumeroDeSeguridadSocial.setText( str(datos_paciente[6]) )


	def eliminar( self ):

		id_paciente = str(self.lineEditIdentificacion.text())
		resultado = self.controladorPaciente.borrarPaciente( id_paciente )

		if isinstance (resultado, Exception):
			self.dialogInformacion.showMensaje( "Eliminar Paciente" , resultado.pgerror )
		else:
		  	self.dialogInformacion.showMensaje( "Eliminar Paciente", "El paciente fue eliminado con exito" )


#====================================================> CAMAS <==========================================================

D_Asignar_Cama_class , D_Asignar_Cama_Base_class = uic.loadUiType( 'gui/enfermera_uis/DialogCama.ui' )

class DialogCama( QDialog, D_Asignar_Cama_class ):

	def __init__( self, asignar=True, 
		controladorCama=None, 
		controladorPaciente=None,
		controladorCamaPaciente=None, 
		parent=None):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#========================================> VARIABELS 
		self.dialogInformacion  = DialogInformacion( self )
		self.controladorCama = controladorCama
		self.controladorPaciente = controladorPaciente
		self.controladorCamaPaciente = controladorCamaPaciente
		self.asignar = asignar
		self.header1 = QStringList()
		self.header1 << "Numero Cama" << "Descripcion" << "Codigo Area" << "Area"
		self.header2 = QStringList()
		self.header2 << "Numero Cama" << "Area"
		#=========================================> SENIALES Y SLOTS
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )
		self.connect( self.pushButtonAsignar, SIGNAL( "clicked()" ), self.asignarLiberarCama  )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )

		#=========================================> MODIFICACIONES 
		if self.asignar:

			self.setWindowTitle( "Asignar Cama Paciente" )
			self.pushButtonAsignar.setText( "Asignar" )
			self.labelCamas.setText( "Camas disponibles por areas" )
			self.tableWidgetCamas.insertColumn( 0 )
			self.tableWidgetCamas.insertColumn( 0 )
			self.tableWidgetCamas.insertColumn( 0 )
			self.tableWidgetCamas.insertColumn( 0 )
			self.tableWidgetCamas.setHorizontalHeaderLabels( QStringList( self.header1 ) )
			
		else:

			self.setWindowTitle( "Liberar Cama Paciente" )
			self.pushButtonAsignar.setText( "Liberar" )
			self.labelCamas.setText( "Cama asignada a paciente" )
			self.tableWidgetCamas.insertColumn( 0 )
			self.tableWidgetCamas.insertColumn( 0 )
			self.tableWidgetCamas.setHorizontalHeaderLabels( QStringList( self.header2 ) )
	
			

		
	#===========================================> METODOS

	
	def consultar( self ):
		id_paciente = str( self.lineEditIdentificacion.text() )
		datos_paciente = self.controladorPaciente.consultar( id_paciente )

		if isinstance ( datos_paciente, Exception ):
			self.dialogInformacion.showMensaje( "Consultar Paciente", datos_paciente.pgerror )
		if datos_paciente == 1:
			self.dialogInformacion.showMensaje( "Consultar Paciente", 
				"El paciente no se encuentra en la base de datos" )
			self.limpiarCampos()

		else:	
				
			self.lineEditIdentificacion.setText( str( datos_paciente[0] ) )
			self.lineEditNombre.setText( str(datos_paciente[1]) )
			self.actualizarTablaCamasDisponibles(id_paciente)


	
	def actualizarTablaCamasDisponibles( self, id_paciente ):

		if self.asignar:
			#AQUI SE LISTAN LAS CAMAS DISPONIBLES
			matriz_camas = self.controladorCama.listarCamas(True)

			if isinstance ( matriz_camas, Exception ):
				self.dialogInformacion.showMensaje( "Actualizar Camas Disponibles",
					matriz_camas.pgerror )
			else:

				for i in range(0, self.tableWidgetCamas.rowCount()):
					self.tableWidgetCamas.removeRow(0)
				
				print matriz_camas				
				for row in matriz_camas:
				
					self.tableWidgetCamas.insertRow( 0 )
					self.tableWidgetCamas.setItem( 0, 0, QTableWidgetItem( str(row[0]) ) )
					self.tableWidgetCamas.setItem( 0, 1, QTableWidgetItem( str(row[1]) ) )
					self.tableWidgetCamas.setItem( 0, 2, QTableWidgetItem( str(row[2]) ) )
					self.tableWidgetCamas.setItem( 0, 3, QTableWidgetItem( str(row[3]) ) )
	
			
		else:
			#AQUI SE LISTA LA CAMA QUE TIENE EL PACIENTE SI LA TIENE ASIGNADA
			matriz_camas = self.controladorCamaPaciente.consultarCamaPaciente(id_paciente)
			
			if isinstance ( matriz_camas, Exception ):
				self.dialogInformacion.showMensaje( "Liberar Cama ", 
					matriz_camas.pgerror )

			elif matriz_camas == 1:
				self.dialogInformacion.showMensaje( "Liberar Cama", 
					"No se encontro infromacion del usuario en la base de datos")


			else:

				for i in range(0, self.tableWidgetCamas.rowCount()):
					self.tableWidgetCamas.removeRow(0)
				
				for row in matriz_camas:
					
					self.tableWidgetCamas.insertRow( 0 )
					self.tableWidgetCamas.setItem( 0, 0, QTableWidgetItem( str(row[0]) ) )
					self.tableWidgetCamas.setItem( 0, 1, QTableWidgetItem( row[1] ) )
					
			

	def asignarLiberarCama( self ):
		
		fila_seleccionada = self.tableWidgetCamas.currentRow()
		if fila_seleccionada > -1:
			identificacon = str( self.lineEditIdentificacion.text() ) 
			num_cama = str ( self.tableWidgetCamas.item( fila_seleccionada, 0 ).text() )

			if self.asignar:
				#AQUI SE ASIGNA LA CAMA AL PACIENTE
				(asg_cama, cambio_estado) = self.controladorCamaPaciente.ingresarCamaPaciente( 
					num_cama, identificacon, "now()")
				
				if isinstance ( asg_cama, Exception ):
					
					self.dialogInformacion.showMensaje( "Asignar Cama", asg_cama.pgerror )
				
				elif isinstance ( cambio_estado, Exception ):

					self.dialogInformacion.showMensaje( "Cambiar estado cama Ocupada", cambio_estado.pgerror )

				else:

					self.dialogInformacion.showMensaje( "Asignar Cama", "La cama fue asignada con exito" )

					self.actualizarTablaCamasDisponibles(identificacon)
				
			else:
				#AQUI SE LIBERA LA CAMA DEL PACIENTE
				
				r_liberar_cama = self.controladorCamaPaciente.liberarCama( num_cama )

				if isinstance ( r_liberar_cama , Exception ):

					self.dialogInformacion.showMensaje( "Liberar Cama", r_liberar_cama.pgerror )

				else: 

					self.dialogInformacion.showMensaje( "Liberar Cama" , "La cama fue liberada con exito")

					self.actualizarTablaCamasDisponibles(identificacon)
		
		else:

			if self.asignar:
				self.dialogInformacion.showMensaje( "Asignar Cama",
					"Por favor seleccione la cama que desea asignar" )
			else:
				self.dialogInformacion.showMensaje( "Liberar Cama",
					"Por favor seleccione la cama que desea liberar" )

		self.limpiarCampos()
		

	def limpiarCampos( self ):

		self.lineEditIdentificacion.setText( "" )
		self.lineEditNombre.setText( "" )
		
		

#====================================================> CITAS <==========================================================

D_CitaInterfaz_class , D_CitaInterfazBase_class = uic.loadUiType( 'gui/enfermera_uis/DialogCita.ui' )

class DialogCita( QDialog, D_CitaInterfaz_class ):

	def __init__( self, 
		nuevo_registro=True, 
		controladorCita=None,
		controladorMedico=None,
		controladorHorarioMedico=None, 
		parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#=================================================> VARIABLES
		self.dialogInformacion = DialogInformacion( self )
		self.nuevo_registro = nuevo_registro
		self.controladorCita = controladorCita
		self.controladorMedico = controladorMedico
		self.controladorHorarioMedico = controladorHorarioMedico

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

		self.cargarEspecialidadesMedico()

	#====================================================> METODOS

	def cargarEspecialidadesMedico( self ):

		especialidades = self.controladorMedico.listarEspecialidades()

		if isinstance (especialidades, Exception):

			self.dialogInformacion.showMensaje( "Cita", 
				"No fue posible cargar las especialidades de los medicos de la base de datos" )

		else:

			for row in especialidades:
		 		self.comboBoxHorariosDisponibles.addItem( row[0] )



	def cargarHorariosMedicos( self ):

		encabezado = QStringList()
		encabezado << "Identificacion Horario" << "Medico" << "Fecha y Hora"
		self.tableWidgetHorariosDisponibles.insertColumn( 0 )
		self.tableWidgetHorariosDisponibles.insertColumn( 0 )
		self.tableWidgetHorariosDisponibles.insertColumn( 0 ) 
		self.tableWidgetHorariosDisponibles.setHorizontalHeaderLabels( encabezado )
		#especialidad = self.
		#horarios = self.controladorHorarioMedico.

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


	
