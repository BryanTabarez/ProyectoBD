import sys
from PyQt4.QtGui import *
from  iniciarSesionFuncionalUI import InterfazIniciarSesion

if __name__ == "__main__":
	app = QApplication( sys.argv )
	iniciarSesion = InterfazIniciarSesion()
	iniciarSesion.show()
	r = app.exec_()
	print "Fin " + str(r)
	sys.exit(r)

