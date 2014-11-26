# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListarMedicamentos.ui'
#
# Created: Sun Nov  9 16:26:26 2014
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

class Ui_widgetListarMedicamentos(object):
    def setupUi(self, widgetListarMedicamentos):
        widgetListarMedicamentos.setObjectName(_fromUtf8("widgetListarMedicamentos"))
        widgetListarMedicamentos.resize(571, 481)
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
        widgetListarMedicamentos.setPalette(palette)
        widgetListarMedicamentos.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        widgetListarMedicamentos.setAutoFillBackground(True)
        self.tableWidget = QtGui.QTableWidget(widgetListarMedicamentos)
        self.tableWidget.setGeometry(QtCore.QRect(10, 10, 551, 461))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)

        self.retranslateUi(widgetListarMedicamentos)
        QtCore.QMetaObject.connectSlotsByName(widgetListarMedicamentos)

    def retranslateUi(self, widgetListarMedicamentos):
        widgetListarMedicamentos.setWindowTitle(_translate("widgetListarMedicamentos", "Listar Medicamentos", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("widgetListarMedicamentos", "Codigo", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("widgetListarMedicamentos", "Nombre", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("widgetListarMedicamentos", "Costo", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("widgetListarMedicamentos", "Descripcion", None))

