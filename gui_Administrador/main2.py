import sys
from PyQt4 import QtGui, QtCore, uic

WidgetEmpleadoInterfaz_class , WidgetEmpleadoInterfazBase_class = uic.loadUiType('administrador/uis/WidgetEmpleadosPorArea.ui')

class Prueba(QtGui.QMainWindow):

	def __init__( self, parent = None):

		QtGui.QMainWindow.__init__(parent)
#if __name__ == "__main__":
app = QtGui.QApplication( sys.argv )

miWidget = QtGui.QWidget()
miWidget2 = QtGui.QWidget(miWidget)
miWidget3 = QtGui.QWidget(miWidget)
miLabel = QtGui.QLabel(miWidget3)
miLabel.setText("Hola") 
miBoton = QtGui.QPushButton(miWidget2)
miBoton.setText("Cambiar")
miBoton.clicked.connect(funcion)

miWidget.show()
miWidget.show()
r = app.exec_()
print "Fin " + str(r)
sys.exit(r)

def funcion():
	miWidget2.hide()