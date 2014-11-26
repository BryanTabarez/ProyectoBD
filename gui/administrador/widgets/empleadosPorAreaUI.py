# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetEmpleadosPorArea.ui'
#
# Created: Sun Nov  9 12:52:39 2014
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

class Ui_widgetEmpleadosPorArea(object):
    def setupUi(self, widgetEmpleadosPorArea):
        widgetEmpleadosPorArea.setObjectName(_fromUtf8("widgetEmpleadosPorArea"))
        widgetEmpleadosPorArea.resize(571, 481)
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
        widgetEmpleadosPorArea.setPalette(palette)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        font.setBold(True)
        font.setWeight(75)
        widgetEmpleadosPorArea.setFont(font)
        widgetEmpleadosPorArea.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        widgetEmpleadosPorArea.setAutoFillBackground(True)
        self.tableWidgetEmpleados = QtGui.QTableWidget(widgetEmpleadosPorArea)
        self.tableWidgetEmpleados.setGeometry(QtCore.QRect(10, 90, 551, 351))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tableWidgetEmpleados.setFont(font)
        self.tableWidgetEmpleados.setObjectName(_fromUtf8("tableWidgetEmpleados"))
        self.tableWidgetEmpleados.setColumnCount(5)
        self.tableWidgetEmpleados.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidgetEmpleados.setHorizontalHeaderItem(4, item)
        self.labelArea = QtGui.QLabel(widgetEmpleadosPorArea)
        self.labelArea.setGeometry(QtCore.QRect(10, 10, 117, 25))
        self.labelArea.setObjectName(_fromUtf8("labelArea"))
        self.comboBox = QtGui.QComboBox(widgetEmpleadosPorArea)
        self.comboBox.setGeometry(QtCore.QRect(10, 50, 541, 25))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.lineArea = QtGui.QFrame(widgetEmpleadosPorArea)
        self.lineArea.setGeometry(QtCore.QRect(10, 30, 551, 16))
        self.lineArea.setFrameShape(QtGui.QFrame.HLine)
        self.lineArea.setFrameShadow(QtGui.QFrame.Sunken)
        self.lineArea.setObjectName(_fromUtf8("lineArea"))

        self.retranslateUi(widgetEmpleadosPorArea)
        QtCore.QMetaObject.connectSlotsByName(widgetEmpleadosPorArea)

    def retranslateUi(self, widgetEmpleadosPorArea):
        widgetEmpleadosPorArea.setWindowTitle(_translate("widgetEmpleadosPorArea", "Empleados Por Area", None))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(0)
        item.setText(_translate("widgetEmpleadosPorArea", "Identificacion", None))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(1)
        item.setText(_translate("widgetEmpleadosPorArea", "Nombre", None))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(2)
        item.setText(_translate("widgetEmpleadosPorArea", "Cargo", None))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(3)
        item.setText(_translate("widgetEmpleadosPorArea", "Salario", None))
        item = self.tableWidgetEmpleados.horizontalHeaderItem(4)
        item.setText(_translate("widgetEmpleadosPorArea", "Jefe", None))
        self.labelArea.setText(_translate("widgetEmpleadosPorArea", "Area", None))

