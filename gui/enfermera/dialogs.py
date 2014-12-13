from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import uic

DialogAgendarCitaInterfaz_clas, DialogAgendarCitaInterfazBase = uic.loadUiType('/enfermera/uis/DialogAgendarCita.ui')

class DialogAgendarCita( QDialog, DialogAgendarCita ):
	
	def __init__( self, parent=None ):
		
		
