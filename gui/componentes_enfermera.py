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

D_Asignar_Cama_class , D_Asignar_Cama_Base_class = uic.loadUiType( 'gui/enfermera_uis/DialogAsignarCama.ui' )

class DialogAsignarCama( QDialog, D_Asignar_Cama_class ):

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
		self.connect( self.pushButtonAsignar, SIGNAL( "clicked" ), self.asignarLiberarCama  )
		self.connect( self.tableWidgetCamas , SIGNAL( "itemClicked( QTableWidgetItem )" ), 
			self.seleccionarCama )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )

		#=========================================> MODIFICACIONES 
		if self.asignar:

			self.setWindowTitle( "Asignar Cama Paciente" )
			self.pushButtonAsignar.setText( "Asignar" )
			self.labelArea.show()
			self.lineArea.show()
			self.comboBoxArea.show()
			self.tableWidgetCamas.show()

		else:

			self.setWindowTitle( "Liberar Cama Paciente" )
			self.pushButtonAsignar.setText( "Liberar" )
			self.labelArea.hide()
			self.lineArea.hide()
			self.comboBoxArea.hide()
			self.tableWidgetCamas.hide()

		self.limpiarCampos()


	#===========================================> METODOS

	def consultar( self ):
		#AQUI SE CONSULTA LA IDENTIFICACION DEL PACIENTE AL QUIE SE LE VA ASIGNAR CAMA
		#identificacon_consultar = str( self.lineEditIndetificacion.text() )
		#self.lineEditNombre.setText( "Nombre paciente" )

		pass

	def actualizar( self ):

		#AQUI SE ACTUALIZAN LOS DATOS DEL COMBO DE AREAS 

		#AQUI SE LISTAN LAS CAMAS DISPONIBLES
		#self.tableWidgetCamas.clearContents()
		#self.tableWidgetCamas.insertRow( 0 )
		#self.tableWidgetCamas.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetCamas.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass


	def seleccionarCama( self, item ):
		fila_seleccionada = self.tableWidgetCamas.currentRow()
		if fila_seleccionada > -1:
			numero_cama_seleccionado = item( fila_seleccionada, 0  ).text()
			self.lineEditNumeroCama.setText( numero_cama_seleccionado )
			self.lineEditArea.setText( self.comboBoxArea.currentText() )

	def asignarLiberarCama( self ):

		if self.asignar:
			#AQUI SE ASIGNA LA CAMA AL PACIENTE
			identificacon = str( self.lineEditIndetificacion.text() ) 
			area_cama = str( self.lineEditArea.text() )
			num_cama = str ( self.lineEditNumeroCama.text() )
			
		else:
			#AQUI SE LIBERA LA CAMA DEL PACIENTE
			pass			
		
		self.limpiarCampos()
		

	def limpiarCampos( self ):

		self.lineEditIndetificacion.setText( "" )
		self.lineEditNombre.setText( "" )
		self.lineEditArea.setText( "" )
		self.lineEditNumeroCama.setText( "" )


#====================================================> CITAS <==========================================================

D_CitaInterfaz_class , D_CitaInterfazBase_class = uic.loadUiType( 'gui/enfermera_uis/DialogCita.ui' )

class DialogCita( QDialog, D_CitaInterfaz_class ):

	def __init__( self, id_paciente, nombre_paciente , parent ):

		QDialog.__init__( self, parent )
		self.setupUi( self )


		self.dialogInformacion = DialogInformacion( self )

		self.lineEditIdentificacion.setText( id_paciente )
		self.lineEditNombre.setText( nombre_paciente )

		self.connect( self.pushButtonAsignarCita, SIGNAL( "clicked()" ), self.asignarCitaPaciente )

	def asignarCitaPaciente( self ):

		fila_seleccionada = self.tableWidgetHorarios.currentRow()
		if fila_seleccionada == -1:

			self.dialogInformacion.showMensaje( "Asignar Cita", 
				"Por favor selcciones el horario en el cual desea que se realice la cita" )

		else:

			print("CITA ASIGNADA")
