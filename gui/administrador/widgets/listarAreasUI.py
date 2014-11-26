# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WidgetListarAreas.ui'
#
# Created: Sun Nov  9 14:47:21 2014
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

class Ui_widgetListarAreas(object):
    def setupUi(self, widgetListarAreas):
        widgetListarAreas.setObjectName(_fromUtf8("widgetListarAreas"))
        widgetListarAreas.resize(571, 481)
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
        widgetListarAreas.setPalette(palette)
        widgetListarAreas.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        widgetListarAreas.setAutoFillBackground(True)
        self.tableWidgetListarAreas = QtGui.QTableWidget(widgetListarAreas)
        self.tableWidgetListarAreas.setGeometry(QtCore.QRect(10, 10, 551, 461))
        self.tableWidgetListarAreas.setObjectName(_fromUtf8("tableWidgetListarAreas"))
        self.tableWidgetListarAreas.setColumnCount(3)
        self.tableWidgetListarAreas.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarAreas.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarAreas.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Ubuntu Condensed"))
        item.setFont(font)
        self.tableWidgetListarAreas.setHorizontalHeaderItem(2, item)

        self.retranslateUi(widgetListarAreas)
        QtCore.QMetaObject.connectSlotsByName(widgetListarAreas)

    def retranslateUi(self, widgetListarAreas):
        widgetListarAreas.setWindowTitle(_translate("widgetListarAreas", "Listar Areas", None))
        item = self.tableWidgetListarAreas.horizontalHeaderItem(0)
        item.setText(_translate("widgetListarAreas", "Codigo", None))
        item = self.tableWidgetListarAreas.horizontalHeaderItem(1)
        item.setText(_translate("widgetListarAreas", "Nombre", None))
        item = self.tableWidgetListarAreas.horizontalHeaderItem(2)
        item.setText(_translate("widgetListarAreas", "Descripcion", None))

