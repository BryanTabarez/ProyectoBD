from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic
from componentes_administrador import DialogInformacion
# ===========================================> MEDICAMENTO <============================================================

D_Medicamento_class , D_Medicamento_Base_class = uic.loadUiType( 'gui/administrador_uis/DialogMedicamento.ui' )

class DialogMedicamento( QDialog, D_Medicamento_class ):

	def __init__( self, nuevo_registro=1, controlador=None, parent=None ):

		#Construtor padre
		QDialog.__init__( self, parent )
		#Configuracion interfaz
		self.setupUi( self )

		#=====================================> VARIABLES
		self.dialogInformativo = DialogInformacion(self)
		self.controladorMedicamento = controlador
		self.nuevo_registro = nuevo_registro

		#=====================================> MODIFICACIONES

		if self.nuevo_registro is 1:

			self.setWindowTitle( "Nuevo Medicamento" )
			self.lineEditCodigo.setText( "Automatico" )
			self.lineEditCodigo.setReadOnly(True)
			self.pushButtonConsultar.hide()
			self.pushButtonEliminar.hide()

		if self.nuevo_registro is 2:

			self.setWindowTitle( "Actualizar Medicamento" )
			self.lineEditCodigo.setText( "" )
			self.lineEditCodigo.setReadOnly(False)
			self.pushButtonEliminar.hide()

		if self.nuevo_registro is 3:

			self.setWindowTitle( "Eliminar Medicamento" )
			self.lineEditCodigo.setText( "" )
			self.lineEditCodigo.setReadOnly(False)
			self.pushButtonConsultar.show()
			self.pushButtonInsertar.hide()

		#========================================> SENIALES Y SLOTS
		self.connect( self.pushButtonLimpiar, SIGNAL( "clicked()" ), self.limpiarCampos )
		self.connect( self.pushButtonInsertar, SIGNAL( "clicked()" ), self.insertarActualizarMedicamento )
		self.connect( self.pushButtonEliminar, SIGNAL( "clicked()" ), self.EliminarMedicamento )
		self.connect( self.pushButtonConsultar, SIGNAL( "clicked()" ), self.consultar )

	#=============================================> METODOS
	def insertarActualizarMedicamento( self ):

		codigo = str(self.lineEditCodigo.text())
		costo = str(self.lineEditCosto.text())
		nombre = str(self.lineEditNombre.text())
		descripcion = str(self.lineEditDescripcion.text())


		#AQUI SE INGRESA LA INFOMACION EN LA BASE DE DATOS
		if self.nuevo_registro is 1:
			result = self.controladorMedicamento.insertarMedicamento(costo, nombre, descripcion)
			self.dialogInformativo.showMensaje("Ingresar", result)
			
			
		else:
			result = self.controladorMedicamento.actualizarMedicamento(codigo, costo, nombre, descripcion)
			self.dialogInformativo.showMensaje("Modificar", result)
		

	def limpiarCampos( self ):

		if self.nuevo_registro is 1:

			self.lineEditNombre.setText("")
			self.lineEditCosto.setText("")
			self.lineEditDescripcion.setText("")

		else:

			self.lineEditCodigo.setText("")
			self.lineEditNombre.setText("")
			self.lineEditCosto.setText("")
			self.lineEditDescripcion.setText("")

	
	def consultar( self ):
		nombre = str(self.lineEditNombre.text())
		medicamento = self.controladorMedicamento.buscarMedicamento(nombre)
		self.lineEditCodigo.setText(str(medicamento.get_codigo()))
		self.lineEditCosto.setText(medicamento.get_costo())
		self.lineEditDescripcion.setText(medicamento.get_descripcion())

	def EliminarMedicamento( self ):
		codigo = str(self.lineEditCodigo.text())
		result = self.controladorMedicamento.eliminarMedicamento(codigo)
		self.dialogInformativo.showMensaje("Eliminar", result)




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
