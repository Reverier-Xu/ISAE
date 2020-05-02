# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileopen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtWidgets import QTreeWidget, QAbstractItemView

from ui_Widgets import uni_Widget


class ui_FileWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralWidget = QtWidgets.QWidget(MainWindow, flags=QtCore.Qt.WindowFlags())
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.layouts = QtWidgets.QVBoxLayout()
        self.layouts.setObjectName('layouts')
        self.layouts.setSpacing(0)
        self.layouts.setContentsMargins(0, 0, 0, 0)
        self.tree = QTreeWidget()
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.tree.setFont(font)
        self.tree.header().hide()
        self.tree.setStyleSheet("QTreeView::item:hover{"
                                "color: lightgrey; "
                                "background-color: rgb(50,50,50)"
                                "}"
                                "QTreeView::item:selected{"
                                "color: lightgrey; "
                                "background-color:rgb(80,110,205)"
                                "}"
                                "QTreeView{"
                                "color: lightgrey; "
                                "background-color: rgb(20, 20, 20); "
                                "border: 1px solid rgb(50, 50, 50);"
                                "}"
                                "QHeaderView::section{"
                                "color: lightgrey; "
                                "background-color: rgb(20, 20, 20);"
                                "}")
        self.tree.setColumnCount(1)
        self.tree.setColumnWidth(0, 50)
        self.tree.setHeaderLabels([""])
        self.tree.setIconSize(Qt.QSize(25, 25))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.actionFileOpen = uni_Widget.ICTFEButton(MainWindow)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.layouts.addWidget(self.actionFileOpen)
        self.layouts.addWidget(self.tree)
        self.centralWidget.setLayout(self.layouts)

        self.reTranslateUi()

    def reTranslateUi(self):
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.actionFileOpen.setText("打开文件夹")
