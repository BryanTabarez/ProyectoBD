from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

#===========================================> HABILIDAD <===============================================================

D_Habilidad_class , D_Habilidad_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogHabilidad.ui' )

class DialogHabilidad( QDialog, D_Habilidad_class ):

	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):

		#Constructor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )
		
		#=========================================> VARIABLES
		self.controladorHabilidad = controlador
		self.nuevo_registro = nuevo_registro

		#=========================================> MODIFICACIONES

		if self.nuevo_registro:

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
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarHabilidad )
		self.connect( self.pushButtonCancelar,SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#=================================================> METODOS
	def insertarActualizarHabilidad( self ):

		codigo = self.lineEditCodigo.text()
		descripcion = self.lineEditDescripcion.text()

		#AQUI SE INSEGRESA LA HABILIDAD A LA BASE DE DATOS
		if self.nuevo_registro:
			#EN CASO DE QUE SE INGRESE UN NUEVO REGISTRO
			pass
		else:
			#EN CASO DE QUE SE ESTE ACTUALIZANDO
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_registro:

			self.lineEditDescripcion.setText( "" )

		else:

			self.lineEditCodigo.setText( "" )
			self.lineEditDescripcion.setText( "" )


	def consultar( self ):
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

		#========================================> VARIABLES
		self.controladorMedicamento = " " #AQUI VA EL CONTROLADOR DE HABILIDADES


	#============================================> METODOS
	def actualizar( self ):
		
		#AQUI SE LISTAN LAS HABILIDADES EN LA TABLA DE HABILIDADES_ENFERMERA DE LA BASE DE DATOS
		#self.tableWidgetHabilidades.clearContents()
		#self.tableWidgetHabilidades.insertRow( 0 )
		#self.tableWidgetHabilidades.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetHabilidades.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass
		

	
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
		self.nuevo_registro = nuevo_registro

		#========================================> MODIFICACIONES

		if self.nuevo_registro:

			self.setWindowTitle( "Nueva Causa" )
			self.lineEditCodigo.setText( "Automatico" )
			self.lineEditCodigo.setReadOnly( True )
			self.pushButtonConsultar.hide()

		else:

			self.setWindowTitle( "Modiicar Causa" )
			self.lineEditCodigo.setText( "" )
			self.lineEditCodigo.setReadOnly( False )
			self.pushButtonConsultar.show()

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
		if self.nuevo_registro:
			#EN CASO DE QUE SE INGRESE UN UEVO REGISTRO
			pass

		else:
			#EN CASO DE QUE SE ESTE ACTUALUZANDO
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_registro:

			
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

		#========================================> VARIABLES
		self.controladorCausa = " " #AQUI VA EL CONTROLADOR DE CAUSA


	#============================================> METODOS
	def actualizar( self ):
		
		#AQUI SE LISTAN LAS CAUSAS DE LA BASE DE DATOS
		#self.tableWidgetListarCausas.clearContents()
		#self.tableWidgetListarCausas.insertRow( 0 )
		#self.tableWidgetListarCausas.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetListarCausas.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass

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

		if self.nuevo_registro:

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
		if self.nuevo_registro:
			#EN CASO DE SE UN NUEVO REGISTRO
			pass

		else:
			#EN CASO DE SER UNA ACTUALIZACION
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_registro:
			
			self.lineEditNumeroDeCama.setText( "" )
			self.lineEditDescripcion.setText( "" )

		else:

			self.lineEditCodigoArea.setText( "" )
			self.lineEditNumeroDeCama.setText( "" )
			self.lineEditDescripcion.setText( "" )

	def consultar( self ):

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

		#========================================> VARIABLES
		self.controladorCama = " " #AQUI VA EL CONTROLADOR DE CAMA


	#============================================> METODOS
	def actualizar( self ):
		#area_seleccionada = self.comboBoxAreaCamas.currentText()
		#AQUI SE LISTAN LAS CAMAS EN LA TABLA DE CAMAS
		#self.tableWidgetCamas.clearContents()
		#self.tableWidgetCamas.insertRow( 0 )
		#self.tableWidgetCamas.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetCamas.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass
			
