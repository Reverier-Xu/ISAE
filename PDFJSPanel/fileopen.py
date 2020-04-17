# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileopen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class ui_PDFFileWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QToolBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.addToolBar(self.menubar)
        self.actionfileopen = QtWidgets.QAction(MainWindow)
        self.actionfileopen.setObjectName("actionfileopen")
        self.menufile.addAction(self.actionfileopen)
        self.menubar.addAction(self.menufile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.menufile.setTitle(_translate("MainWindow", "打开"))
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet('color: white; background-color: rgb(30, 30, 30)')
        self.actionfileopen.setText(_translate("MainWindow", "打开文件夹"))
