# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fileopen.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import traceback

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from PyQt5.QtCore import QMimeData
from PyQt5.QtGui import QDrag, QFont
from PyQt5.QtWidgets import QTreeWidget, QAbstractItemView, QTreeWidgetItem, QTreeWidgetItemIterator

from ui_Widgets import uni_Widget


class ui_FileWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        self.centralWidget = QtWidgets.QWidget(MainWindow, flags=QtCore.Qt.WindowFlags())
        self.centralWidget.setObjectName("centralWidget")
        MainWindow.setCentralWidget(self.centralWidget)
        self.layouts = QtWidgets.QVBoxLayout()
        self.layouts.setObjectName('layouts')
        self.layouts.setSpacing(0)
        self.layouts.setContentsMargins(0, 0, 0, 0)
        self.tree = FileDragList()
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.tree.setFont(font)
        self.tree.header().hide()
        self.tree.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tree.setDragEnabled(True)
        self.tree.setColumnCount(1)
        self.tree.setColumnWidth(0, 50)
        self.tree.setHeaderLabels([""])
        self.tree.setIconSize(Qt.QSize(25, 25))
        self.tree.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.actionFileOpen = uni_Widget.ICTFEButton(MainWindow)
        self.actionFileOpen.setObjectName("actionFileOpen")
        self.HeaderLayout = QtWidgets.QHBoxLayout()
        self.HeaderLayout.setObjectName('HeaderLayout')
        self.HeaderLayout.addWidget(self.actionFileOpen)
        self.layouts.addWidget(self.actionFileOpen)
        self.layouts.addWidget(self.tree)
        self.centralWidget.setLayout(self.layouts)

        self.reTranslateUi()

    def reTranslateUi(self):
        font = QtGui.QFont()
        font.setFamily('文泉驿等宽微米黑')
        font.setPixelSize(20)
        self.actionFileOpen.setText("打开文件夹")


class FileDragList(QTreeWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUI()

    def initUI(self):
        # init
        self.setSelectionMode(QAbstractItemView.SingleSelection)
        self.setDragEnabled(True)
        self.setStyleSheet("QTreeWidget::item:hover{color: lightgrey; background-color: rgb(60,150,225)}"
                           "QTreeWidget::item:selected{color: lightgrey; background-color:rgb(80,130,255)}"
                           "QTreeWidget{border: 1px solid rgb(50, 50, 50);color: lightgrey; background-color: rgb(30, 30, 30)}")
        self.header().setVisible(False)
        font = QFont()
        font.setFamily('文泉驿微米黑')
        font.setPixelSize(24)
        self.setFont(font)

    def addItem(self, name, categories):
        # can be (icon, text, parent, <int>type)
        try:
            i = self.findItems(categories, QtCore.Qt.MatchStartsWith, column=0)[0]
        except:
            fa = QTreeWidgetItem(self)
            fa.setText(0, categories)
            i = fa
        item = QTreeWidgetItem(i)
        item.setText(0, name)

        item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable |
                      QtCore.Qt.ItemIsDragEnabled)

    def startDrag(self, *args, **kwargs):

        item = self.currentItem()

        mime_data = QMimeData()
        mime_data.setText(item.FilePath)

        drag = QDrag(self)
        drag.setMimeData(mime_data)

        drag.exec_(QtCore.Qt.MoveAction)
