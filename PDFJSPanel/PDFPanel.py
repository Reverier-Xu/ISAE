# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PDFPanel.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1041, 677)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.FileListDock = QtWidgets.QDockWidget(Form)
        self.FileListDock.setMaximumSize(QtCore.QSize(130, 524287))
        self.FileListDock.setFeatures(
            QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        self.FileListDock.setObjectName("FileListDock")
        self.dockWidgetContents = QtWidgets.QWidget()
        self.dockWidgetContents.setObjectName("dockWidgetContents")
        self.FileListDock.setWidget(self.dockWidgetContents)
        self.horizontalLayout.addWidget(self.FileListDock)
        self.PDFDock = QtWidgets.QDockWidget(Form)
        self.PDFDock.setFeatures(QtWidgets.QDockWidget.DockWidgetFloatable | QtWidgets.QDockWidget.DockWidgetMovable)
        self.PDFDock.setObjectName("PDFDock")
        self.dockWidgetContents_2 = QtWidgets.QWidget()
        self.dockWidgetContents_2.setObjectName("dockWidgetContents_2")
        self.PDFDock.setWidget(self.dockWidgetContents_2)
        self.horizontalLayout.addWidget(self.PDFDock)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
