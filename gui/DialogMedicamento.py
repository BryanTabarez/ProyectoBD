from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

# ===========================================> MEDICAMENTO <============================================================

D_Medicamento_class , D_Medicamento_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogMedicamento.ui' )

class DialogMedicamento( QDialog, D_Medicamento_class ):

	def __init__( self, nuevo_registro=True, controlador=None, parent=None ):

		#Construtor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#=====================================> VARIABLES
		self.controladorMedicamento = controlador
		self.nuevo_registro = nuevo_registro

		#=====================================> MODIFICACIONES

		if self.nuevo_registro:

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
		if self.nuevo_registro:
			#EN CASO DE UN NUEVO REGISTRO
			pass
		else:
			#EN CASO DE UNA ACTUALIZACION
			pass

		self.limpiarCampos()

	def limpiarCampos( self ):

		if self.nuevo_registro:

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

		#========================================> VARIABLES
		self.controladorMedicamento = " " #AQUI VA EL CONTROLADOR DE MEDICAMENTO


	#============================================> METODOS
	def actualizar( self ):
		
		#AQUI SE LISTAN LAS CAMAS EN LA TABLA DE CAMAS
		#self.tableWidgetMedicamentos.clearContents()
		#self.tableWidgetMedicamentos.insertRow( 0 )
		#self.tableWidgetMedicamentos.setItem( 0, 0, QTableWidgetItem( "Codigo" ) )
		#self.tableWidgetMedicamentos.setItem( 0, 1, QTableWidgetItem( "descripcion" ) )
		pass
