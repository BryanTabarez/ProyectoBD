from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic


#=======================================================================================================================
# INTEGRANTES:
# Bryan Stiven Tabarez Mestra	- 1131782
# Aurelio Antonio Vivas Meza	- 1110348
# George Romero Ramirez		    - 1130924
#=======================================================================================================================
#InterfazEnfermera

#=======================================================================================================================


#=============================================> DIALOGO DE INFORMACION <================================================

D_Informacion_class , D_Informacion_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogInformacion.ui' )

class DialogInformacion( QDialog, D_Informacion_class ):

	def __init__( self, parent=None ):

		QDialog.__init__( self, parent )
		self.setupUi( self )

	def showMensaje( self, encabezado, mensaje ):

		self.labelEncabezado.setText( encabezado )
		self.plainTextEditCuerpo.setPlainText( mensaje )
		self.show()



#=============================================> EMPLEADO <==============================================================


D_Empleado_class , D_Emeplado_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogEmpleado.ui' )

class DialogEmpleado( QDialog, D_Empleado_class ):


	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):


		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion de la interfaz
		self.setupUi( self )


		#=========================================> VARIABLES
		self.controaldorEmpleado = controaldor
		self.nuevo_regsitro = nuevo_regsitro
		
		#=========================================> WIDGETS 
		self.widgetTipoEmpleadoEnfermera = WidgetTipoEmpleadoEnfermera( self.widgetTipoEmpleado )
		self.widgetTipoEmpleadoEnfermera.hide()
		self.widgetTipoEmpleadoMedico = WidgetTipoEmpleadoMedico( self.widgetTipoEmpleado )
		self.widgetTipoEmpleadoMedico.hide()

		#=========================================> SENIALES Y SLOTS 
		self.connect( self.comboBoxTipoEmpleado, SIGNAL( "currentIndexChanged(int)" ), self.mostarTipoEmpleado )
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarEmpleado )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )

		#==========================================>MODIFICACIONES
		
		if nuevo_regsitro:			

			self.setWindowTitle("Nuevo Empleado")
			self.widgetCuerpo.pushButtonInsertar.setText("Insertar")
			self.widgetCuerpo.pushButtonConsultar.hide()

		else:			

			self.setWindowTitle("Actualizar Empleado")
			self.widgetCuerpo.pushButtonInsertar.setText("Actualizar")
			self.widgetCuerpo.pushButtonConsultar.show()


	
	#=============================================> METODOS
	def mostarTipoEmpleado( self, indice ):

		if( indice == 0 ):

			self.widgetTipoEmpleadoEnfermera.show()
			self.widgetTipoEmpleadoMedico.hide()
		
		elif( indice == 1 ):
			
			self.widgetTipoEmpleadoMedico.show()
			self.widgetTipoEmpleadoEnfermera.hide()


	def insertarActualizarEmpleado( self ):

		identificacion = self.widgetCuerpo.lineEditIdentificacion.text()
		nombre = self.widgetCuerpo.lineEditNombre.text()
		direccion = self.widgetCuerpo.lineEditDireccion.text()
		telefono = self.widgetCuerpo.lineEditTelefono.text()
		email = self.widgetCuerpo.lineEditEmail.text()
		salario = self.widgetCuerpo.lineEditEmail.text()
		cargo = self.widgetCuerpo.lineEditCargo.text()
		codigo_area = self.widgetCuerpo.comboBoxCodigoArea.currentText()
		codigo_jefe = self.widgetCuerpo.comboBoxCodigoJefe.currentText()

		indice =  self.comboBoxTipoEmpleado.currentIndex() 
		if indice == 0:

			anios_experiencia = self.widgetCuerpo.widgetTipoEmpleadoEnfermera.lineEditAniosExperiencia.text()
			numero_filas = self.widgetCuerpo.widgetTipoEmpleadoEnfermera.tableWidgetHabilidades.rowCount()
			arreglo_habilidades = self.widgetCuerpo.widgetTipoEmpleadoEnfermera.habilidadesEnfermera()
			
			#INSERTE DATOS A LA BASE DE DATOS DE ENFERMERAS 
			if self.nuevo_regsitro:
				#Cuando la opeacion de de insercion 
				pass

			else:
				#Cuando la operacion es de actualizacion 
				
				pass

		else:

			especialidad = self.widgetCuerpo.widgetTipoEmpleadoMedico.lineEditEspecialidad.text()
			universidad = self.widgetCuerpo.widgetTipoEmpleadoMedico.lineEditUniversidad.text()
			numero_licencia = self.widgetCuerpo.widgetTipoEmpleadoMedico.lineEditNumeroLicencia.text()
			
			#INSERTE DATOS A LA BASE DE DATOS DE MEDICOS
			if self.nuevo_regsitro:
				#Cuando la opeacion de de insercion 
				pass

			else:
				#Cuando la operacion es de actualizacion
				pass

		self.limpiarCampos()


	def limpiarCampos( self ):

		self.widgetCuerpo.lineEditIdentificacion.setText("")
		self.widgetCuerpo.lineEditNombre.setText("")
		self.widgetCuerpo.lineEditDireccion.setText("")
		self.widgetCuerpo.lineEditTelefono.setText("")
		self.widgetCuerpo.lineEditEmail.setText("")
		self.widgetCuerpo.lineEditEmail.setText("")
		self.widgetCuerpo.lineEditCargo.setText("")
		#self.widgetCuerpo.comboBoxCodigoArea.currentText()
		#self.widgetCuerpo.comboBoxCodigoJefe.currentText()

		self.widgetCuerpo.widgetTipoEmpleadoEnfermera.lineEditAniosExperiencia.setText("")
		self.widgetCuerpo.widgetTipoEmpleadoEnfermera.tableWidgetHabilidades.setText("")
		self.widgetCuerpo.widgetTipoEmpleadoEnfermera.tableWidgetHabilidadesEnfermera.clear()

		self.widgetCuerpo.widgetTipoEmpleadoMedico.lineEditEspecialidad.setText("")
		self.widgetCuerpo.widgetTipoEmpleadoMedico.lineEditUniversidad.setText("")
		self.widgetCuerpo.widgetTipoEmpleadoMedico.lineEditNumeroLicencia.setText("")


	def consultar( self ):

		#AQUI VA LA CONSULTA DEL CODIGO DEL EMPLEADO
		pass


#============================================> TIPO EMPLEADO ENFERMERA <================================================

W_Enfermera_class , W_Enfermera_Base_class = uic.loadUiType('gui/administrador_uis/WidgetTipoEmpleadoEnfermera.ui')

class WidgetTipoEmpleadoEnfermera( QWidget, W_Enfermera_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion de la interfaz	
		self.setupUi( self )

		#=============================================> VARIABLES
		indice = 0

		#=============================================> SENIALES Y SLOTS
		self.connect( self.pushButtonAgregar, SIGNAL( "clicked()" ), self.agregar )
		self.connect( self.pushButtonEliminar, SIGNAL( "clicked()" ), self.eliminar )

	#==================================================> METODOS 


	def agregar( self ):

		fila_seleccionada = self.tableWidgetHabilidades.currentRow()
		if fila_seleccionada == -1:
			self.dialogInformacion = DialogInformacion( self )
			self.dialogInformacion.showMensaje( "Nuevo Empleado"
				,"Por favor seleccione un hablidad para la enfermera  de la tabla habilidades" )
		else:

			item = self.tableWidgetHabilidades.item( fila_seleccionada,0 )
			self.tableWidgetHabilidadesEnfermera.insertRow( indice )
			self.tableWidgetHabilidadesEnfermera.setItem( 0, 0, item )
			self.indice = self.indice + 1

	def eliminar( self ):

		fila_seleccionada = self.tableWidgetHabilidadesEnfermera.currentRow()
		if fila_seleccionada == -1:
			self.dialogInformacion = DialogInformacion( self )
			self.dialogInformacion.showMensaje( "Nuevo Empleado"
				,"Por favor seleccione la habilidad de la tabla 'Habilidades Enfermera que desea eliminar'" )
		else:

			item = self.tableWidgetHabilidades.item( fila_seleccionada,0 )
			self.tableWidgetHabilidadesEnfermera.insertRow( indice )
			self.tableWidgetHabilidadesEnfermera.setItem( 0, 0, item )
			self.indice = self.indice -1

	def habilidadesEnfermera( self ):
		numero_filas =  self.tableWidgetHabilidadesEnfermera.rowCount()
		arreglo_habilidades = [None] * numero_filas
		for i in range( 0, numero_filas ):
			value = self.tableWidgetHabilidadesEnfermera.item( i, 0).toString()
			arreglo_habilidades[ i ] = value

		return arreglo_habilidades


#===========================================> TIPO EMPLEADO MEDICO <====================================================

W_Medico_class , W_Medico_Base_class = uic.loadUiType('gui/administrador_uis/WidgetTipoEmpleadoMedico.ui')


class WidgetTipoEmpleadoMedico( QWidget, W_Medico_class ):

	def __init__( self, parent=None ):

		#Constructor padre 
		QWidget.__init__( self, parent )
		#Configuracion de la interfaz
		self.setupUi( self )
	

			

#============================================> EMPLEADOS POR AREAS <====================================================


W_Empleados_Area_class , W__Empleados_Area_Base_class = uic.loadUiType('gui/administrador_uis/WidgetEmpleadosPorArea.ui')

class WidgetEmpleadosPorArea( QWidget , W_Empleados_Area_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion de la interfaz
		self.setupUi( self )

		
#===============================================> AREAS <===============================================================

D_Area_class , D_Area_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogArea.ui' )

class DialogArea( QDialog, D_Area_class ):

	def __init__( self, nuevo_registro=True, contolador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#================================================> VARIABLES
		self.controladorArea = contolador 
		self.nuevo_regsitro = nuevo_regsitro

		#================================================> SENIALES Y SLOTS
		self.controladorAreas = contolador
		self.nuevo_regsitro
		#=================================================> MODIFICACIONES 

		if self.nuevo_regsitro:

			self.setWindowTitle( "Nueva Area" )
			self.pushButtonInsertar.setText( "Insertar" )
			self.pushButtonConsultar.hide()
			self.lineEditCodigo.setText( "Automatico" )
			self.lineEditCodigo.setReadOnly(True)

		else:

			self.setWindowTitle( "Modificar Area" )
			self.pushButtonInsertar.setText( "Actualizar" )
			self.pushButtonConsultar.show()
			self.lineEditCodigo.setText( "" )
			self.lineEditCodigo.setReadOnly(False)


		#=================================================> SENIALES Y SLOTS 
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarArea )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos  )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#====================================================> METODOS

	def insertarActualizarArea( self ):

		codigo = self.lineEditCodigo.text()
		nombre = self.lineEditNombre.text()
		descripcion = self.lineEditDescripcion.text()

		#AQUI SE INSERTA LA INFORMACION A LA BASE DE DATOS
		if nuevo_regsitro:
			#ENCASO DE QUE SEA UN NUEVO REGISTRO
			pass

		else:
			#EN CASO DE QUE SEA UNA ACTUALIZACION
			pass


		self.limpiarCampos

	def limpiarCampos( self ):

		if nuevo_regsitro:
			
			self.lineEditNombre.setText( "" )
			self.lineEditDescripcion.text( "" )
		
		else:
			
			self.lineEditCodigo.setText( "" )
			self.lineEditNombre.setText( "" )
			self.lineEditDescripcion.setText( "" )

	def consultar( self ):

		#AQUI SE CONSULTA EL CODIGO DEL AREA 
		pass

		
#===========================================> LISTAR AREAS <============================================================

W_Areas_class , W_Areas_Base_class = uic.loadUiType('gui/administrador_uis/WidgetListarAreas.ui')


class WidgetListarAreas( QWidget, W_Areas_class ):
	
	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )
	
#===============================================> CAMA <================================================================

D_Cama_class , D_Cama_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogCama.ui' )

class DialogCama( QDialog, D_Cama_class ):

	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#=======================================> VARIABLES
		self.nuevo_registro = nuevo_registro
		self.controladorCama = controlador

		#=================================================> MODIFICACIONES 

		if self.nuevo_regsitro:

			self.setWindowTitle( "Nueva Cama" )
			self.pushButtonInsertar.setText( "Insertar" )
			self.pushButtonConsultar.hide()
			self.lineEditNumeroDeCama.setText( "Automatico" )
			self.lineEditNumeroDeCama.setReadOnly(True)

		else:

			self.setWindowTitle( "Modificar Cama" )
			self.pushButtonInsertar.setText( "Actualizar" )
			self.pushButtonConsultar.show()
			self.lineEditNumeroDeCama.setText( "" )
			self.lineEditNumeroDeCama.setReadOnly(False)


		#========================================> SENIALES Y SLOTS
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarCama )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#============================================> METODOS 
	def insertarActualizarCama( self ):

		codigo_area = self.lineEditCodigoArea.text()
		numero_cama = self.lineEditNumeroDeCama.text()
		descripcion = self.lineEditDescripcion.text()

		#AQUIE SE INGRESAN LOS DATOS A LA BASE DE DATOS
		if self.nuevo_regsitro:
			#EN CASO DE SE UN NUEVO REGISTRO
			pass

		else:
			#EN CASO DE SER UNA ACTUALIZACION 
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_regsitro:
			
			self.lineEditNumeroDeCama.setText( "" ) 
			self.lineEditDescripcion.setText( "" )

		else:

			self.lineEditCodigoArea.setText( "" )
			self.lineEditNumeroDeCama.setText( "" )
			self.lineEditDescripcion.setText( "" )

	def consulta( self ):

		#AQUI VA LA CONSULTA DE LA CAMA 
		pass
			 
#==================================================> LISTAR CAMAS <=====================================================

W_Camas_class , W_Camas_Base_class = uic.loadUiType('gui/administrador_uis/WidgetListarCamas.ui')


class WidgetListarCamas( QWidget, W_Camas_class ):

	def __init__( self, parent=None ):

		#Constructor padre 
		QWidget.__init__( self, parent )
		#Configuracion de la interfaz
		self.setupUi( self )
			


# ===========================================> MEDICAMENTO <============================================================

D_Medicamento_class , D_Medicamento_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogMedicamento.ui' )

class DialogMedicamento( QDialog, D_Medicamento_class ):

	def __init__( self, nuevo_regsitro=True, controlador=None, parent=None ):

		#Construtor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#=====================================> VARIABLES
		self.controladorMedicamento = controlador
		self.nuevo_regsitro = nuevo_regsitro

		#=====================================> MODIFICACIONES

		if self.nuevo_regsitro:

			self.setWindowTitle( "Nuevo Medicamento" )
			self.lineEditCodigo.setText( "Automatico" )
			self.lineEditCodigo.setReadOnly(True)
			self.pushButtonConsultar.hide()

		else:

			self.setWindowTitle( "Actualizar Medicamento" )
			self.lineEditCodigo.setText( "" )
			self.lineEditCodigo.setReadOnly(False)
			self.pushButtonConsultar.show()

		#========================================> SENIALES Y SLOTS
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarMedicamento )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#=============================================> METODOS
	def insertarActualizarMedicamento( self ):

		codigo = self.lineEditCodigo.text()
		nombre = self.lineEditNombre.text()
		costo = self.lineEditCosto.text()
		descripcion = self.lineEditDescripcion.text()

		#AQUI SE INGRESA LA INFOMACION EN LA BASE DE DATOS 
		if self.nuevo_regsitro:
			#EN CASO DE UN NUEVO REGISTRO
			pass
		else:
			#EN CASO DE UNA ACTUALIZACION 
			pass

		self.limpiarCampos()

	def limpiarCapos( self ):

		if self.nuevo_regsitro:

			self.lineEditNombre.text()
			self.lineEditCosto.text()
			self.lineEditDescripcion.text()

		else:

			self.lineEditCodigo.text()
			self.lineEditNombre.text()
			self.lineEditCosto.text()
			self.lineEditDescripcion.text()

	
	def consultar( self ):
		#AQUI VA LA CONSULTA DEL MEDICAMENTO
		pass



#=========================================> Listar medicamentos <=======================================================

W_Medicamentos_class , W_MedicamentosBase_class = uic.loadUiType('gui/administrador_uis/WidgetListarMedicamentos.ui')


class WidgetListarMedicamentos( QWidget, W_Medicamentos_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )	

#===========================================> HABILIDAD <===============================================================

D_Habilidad_class , D_Habilidad_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogHabilidad.ui' )


class DialogHabilidad( QDialog, D_Habilidad_class ):

	def __init__( self, nuevo_regsitro=True, controlador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )
		
		#=========================================> VARIABLES
		self.controladorHabilidad = controlador
		self.nuevo_regsitro = nuevo_regsitro

		#=========================================> MODIFICACIONES 

		if self.nuevo_regsitro:

			self.setWindowTitle( "Nueva Habilidad" )
			self.lineEditCodigo.setReadOnly( True )
			self.lineEditCodigo.setText( "Automatico" )
			self.pushButtonInsertar.setText( "Insertar" )
			self.pushButtonConsultar.hide()

		else:

			self.setWindowTitle( "Nueva Habilidad" )
			self.lineEditCodigo.setReadOnly( False )
			self.lineEditCodigo.setText( "" )
			self.pushButtonInsertar.setText( "Actualizar" )
			self.pushButtonConsultar.show()

		#=============================================> SENIALES Y SLOTS
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarHabilida )
		self.connect( self.pushButtonCancelar,SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#=================================================> METODOS
	def insertarActualizarHabilidad():

		codigo = self.lineEditCodigo.text()
		descripcion = self.lineEditDescripcion.text()

		#AQUI SE INSEGRESA LA HABILIDAD A LA BASE DE DATOS
		if self.nuevo_regsitro:
			#EN CASO DE QUE SE INGRESE UN NUEVO REGISTRO
			pass
		else:
			#EN CASO DE QUE SE ESTE ACTUALIZANDO
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_regsitro:

			self.lineEditDescripcion.setText( "" )

		else:

			self.lineEditCodigo.setText( "" )
			self.lineEditDescripcion.setText( "" )


	def consultar():
		#AQUI SE CONSULTA LA HABILIDAD
		pass



#============================================> LISTAR HABILIDADES <===================================================== 

W_Habilidades_class , W_Habilidades_Base_class = uic.loadUiType('gui/administrador_uis/WidgetListarHabilidades.ui')


class WidgetListarHabilidades( QWidget, W_Habilidades_class ):

	def __init__( self, parent=None ):
		
		#Constrcutro padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )
		

	
#=================================================> CAUSA <=============================================================

D_Causa_class , D_Causa_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogCausa.ui' )

class DialogCausa( QDialog, D_Causa_class ):

	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):


		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#========================================> VARIABLES
		self.controladorCausa = controlador
		self.nuevo_regsitro = nuevo_regsitro

		#========================================> MODIFICACIONES

		if self.nuevo_regsitro:

			self.setWindowTitle( "Nueva Causa" )
			self.lineEditCodigo.setText( "Automatico" )
			self.lineEditCodigo.setReadOnly( True )

		else:

			self.setWindowTitle( "Modiicar Causa" )
			self.lineEditCodigo.setText( "" )
			self.lineEditCodigo.setReadOnly( False )

		#============================================> SENIALES Y SLOTS 
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarCausa )
		self.connect( self.pushButtonCancelar, SIGNAL( "clicked()" ), self.limpiarCampos ) 
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#=================================================> METODOS
	def insertarActualizarCausa( self ):

		codigo = self.lineEditCodigo.text()
		nombre = self.lineEditNombre.text()
		descripcion = self.lineEditDescripcion.text()

		#AQUI SE INGRESAN LOS DATOS A LA BASE DE DATOS
		if self.nuevo_regsitro:
			#EN CASO DE QUE SE INGRESE UN UEVO REGISTRO
			pass

		else:
			#EN CASO DE QUE SE ESTE ACTUALUZANDO
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_regsitro:

			
			self.lineEditNombre.setText( "" )
			self.lineEditDescripcion.setText( "" )

		else:

			self.lineEditCodigo.setText( "" )
			self.lineEditNombre.setText( "" )
			self.lineEditDescripcion.setText( "" )

	

	def consultar( self ):

		#AQUI SE HACE LA CONSULTA DE LA CAUSA
		pass




#=============================================> LISTAR CAUSAS <=========================================================

W_Causas_class , W_Causas_Base_class = uic.loadUiType( 'gui/administrador_uis/WidgetListarCausas.ui' )

class WidgetListarCausas( QWidget, W_Causas_class ):

	def __init__( self, parent=None ):

		
		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )


#=============================================> INFORMES <==============================================================

#=======================================> AGENDA MEDICO MES 

W_AgendaMedicoMes_class , W_AgendaMedicoMes_Base_class = uic.loadUiType("gui/administrador_uis/WidgetAgendaMedico.ui");

class WidgetAgendaMedicoMes( QWidget, W_AgendaMedicoMes_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )


#========================================> HISTORIA CLINICA PACIENTE

W_HistoriaPaciente_class , W_HistoriaPaciente_Base_class = uic.loadUiType("gui/administrador_uis/WidgetHistoriaClinica.ui");

class WidgetHistoriaClinicaPaciente( QWidget, W_HistoriaPaciente_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

#=====================================> CITAS ATENDIDAS MEDICO MES 

W_CitasMedico_class , W_CitasMedico_Base_class = uic.loadUiType("gui/administrador_uis/WidgetNumeroCitasMedico.ui");

class WidgetNumeroCitasMedico( QWidget, W_CitasMedico_class ):

	def __init__( self, parent=None ):

		#Constructor padre 
		QWidget.__init__( self, parent )
		#Confifuracion interfaz
		self.setupUi( self )

#=====================================> COSTO PACIENTE MES ANIO  

W_Costo_Paciente_class , W_Costo_Paciente_Base_class = uic.loadUiType("gui/administrador_uis/WidgetCostoPromedioPaciente.ui");

class WidgetCostoPromedioPaciente( QWidget, W_Costo_Paciente_class ):

	def __init__( self, parent=None ):

		#Constructor padre
		QWidget.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )
