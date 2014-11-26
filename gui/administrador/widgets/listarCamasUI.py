# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListarCamas.ui'
#
# Created: Sun Nov  9 15:40:52 2014
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

class Ui_widgetListarCamas(object):
    def setupUi(self, widgetListarCamas):
        widgetListarCamas.setObjectName(_fromUtf8("widgetListarCamas"))
        widgetListarCamas.resize(571, 481)
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
        widgetListarCamas.setPalette(palette)
        widgetListarCamas.setAutoFillBackground(True)
        self.tableWidgetListarCamas = QtGui.QTableWidget(widgetListarCamas)
        self.tableWidgetListarCamas.setGeometry(QtCore.QRect(10, 10, 551, 461))
        self.tableWidgetListarCamas.setObjectName(_fromUtf8("tableWidgetListarCamas"))
        self.tableWidgetListarCamas.setColumnCount(4)
        self.tableWidgetListarCamas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarCamas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarCamas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarCamas.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarCamas.setHorizontalHeaderItem(3, item)

        self.retranslateUi(widgetListarCamas)
        QtCore.QMetaObject.connectSlotsByName(widgetListarCamas)

    def retranslateUi(self, widgetListarCamas):
        widgetListarCamas.setWindowTitle(_translate("widgetListarCamas", "Listar Camas", None))
        item = self.tableWidgetListarCamas.horizontalHeaderItem(0)
        item.setText(_translate("widgetListarCamas", "Codigo Area", None))
        item = self.tableWidgetListarCamas.horizontalHeaderItem(1)
        item.setText(_translate("widgetListarCamas", "Numero Cama", None))
        item = self.tableWidgetListarCamas.horizontalHeaderItem(2)
        item.setText(_translate("widgetListarCamas", "Codigo Area", None))
        item = self.tableWidgetListarCamas.horizontalHeaderItem(3)
        item.setText(_translate("widgetListarCamas", "descripcion", None))

