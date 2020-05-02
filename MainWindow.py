# -*- coding: utf-8 -*-

#############################################################
#                                                           #
#              Created By Reverier, XDSEC 2020              #
#                                                           #
#############################################################


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt

from PDFJSPanel.PDFJSPanel import PDFJSPanel
from ui_Widgets import uni_Widget
from DIYPanel.DIYPanel import DIYPanel
from CyberChefPanel.CyberChefPanel import CyberChefPanel
from BrowserPanel.BrowserPanel import BrowserPanel
from WikiPanel.WikiPanel import WikiPanel
from WebPanel.WebPanel import WebPanel
from DataFlowPanel import DataFlowPanel
from KiwixPanel.KiwixPanel import KiwixPanel
import psutil
import time
import traceback


class Ui_MainWindow(object):
    currentDock = None
    def setupUi(self, MainWindow):
        QtGui.QFontDatabase.addApplicationFont("./Resources/wqy-microhei.ttc")
        QtGui.QFontDatabase.addApplicationFont('./Resources/fira-code.ttf')
        self.MainWindow = MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        self.StatusBar = QtWidgets.QStatusBar()
        MainWindow.setStatusBar(self.StatusBar)
        self.StatusBar.setObjectName('StatusBar')
        self.StatusBar.setStyleSheet(
            'QWidget{background-color: transparent;}')
        self.centralWidget = QtWidgets.QWidget(MainWindow, flags=Qt.WindowFlags())
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.MainWindow.setStyleSheet("QMainWindow#MainWindow{\n"
                                      "background-color: rgb(20, 20, 20);\n"
                                      "border: 1px rgb(50, 50, 50);\n"
                                      "border-style: solid;\n"
                                      "}" + uni_Widget.TabStyle)
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.TitleWidget = QtWidgets.QWidget()
        self.TitleWidget.setObjectName('TitleWidget')
        self.TitleWidget.setStyleSheet('#TitleWidget{background-color: rgb(40, 40, 40)}')
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TitleLabel = uni_Widget.ICTFELabel(self.centralWidget)
        self.TitleLabel.setObjectName("TitleLabel")
        font = QtGui.QFont()
        font.setFamily('Fira Code')
        font.setPixelSize(16)
        self.TitleLabel.setFont(font)
        self.TitleLabel.setText('  ICTFE  ')
        self.TitleLabel.setStyleSheet('QLabel{'
                                      'background-color: rgb(130, 50, 235);'
                                      'color: white;'
                                      '}'
                                      "QLabel:hover{"
                                      "background-color: rgba(60, 130, 240, 100%);"
                                      "color: white;"
                                      'border-radius: 16px;'
                                      "}")
        self.horizontalLayout.addWidget(self.TitleLabel, alignment=QtCore.Qt.Alignment())
        '''
        self.TabLayout = QtWidgets.QHBoxLayout()
        self.TabLayout.setContentsMargins(0, 0, 0, 0)
        self.TabLayout.setObjectName("TabLayout")
        self.horizontalLayout.addLayout(self.TabLayout)
        '''
        spacer_item = QtWidgets.QSpacerItem(
            1088, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)

        self.MiniButton = QtWidgets.QPushButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.MiniButton.sizePolicy().hasHeightForWidth())
        self.MiniButton.setSizePolicy(size_policy)
        self.MiniButton.setMinimumSize(QtCore.QSize(54, 32))
        self.MiniButton.setMaximumSize(QtCore.QSize(54, 32))
        self.MiniButton.setBaseSize(QtCore.QSize(120, 45))
        self.MiniButton.setStyleSheet("QPushButton#MiniButton{\n"
                                      "            image:url(./Resources/mini);\n"
                                      "            background-color: transparent;\n"
                                      "            border:none;\n"
                                      "            }\n"
                                      "            QPushButton#MiniButton:hover{\n"
                                      "            image:url(./Resources/mini);\n"
                                      "            background-color: rgb(30, 30, 30);\n"
                                      "            border:none;\n"
                                      "            }\n"
                                      "            QPushButton#MiniButton:pressed{\n"
                                      "            image:url(./Resources/mini);\n"
                                      "            background-color: rgb(50, 50, 50);\n"
                                      "            border:none;\n"
                                      "            }")
        self.MiniButton.setText("")
        self.MiniButton.setFlat(True)
        self.MiniButton.setObjectName("MiniButton")
        self.horizontalLayout.addWidget(self.MiniButton, alignment=QtCore.Qt.Alignment())
        self.MaxButton = QtWidgets.QPushButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.MaxButton.sizePolicy().hasHeightForWidth())
        self.MaxButton.setSizePolicy(size_policy)
        self.MaxButton.setMinimumSize(QtCore.QSize(54, 32))
        self.MaxButton.setMaximumSize(QtCore.QSize(54, 32))
        self.MaxButton.setBaseSize(QtCore.QSize(120, 45))
        self.MaxButton.setStyleSheet("QPushButton#MaxButton{\n"
                                     "            image:url(./Resources/max);\n"
                                     "            border:none;\n"
                                     "            background-color: transparent;\n"
                                     "            }\n"
                                     "            QPushButton#MaxButton:hover{\n"
                                     "            image:url(./Resources/max);\n"
                                     "            background-color: rgb(30, 30, 30);\n"
                                     "            border:none;\n"
                                     "            }\n"
                                     "            QPushButton#MaxButton:pressed{\n"
                                     "            image:url(./Resources/max);\n"
                                     "            background-color: rgb(50, 50, 50);\n"
                                     "            border:none;\n"
                                     "            }")
        self.MaxButton.setText("")
        self.MaxButton.setFlat(True)
        self.MaxButton.setObjectName("MaxButton")
        self.horizontalLayout.addWidget(self.MaxButton, alignment=QtCore.Qt.Alignment())
        self.CloseButton = QtWidgets.QPushButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(size_policy)
        self.CloseButton.setMinimumSize(QtCore.QSize(54, 32))
        self.CloseButton.setMaximumSize(QtCore.QSize(54, 32))
        self.CloseButton.setStyleSheet("QPushButton#CloseButton{\n"
                                       "            image:url(./Resources/close);\n"
                                       "            background-color: transparent;\n"
                                       "            border:none;\n"
                                       "            }\n"
                                       "            QPushButton#CloseButton:hover{\n"
                                       "            image:url(./Resources/close);\n"
                                       "            background-color: rgba(255, 50, 50, 80%);\n"
                                       "            border:none;\n"
                                       "            }\n"
                                       "            QPushButton#CloseButton:pressed{\n"
                                       "            image:url(./Resources/close);\n"
                                       "            background-color: rgba(255, 100, 100, 80%);\n"
                                       "            border:none;\n"
                                       "            }")
        self.CloseButton.setText("")
        self.CloseButton.setFlat(True)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton, alignment=QtCore.Qt.Alignment())
        self.TitleWidget.setLayout(self.horizontalLayout)
        self.verticalLayout.addWidget(self.TitleWidget)
        self.ButtonDock = QtWidgets.QWidget(self.centralWidget)
        self.ButtonDock.setObjectName('ButtonDock')
        self.ButtonDockLayout = QtWidgets.QVBoxLayout(self.ButtonDock)
        self.ButtonDockLayout.setObjectName('ButtonDockLayout')

        self.BinaryButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.BinaryButton.sizePolicy().hasHeightForWidth())
        self.BinaryButton.setSizePolicy(size_policy)
        self.BinaryButton.setObjectName("BinaryButton")
        self.BinaryButton.setMinimumHeight(64)
        self.BinaryButton.setMaximumHeight(64)
        self.BinaryButton.setMinimumWidth(64)
        self.BinaryButton.setMaximumWidth(64)
        self.BinaryButton.setIconSize(QtCore.QSize(48, 48))
        self.BinaryButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/binary.png')))
        self.ButtonDockLayout.addWidget(self.BinaryButton)

        self.WebButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.WebButton.sizePolicy().hasHeightForWidth())
        self.WebButton.setSizePolicy(size_policy)
        self.WebButton.setObjectName("WebButton")
        self.WebButton.setMinimumHeight(64)
        self.WebButton.setMaximumHeight(64)
        self.WebButton.setMinimumWidth(64)
        self.WebButton.setMaximumWidth(64)
        self.WebButton.setIconSize(QtCore.QSize(48, 48))
        self.WebButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/web.png')))
        self.ButtonDockLayout.addWidget(self.WebButton)

        self.DataFlowButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.DataFlowButton.sizePolicy().hasHeightForWidth())
        self.DataFlowButton.setSizePolicy(size_policy)
        self.DataFlowButton.setObjectName("DataFlowButton")
        self.DataFlowButton.setMinimumHeight(64)
        self.DataFlowButton.setMaximumHeight(64)
        self.DataFlowButton.setMinimumWidth(64)
        self.DataFlowButton.setMaximumWidth(64)
        self.DataFlowButton.setIconSize(QtCore.QSize(48, 48))
        self.DataFlowButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/dataflow.png')))
        self.ButtonDockLayout.addWidget(self.DataFlowButton)

        self.ToolsButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.ToolsButton.sizePolicy().hasHeightForWidth())
        self.ToolsButton.setSizePolicy(size_policy)
        self.ToolsButton.setObjectName("ToolsButton")
        self.ToolsButton.setMinimumHeight(64)
        self.ToolsButton.setMaximumHeight(64)
        self.ToolsButton.setMinimumWidth(64)
        self.ToolsButton.setMaximumWidth(64)
        self.ToolsButton.setIconSize(QtCore.QSize(48, 48))
        self.ToolsButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/tools.png')))
        self.ButtonDockLayout.addWidget(self.ToolsButton)

        self.CyberChefButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.CyberChefButton.sizePolicy().hasHeightForWidth())
        self.CyberChefButton.setSizePolicy(size_policy)
        self.CyberChefButton.setObjectName("CyberChefButton")
        self.CyberChefButton.setMinimumHeight(64)
        self.CyberChefButton.setMaximumHeight(64)
        self.CyberChefButton.setMinimumWidth(64)
        self.CyberChefButton.setMaximumWidth(64)
        self.CyberChefButton.setIconSize(QtCore.QSize(48, 48))
        self.CyberChefButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/cyberchef.png')))
        self.ButtonDockLayout.addWidget(self.CyberChefButton)

        self.WikiButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.WikiButton.sizePolicy().hasHeightForWidth())
        self.WikiButton.setSizePolicy(size_policy)
        self.WikiButton.setObjectName("WikiButton")
        self.WikiButton.setMinimumHeight(64)
        self.WikiButton.setMaximumHeight(64)
        self.WikiButton.setMinimumWidth(64)
        self.WikiButton.setMaximumWidth(64)
        self.WikiButton.setIconSize(QtCore.QSize(48, 48))
        self.WikiButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/wiki.png')))
        self.ButtonDockLayout.addWidget(self.WikiButton)

        self.BrowserButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.BrowserButton.sizePolicy().hasHeightForWidth())
        self.BrowserButton.setSizePolicy(size_policy)
        self.BrowserButton.setObjectName("BrowserButton")
        self.BrowserButton.setMinimumHeight(64)
        self.BrowserButton.setMaximumHeight(64)
        self.BrowserButton.setMinimumWidth(64)
        self.BrowserButton.setMaximumWidth(64)
        self.BrowserButton.setIconSize(QtCore.QSize(48, 48))
        self.BrowserButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/browser.png')))
        self.ButtonDockLayout.addWidget(self.BrowserButton)

        self.KiwixButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.KiwixButton.sizePolicy().hasHeightForWidth())
        self.KiwixButton.setSizePolicy(size_policy)
        self.KiwixButton.setObjectName("KiwixButton")
        self.KiwixButton.setMinimumHeight(64)
        self.KiwixButton.setMaximumHeight(64)
        self.KiwixButton.setMinimumWidth(64)
        self.KiwixButton.setMaximumWidth(64)
        self.KiwixButton.setIconSize(QtCore.QSize(48, 48))
        self.KiwixButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/kiwix.png')))
        self.ButtonDockLayout.addWidget(self.KiwixButton)

        self.StartButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.StartButton.sizePolicy().hasHeightForWidth())
        self.StartButton.setSizePolicy(size_policy)
        self.StartButton.setObjectName("StartButton")
        self.StartButton.setMinimumHeight(64)
        self.StartButton.setMaximumHeight(64)
        self.StartButton.setMinimumWidth(64)
        self.StartButton.setMaximumWidth(64)
        self.StartButton.setIconSize(QtCore.QSize(48, 48))
        self.StartButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/start.png')))
        self.ButtonDockLayout.addWidget(self.StartButton)

        self.PDFButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.PDFButton.sizePolicy().hasHeightForWidth())
        self.PDFButton.setSizePolicy(size_policy)
        self.PDFButton.setObjectName("PDFButton")
        self.PDFButton.setMinimumHeight(64)
        self.PDFButton.setMaximumHeight(64)
        self.PDFButton.setMinimumWidth(64)
        self.PDFButton.setMaximumWidth(64)
        self.PDFButton.setIconSize(QtCore.QSize(48, 48))
        self.PDFButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/pdf.png')))
        self.ButtonDockLayout.addWidget(self.PDFButton)

        spacer_item = QtWidgets.QSpacerItem(
            20, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.ButtonDockLayout.addItem(spacer_item)

        self.TempStackButton = uni_Widget.ICTFEButton(self.centralWidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.TempStackButton.sizePolicy().hasHeightForWidth())
        self.TempStackButton.setSizePolicy(size_policy)
        self.TempStackButton.setObjectName("TempStackButton")
        self.TempStackButton.setMinimumHeight(64)
        self.TempStackButton.setMaximumHeight(64)
        self.TempStackButton.setMinimumWidth(64)
        self.TempStackButton.setMaximumWidth(64)
        self.TempStackButton.setIconSize(QtCore.QSize(48, 48))
        self.TempStackButton.setIcon(QtGui.QIcon(QtGui.QPixmap('./Resources/panel/stack.png')))
        self.ButtonDockLayout.addWidget(self.TempStackButton)

        self.TypeStack = QtWidgets.QStackedWidget(self.centralWidget)
        self.TypeStack.setStyleSheet("QWidget#TypeStack{\n"
                                     "background-color: transparent;\n"
                                     "}")
        self.TypeStack.setObjectName("TypeStack")

        self.MainStackWindow = QtWidgets.QMainWindow()
        self.MainStackWindow.setObjectName('MainStackWindow')
        self.MainStackWindow.setDockNestingEnabled(True)
        # self.MainStackWindow.centralContent = QtWidgets.QWidget(self.MainStackWindow)
        self.TypeStack.addWidget(self.MainStackWindow)
        # self.MainStackWindow.setMaximumWidth(0)

        self.MainHLayout = QtWidgets.QHBoxLayout()
        self.MainHLayout.setSpacing(0)
        self.ButtonDockLayout.setSpacing(5)
        self.ButtonDockLayout.setContentsMargins(0, 0, 0, 0)
        self.ButtonDock.setStyleSheet('#ButtonDock{background-color: rgb(30, 30, 30);}')
        self.ButtonDock.setMaximumWidth(64)
        self.MainHLayout.setContentsMargins(0, 0, 0, 0)
        self.MainHLayout.addWidget(self.ButtonDock, alignment=Qt.Alignment())
        self.ButtonDock.setLayout(self.ButtonDockLayout)
        self.MainHLayout.addWidget(self.TypeStack, alignment=Qt.Alignment())
        self.verticalLayout.addLayout(self.MainHLayout)
        MainWindow.setCentralWidget(self.centralWidget)
        self.MaxFlag = False
        # self.reTranslateUi(MainWindow)
        self.MiniButton.clicked.connect(MainWindow.showMinimized)
        self.CloseButton.clicked.connect(self.FormClosing)
        self.MaxButton.clicked.connect(MainWindow.MaximumWindow)

        self.StatusThread = SystemInfoThread(MainWindow)
        self.StatusThread.start()
        self.center()
        self.DataFlowButton.clicked.connect(self.DataFlowPanelCreate)
        self.CyberChefButton.clicked.connect(self.CyberChefCreate)
        self.KiwixButton.clicked.connect(self.KiwixPanelCreate)
        self.PDFButton.clicked.connect(self.PDFJSPanelCreate)
        self.WebButton.clicked.connect(self.WebPanelCreate)
        self.WikiButton.clicked.connect(self.WikiPanelCreate)
        self.StartButton.clicked.connect(self.DIYPanelCreate)
        self.BrowserButton.clicked.connect(self.BrowserPanelCreate)

    def MaximumWindow(self):
        if self.MaxFlag:
            self.MaxFlag = False
            self.MainWindow.showNormal()
        else:
            self.MaxFlag = True
            self.MainWindow.showMaximized()

    def center(self):
        """窗口居中显示"""
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def FormClosing(self):
        self.StatusThread.exit()
        self.MainWindow.close()

    def DataFlowPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "数据流":
                dock.raise_()
                return
        self.MainStackWindow.DataFlowPanelDock = QtWidgets.QDockWidget("数据流")
        self.MainStackWindow.DataFlowPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.DataFlowPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.DataFlowPanel = DataFlowPanel.DataFlowPanel()
        self.MainStackWindow.DataFlowPanelDock.setWidget(self.MainStackWindow.DataFlowPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.DataFlowPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.DataFlowPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.DataFlowPanelDock

    def CyberChefCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "CyberChef":
                dock.raise_()
                return
        self.MainStackWindow.CyberChefDock = QtWidgets.QDockWidget("CyberChef")
        self.MainStackWindow.CyberChefDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.CyberChefDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.CyberChef = CyberChefPanel()
        self.MainStackWindow.CyberChefDock.setWidget(self.MainStackWindow.CyberChef)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.CyberChefDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.CyberChefDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.CyberChefDock

    def KiwixPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "Kiwix":
                dock.raise_()
                return
        self.MainStackWindow.KiwixPanelDock = QtWidgets.QDockWidget("Kiwix")
        self.MainStackWindow.KiwixPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.KiwixPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.KiwixPanel = KiwixPanel()
        self.MainStackWindow.KiwixPanelDock.setWidget(self.MainStackWindow.KiwixPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.KiwixPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.KiwixPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.KiwixPanelDock

    def WebPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "Web":
                dock.raise_()
                return
        self.MainStackWindow.WebPanelDock = QtWidgets.QDockWidget("Web")
        self.MainStackWindow.WebPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.WebPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.WebPanel = WebPanel()
        self.MainStackWindow.WebPanelDock.setWidget(self.MainStackWindow.WebPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.WebPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.WebPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.WebPanelDock

    def WikiPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "Wiki":
                dock.raise_()
                return
        self.MainStackWindow.WikiPanelDock = QtWidgets.QDockWidget("Wiki")
        self.MainStackWindow.WikiPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.WikiPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.WikiPanel = WikiPanel()
        self.MainStackWindow.WikiPanelDock.setWidget(self.MainStackWindow.WikiPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.WikiPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.WikiPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.WikiPanelDock

    def BrowserPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "Browser":
                dock.raise_()
                return
        self.MainStackWindow.BrowserPanelDock = QtWidgets.QDockWidget("Browser")
        self.MainStackWindow.BrowserPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.BrowserPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.BrowserPanel = BrowserPanel()
        self.MainStackWindow.BrowserPanelDock.setWidget(self.MainStackWindow.BrowserPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.BrowserPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.BrowserPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.BrowserPanelDock

    def DIYPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "DIY":
                dock.raise_()
                return
        self.MainStackWindow.DIYPanelDock = QtWidgets.QDockWidget("DIY")
        self.MainStackWindow.DIYPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.DIYPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.DIYPanel = DIYPanel()
        self.MainStackWindow.DIYPanelDock.setWidget(self.MainStackWindow.DIYPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.DIYPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.DIYPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.DIYPanelDock

    def PDFJSPanelCreate(self):
        for dock in self.MainStackWindow.findChildren(QtWidgets.QDockWidget):
            if dock.windowTitle() == "PDFJS":
                dock.raise_()
                return
        self.MainStackWindow.PDFJSPanelDock = QtWidgets.QDockWidget("PDFJS")
        self.MainStackWindow.PDFJSPanelDock.setStyleSheet(uni_Widget.DockStyleSheet)
        self.MainStackWindow.PDFJSPanelDock.setAttribute(Qt.WA_DeleteOnClose)
        self.MainStackWindow.PDFJSPanel = PDFJSPanel()
        self.MainStackWindow.PDFJSPanelDock.setWidget(self.MainStackWindow.PDFJSPanel)
        self.MainStackWindow.addDockWidget(Qt.LeftDockWidgetArea, self.MainStackWindow.PDFJSPanelDock)
        try:
            if self.currentDock != None:
                self.MainStackWindow.tabifyDockWidget(self.currentDock, self.MainStackWindow.PDFJSPanelDock)
        except:
            traceback.print_exc()
        self.currentDock = self.MainStackWindow.PDFJSPanelDock

class SystemInfoThread(QtCore.QThread):

    def __init__(self, window):
        super(SystemInfoThread, self).__init__()
        self.__win = window
        self.__win.StatusBar.setStyleSheet(
            'QStatusBar{background-color: rgb(40, 40, 40);color: white; border: 1px solid rgb(50, 50, 50);}')
        font = QtGui.QFont()
        font.setFamily('Fira Code')
        font.setPixelSize(16)
        self.__win.StatusBar.setFont(font)

    def run(self):
        old_net_speed = psutil.net_io_counters().bytes_recv
        while True:
            new_net_speed = psutil.net_io_counters().bytes_recv
            time.sleep(1)
            self.__win.StatusBar.showMessage(
                '-> ICTFE - Version 1.0.0 Dev Build 28147 | Powered By Reverier       ' +
                "NetSpeed: %.2fK/s" % ((new_net_speed - old_net_speed) / 1024) + '      Memory Usage: ' + str(
                    int(psutil.virtual_memory().used * 100 / psutil.virtual_memory().total)) + '%' +
                '      CPU Usage: ' + str(psutil.cpu_percent()) + '%')
            old_net_speed = new_net_speed
