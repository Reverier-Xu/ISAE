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
        self.centralWidget = QtWidgets.QWidget(MainWindow, flags=QtCore.Qt.WindowFlags())
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menubar = QtWidgets.QToolBar(self)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.addToolBar(self.menubar)
        self.actionFileOpen = QtWidgets.QAction(MainWindow)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.menuFile.addAction(self.actionFileOpen)
        self.menubar.addAction(self.menuFile.menuAction())

        self.reTranslateUi()

    def reTranslateUi(self):
        self.menuFile.setTitle("打开")
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.menubar.setFont(font)
        self.menubar.setStyleSheet('color: white; background-color: rgb(20, 20, 20)')
        self.actionFileOpen.setText("打开文件夹")
