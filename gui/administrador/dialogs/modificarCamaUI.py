# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'DialogModificarCama.ui'
#
# Created: Sun Nov  9 14:53:28 2014
#      by: PyQt4 UI code generator 4.11.2
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_dialogModificarCama(object):
    def setupUi(self, dialogModificarCama):
        dialogModificarCama.setObjectName(_fromUtf8("dialogModificarCama"))
        dialogModificarCama.resize(800, 330)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        dialogModificarCama.setPalette(palette)
        dialogModificarCama.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        dialogModificarCama.setAutoFillBackground(True)
        self.widgetCabecera = QtGui.QWidget(dialogModificarCama)
        self.widgetCabecera.setGeometry(QtCore.QRect(0, 0, 800, 65))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 77, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 77, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(159, 158, 158))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 77, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(57, 77, 76))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.widgetCabecera.setPalette(palette)
        self.widgetCabecera.setAutoFillBackground(True)
        self.widgetCabecera.setObjectName(_fromUtf8("widgetCabecera"))
        self.layoutWidget_4 = QtGui.QWidget(self.widgetCabecera)
        self.layoutWidget_4.setGeometry(QtCore.QRect(20, 0, 162, 63))
        self.layoutWidget_4.setObjectName(_fromUtf8("layoutWidget_4"))
        self.formLayout_5 = QtGui.QFormLayout(self.layoutWidget_4)
        self.formLayout_5.setMargin(0)
        self.formLayout_5.setObjectName(_fromUtf8("formLayout_5"))
        self.labelColMedica = QtGui.QLabel(self.layoutWidget_4)
        self.labelColMedica.setStyleSheet(_fromUtf8("font: 30pt \"Ubuntu Condensed\";\n"
"color: rgb(255, 255, 255);"))
        self.labelColMedica.setObjectName(_fromUtf8("labelColMedica"))
        self.formLayout_5.setWidget(0, QtGui.QFormLayout.LabelRole, self.labelColMedica)
        self.labelClinicManager = QtGui.QLabel(self.layoutWidget_4)
        self.labelClinicManager.setObjectName(_fromUtf8("labelClinicManager"))
        self.formLayout_5.setWidget(1, QtGui.QFormLayout.LabelRole, self.labelClinicManager)
        self.widgetCuerpo = QtGui.QWidget(dialogModificarCama)
        self.widgetCuerpo.setGeometry(QtCore.QRect(10, 70, 781, 251))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setBold(True)
        font.setWeight(75)
        self.widgetCuerpo.setFont(font)
        self.widgetCuerpo.setAutoFillBackground(True)
        self.widgetCuerpo.setObjectName(_fromUtf8("widgetCuerpo"))
        self.layoutWidget_2 = QtGui.QWidget(self.widgetCuerpo)
        self.layoutWidget_2.setGeometry(QtCore.QRect(10, 10, 761, 110))
        self.layoutWidget_2.setObjectName(_fromUtf8("layoutWidget_2"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget_2)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.labelNumerDeCama = QtGui.QLabel(self.layoutWidget_2)
        self.labelNumerDeCama.setObjectName(_fromUtf8("labelNumerDeCama"))
        self.gridLayout.addWidget(self.labelNumerDeCama, 1, 0, 1, 1)
        self.comboBoxCodigoArea = QtGui.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBoxCodigoArea.setFont(font)
        self.comboBoxCodigoArea.setObjectName(_fromUtf8("comboBoxCodigoArea"))
        self.gridLayout.addWidget(self.comboBoxCodigoArea, 0, 2, 1, 1)
        self.lineEditDescripcion = QtGui.QLineEdit(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEditDescripcion.setFont(font)
        self.lineEditDescripcion.setObjectName(_fromUtf8("lineEditDescripcion"))
        self.gridLayout.addWidget(self.lineEditDescripcion, 2, 2, 1, 1)
        self.labelCodigoArea = QtGui.QLabel(self.layoutWidget_2)
        self.labelCodigoArea.setObjectName(_fromUtf8("labelCodigoArea"))
        self.gridLayout.addWidget(self.labelCodigoArea, 0, 0, 1, 1)
        self.labelDescripcion = QtGui.QLabel(self.layoutWidget_2)
        self.labelDescripcion.setObjectName(_fromUtf8("labelDescripcion"))
        self.gridLayout.addWidget(self.labelDescripcion, 2, 0, 1, 1)
        self.comboBoxNumeroDeCama = QtGui.QComboBox(self.layoutWidget_2)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBoxNumeroDeCama.setFont(font)
        self.comboBoxNumeroDeCama.setObjectName(_fromUtf8("comboBoxNumeroDeCama"))
        self.gridLayout.addWidget(self.comboBoxNumeroDeCama, 1, 2, 1, 1)
        self.layoutWidget = QtGui.QWidget(self.widgetCuerpo)
        self.layoutWidget.setGeometry(QtCore.QRect(410, 210, 361, 29))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.pushButtonEliminar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonEliminar.setObjectName(_fromUtf8("pushButtonEliminar"))
        self.horizontalLayout.addWidget(self.pushButtonEliminar)
        self.pushButtonActualizar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonActualizar.setObjectName(_fromUtf8("pushButtonActualizar"))
        self.horizontalLayout.addWidget(self.pushButtonActualizar)
        self.pushButtonCancelar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonCancelar.setObjectName(_fromUtf8("pushButtonCancelar"))
        self.horizontalLayout.addWidget(self.pushButtonCancelar)
        self.pushButtonAceptar = QtGui.QPushButton(self.layoutWidget)
        self.pushButtonAceptar.setObjectName(_fromUtf8("pushButtonAceptar"))
        self.horizontalLayout.addWidget(self.pushButtonAceptar)

        self.retranslateUi(dialogModificarCama)
        QtCore.QMetaObject.connectSlotsByName(dialogModificarCama)

    def retranslateUi(self, dialogModificarCama):
        dialogModificarCama.setWindowTitle(_translate("dialogModificarCama", "Modificar cama", None))
        self.labelColMedica.setText(_translate("dialogModificarCama", "ColMedica", None))
        self.labelClinicManager.setText(_translate("dialogModificarCama", "Clinic Manager", None))
        self.labelNumerDeCama.setText(_translate("dialogModificarCama", "Numero de cama", None))
        self.labelCodigoArea.setText(_translate("dialogModificarCama", "Codigo area", None))
        self.labelDescripcion.setText(_translate("dialogModificarCama", "Descripcion", None))
        self.pushButtonEliminar.setText(_translate("dialogModificarCama", "Eliminar", None))
        self.pushButtonActualizar.setText(_translate("dialogModificarCama", "Actualizar", None))
        self.pushButtonCancelar.setText(_translate("dialogModificarCama", "Cancelar", None))
        self.pushButtonAceptar.setText(_translate("dialogModificarCama", "Aceptar", None))

