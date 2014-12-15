import sys
from PyQt4.QtGui import *
# from gui.login import InterfazIniciarSesion
from gui.login import *

if __name__ == "__main__":
	app = QApplication( sys.argv )
	iniciarSesion = InterfazIniciarSesion()
	iniciarSesion.show()
	r = app.exec_()
	print "Fin " + str(r)
	sys.exit(r)
