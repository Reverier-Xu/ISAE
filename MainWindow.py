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
from TerminalPanel.TerminalPanel import TerminalPanel
from BrowserPanel.BrowserPanel import BrowserPanel
from WikiPanel.WikiPanel import WikiPanel
from DataFlowPanel import DataFlowPanel
from kiwix.KiwixPanel import KiwixPanel
import psutil
import time


class Ui_MainWindow(object):
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
        self.centralwidget = QtWidgets.QWidget(MainWindow, flags=Qt.WindowFlags())
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.MainWindow.setStyleSheet("QMainWindow#MainWindow{\n"
                                      "background-color: rgb(30, 30, 30);\n"
                                      "border: 1px rgb(50, 50, 50);\n"
                                      "border-style: solid;\n"
                                      "}")
        self.centralwidget.setObjectName("centralWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.TitleLabel = uni_Widget.ICTFELabel(self.centralwidget)
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
        self.TabLayout = QtWidgets.QHBoxLayout()
        self.TabLayout.setContentsMargins(0, 0, 0, 0)
        self.TabLayout.setObjectName("TabLayout")
        self.horizontalLayout.addLayout(self.TabLayout)
        spacer_item = QtWidgets.QSpacerItem(
            1088, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacer_item)

        self.MiniButton = QtWidgets.QPushButton(self.centralwidget)
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
                                      "            border:none;\n"
                                      "            }\n"
                                      "            QPushButton#MiniButton:hover{\n"
                                      "            image:url(./Resources/mini1);\n"
                                      "            border:none;\n"
                                      "            }\n"
                                      "            QPushButton#MiniButton:pressed{\n"
                                      "            image:url(./Resources/mini2);\n"
                                      "            border:none;\n"
                                      "            }")
        self.MiniButton.setText("")
        self.MiniButton.setFlat(True)
        self.MiniButton.setObjectName("MiniButton")
        self.horizontalLayout.addWidget(self.MiniButton, alignment=QtCore.Qt.Alignment())
        self.MaxButton = QtWidgets.QPushButton(self.centralwidget)
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
                                     "            }\n"
                                     "            QPushButton#MaxButton:hover{\n"
                                     "            image:url(./Resources/max1);\n"
                                     "            border:none;\n"
                                     "            }\n"
                                     "            QPushButton#MaxButton:pressed{\n"
                                     "            image:url(./Resources/max2);\n"
                                     "            border:none;\n"
                                     "            }")
        self.MaxButton.setText("")
        self.MaxButton.setFlat(True)
        self.MaxButton.setObjectName("MaxButton")
        self.horizontalLayout.addWidget(self.MaxButton, alignment=QtCore.Qt.Alignment())
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
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
                                       "            border:none;\n"
                                       "            }\n"
                                       "            QPushButton#CloseButton:hover{\n"
                                       "            image:url(./Resources/close1);\n"
                                       "            border:none;\n"
                                       "            }\n"
                                       "            QPushButton#CloseButton:pressed{\n"
                                       "            image:url(./Resources/close2);\n"
                                       "            border:none;\n"
                                       "            }")
        self.CloseButton.setText("")
        self.CloseButton.setFlat(True)
        self.CloseButton.setObjectName("CloseButton")
        self.horizontalLayout.addWidget(self.CloseButton, alignment=QtCore.Qt.Alignment())
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ReverseButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.ReverseButton.sizePolicy().hasHeightForWidth())
        self.ReverseButton.setSizePolicy(size_policy)
        self.ReverseButton.setObjectName("ReverseButton")
        self.ReverseButton.setMaximumHeight(32)

        self.TabLayout.setSpacing(0)

        self.TabLayout.addWidget(self.ReverseButton, alignment=QtCore.Qt.Alignment())
        self.WebButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.WebButton.sizePolicy().hasHeightForWidth())
        self.WebButton.setSizePolicy(size_policy)
        self.WebButton.setObjectName("WebButton")
        self.WebButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.WebButton, alignment=QtCore.Qt.Alignment())
        self.CryptoButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.CryptoButton.sizePolicy().hasHeightForWidth())
        self.CryptoButton.setSizePolicy(size_policy)
        self.CryptoButton.setObjectName("CryptoButton")
        self.CryptoButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.CryptoButton, alignment=QtCore.Qt.Alignment())
        self.MiscButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.MiscButton.sizePolicy().hasHeightForWidth())
        self.MiscButton.setSizePolicy(size_policy)
        self.MiscButton.setObjectName("MiscButton")
        self.MiscButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.MiscButton, alignment=QtCore.Qt.Alignment())
        self.TerminalButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.TerminalButton.sizePolicy().hasHeightForWidth())
        self.TerminalButton.setSizePolicy(size_policy)
        self.TerminalButton.setObjectName("TerminalButton")
        self.TerminalButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.TerminalButton, alignment=QtCore.Qt.Alignment())
        self.WikiButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.WikiButton.sizePolicy().hasHeightForWidth())
        self.WikiButton.setSizePolicy(size_policy)
        self.WikiButton.setMaximumHeight(32)
        self.WikiButton.setObjectName("WikiButton")
        self.TabLayout.addWidget(self.WikiButton, alignment=QtCore.Qt.Alignment())
        self.BrowserButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.BrowserButton.sizePolicy().hasHeightForWidth())
        self.BrowserButton.setSizePolicy(size_policy)
        self.BrowserButton.setObjectName("BrowserButton")
        self.BrowserButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.BrowserButton, alignment=QtCore.Qt.Alignment())
        self.KiwixButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.KiwixButton.sizePolicy().hasHeightForWidth())
        self.KiwixButton.setSizePolicy(size_policy)
        self.KiwixButton.setObjectName("KiwixButton")
        self.KiwixButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.KiwixButton, alignment=QtCore.Qt.Alignment())
        self.DIYButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.DIYButton.sizePolicy().hasHeightForWidth())
        self.DIYButton.setSizePolicy(size_policy)
        self.DIYButton.setObjectName("DIYButton")
        self.DIYButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.DIYButton, alignment=QtCore.Qt.Alignment())
        self.PDFJSButton = uni_Widget.ICTFEButton(self.centralwidget)
        size_policy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        size_policy.setHorizontalStretch(0)
        size_policy.setVerticalStretch(0)
        size_policy.setHeightForWidth(
            self.PDFJSButton.sizePolicy().hasHeightForWidth())
        self.PDFJSButton.setSizePolicy(size_policy)
        self.PDFJSButton.setMaximumHeight(32)
        self.PDFJSButton.setObjectName("PDFJSButton")
        self.TabLayout.addWidget(self.PDFJSButton, alignment=QtCore.Qt.Alignment())

        self.TypeStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.TypeStack.setMinimumSize(QtCore.QSize(1000, 600))
        self.TypeStack.setStyleSheet("QWidget#TypeStack{\n"
                                     "background-color: transparent;\n"
                                     "}")
        self.TypeStack.setObjectName("TypeStack")

        # Reverse Panel
        self.BinaryPanel = QtWidgets.QWidget(None, flags=Qt.WindowFlags())
        self.BinaryPanel.setObjectName("BinaryPanel")
        self.TypeStack.addWidget(self.BinaryPanel)

        # Web Panel
        self.WebPanel = QtWidgets.QWidget(None, flags=Qt.WindowFlags())
        self.WebPanel.setObjectName("WebPanel")
        self.TypeStack.addWidget(self.WebPanel)

        # Crypto Panel
        self.CryptoPanel = DataFlowPanel.DataFlowPanel()
        self.CryptoPanel.setObjectName("DataFlowPanel")
        self.TypeStack.addWidget(self.CryptoPanel)

        # Misc Panel
        self.MiscPanel = QtWidgets.QWidget(None, flags=Qt.WindowFlags())
        self.MiscPanel.setObjectName("MiscPanel")
        self.TypeStack.addWidget(self.MiscPanel)

        # DIY Panel
        self.DIYPanel = DIYPanel()
        self.DIYPanel.setObjectName('DIYPanel')
        self.TypeStack.addWidget(self.DIYPanel)

        # PDFJS Panel
        self.PDFJSPanel = PDFJSPanel()
        self.PDFJSPanel.setObjectName('PDFJSPanel')
        self.TypeStack.addWidget(self.PDFJSPanel)

        # Terminal Panel
        self.TerminalPanel = TerminalPanel()
        self.TerminalPanel.setObjectName('TerminalPanel')
        self.TypeStack.addWidget(self.TerminalPanel)

        # Browser Panel
        self.BrowserPanel = BrowserPanel()
        self.BrowserPanel.setObjectName('BrowserPanel')
        self.TypeStack.addWidget(self.BrowserPanel)

        # Wiki Panel
        self.WikiPanel = WikiPanel()
        self.WikiPanel.setObjectName('WikiPanel')
        self.TypeStack.addWidget(self.WikiPanel)

        # Wiki Panel
        self.KiwixPanel = KiwixPanel()
        self.KiwixPanel.setObjectName('KiwixPanel')
        self.TypeStack.addWidget(self.KiwixPanel)

        # Welcome Panel
        self.WelcomeLabel = QtWidgets.QLabel()
        self.WelcomeLabel.setObjectName('WelcomeLabel')
        self.WelcomeLabel.setAlignment(Qt.AlignVCenter | Qt.AlignCenter)
        pixmap = QtGui.QPixmap("./Resources/welcome.png")  # 按指定路径找到图片
        self.WelcomeLabel.setPixmap(pixmap)  # 在label上显示图片
        self.TypeStack.addWidget(self.WelcomeLabel)

        self.SplitterWidget1 = QtWidgets.QWidget(self, flags=Qt.WindowFlags())
        self.SplitterWidget1.setMaximumHeight(3)
        self.SplitterWidget1.setMinimumHeight(3)
        self.SplitterWidget1.setStyleSheet("QWidget{\n"
                                           "background-color: rgb(130, 50, 235);\n"
                                           "border: 2px rgb(130, 50, 235);\n"
                                           "border-style: solid;\n"
                                           "}")
        self.verticalLayout.addWidget(self.SplitterWidget1, alignment=Qt.Alignment())
        self.styleGetter = 0

        self.verticalLayout.addWidget(self.TypeStack, alignment=Qt.Alignment())
        MainWindow.setCentralWidget(self.centralwidget)
        self.MaxFlag = False

        self.reTranslateUi(MainWindow)
        self.MiniButton.clicked.connect(MainWindow.showMinimized)
        self.CloseButton.clicked.connect(self.FormClosing)
        self.MaxButton.clicked.connect(MainWindow.MaximumWindow)
        self.CryptoButton.clicked.connect(self.ChangeTypeStackCrypto)
        self.ReverseButton.clicked.connect(self.ChangeTypeStackReverse)
        self.MiscButton.clicked.connect(self.ChangeTypeStackMisc)
        self.WebButton.clicked.connect(self.ChangeTypeStackWeb)
        self.DIYButton.clicked.connect(self.ChangeTypeStackDIY)
        self.PDFJSButton.clicked.connect(self.ChangeTypeStackPDFJS)
        self.BrowserButton.clicked.connect(self.ChangeTypeStackBrowser)
        self.WikiButton.clicked.connect(self.ChangeTypeStackWiki)
        self.KiwixButton.clicked.connect(self.ChangeTypeStackKiwix)
        self.TerminalButton.clicked.connect(self.ChangeTypeStackTerminal)
        self.StatusThread = SystemInfoThread(MainWindow)
        self.StatusThread.start()
        self.center()

    def MaximumWindow(self):
        if self.MaxFlag:
            self.MaxFlag = False
            self.MainWindow.showNormal()
        else:
            self.MaxFlag = True
            self.MainWindow.showMaximized()

    def setTabButtonColor(self, button):
        self.CryptoButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.ReverseButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.MiscButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.WebButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.DIYButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.PDFJSButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.BrowserButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.WikiButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.TerminalButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        self.KiwixButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
        button.setStyleSheet(uni_Widget.ButtonStyles[self.styleGetter])
        self.SplitterWidget1.setStyleSheet(
            uni_Widget.SplitterStyles[self.styleGetter])
        self.styleGetter += 1
        self.styleGetter %= 4

    def ChangeTypeStackCrypto(self):
        """改变类型控件组 密码学"""
        self.TypeStack.setCurrentWidget(self.CryptoPanel)
        self.setTabButtonColor(self.CryptoButton)

    def ChangeTypeStackReverse(self):
        """改变类型控件组 逆向"""
        self.TypeStack.setCurrentWidget(self.BinaryPanel)
        self.setTabButtonColor(self.ReverseButton)

    def ChangeTypeStackWeb(self):
        """改变类型控件组 web"""
        self.TypeStack.setCurrentWidget(self.WebPanel)
        self.setTabButtonColor(self.WebButton)

    def ChangeTypeStackMisc(self):
        """改变类型控件组 杂项"""
        self.TypeStack.setCurrentWidget(self.MiscPanel)
        self.setTabButtonColor(self.MiscButton)

    def ChangeTypeStackDIY(self):
        """改变类型控件组 DIY"""
        self.TypeStack.setCurrentWidget(self.DIYPanel)
        self.setTabButtonColor(self.DIYButton)

    def ChangeTypeStackPDFJS(self):
        """改变类型控件组 PDFJS"""
        self.TypeStack.setCurrentWidget(self.PDFJSPanel)
        self.setTabButtonColor(self.PDFJSButton)

    def ChangeTypeStackTerminal(self):
        """改变类型控件组 Terminal"""
        self.TypeStack.setCurrentWidget(self.TerminalPanel)
        self.setTabButtonColor(self.TerminalButton)

    def ChangeTypeStackBrowser(self):
        self.TypeStack.setCurrentWidget(self.BrowserPanel)
        self.setTabButtonColor(self.BrowserButton)

    def ChangeTypeStackWiki(self):
        self.TypeStack.setCurrentWidget(self.WikiPanel)
        self.setTabButtonColor(self.WikiButton)

    def ChangeTypeStackKiwix(self):
        self.TypeStack.setCurrentWidget(self.KiwixPanel)
        self.setTabButtonColor(self.KiwixButton)

    def center(self):
        """窗口居中显示"""
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def FormClosing(self):
        self.StatusThread.exit()
        self.MainWindow.close()

    def reTranslateUi(self, MainWindow):
        MainWindow.setWindowTitle("ICTFE")
        self.ReverseButton.setText("二进制")
        self.WebButton.setText("Web渗透")
        self.CryptoButton.setText("数据流")
        self.MiscButton.setText("独立工具")
        self.TerminalButton.setText("数据厨师")
        self.WikiButton.setText("Wiki")
        self.BrowserButton.setText("浏览器")
        self.KiwixButton.setText("Kiwix")
        self.DIYButton.setText("启动器")
        self.PDFJSButton.setText("PDF阅读")


class SystemInfoThread(QtCore.QThread):

    def __init__(self, window):
        super(SystemInfoThread, self).__init__()
        self.__win = window
        self.__win.StatusBar.setStyleSheet('QStatusBar{color: white; border: 1px solid rgb(50, 50, 50);}')
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
                '  -> ICTFE - Version 1.0.0 Dev Build 28147 | Powered By Reverier       ' +
                "NetSpeed: %.2fK/s" % ((new_net_speed - old_net_speed) / 1024) + '      Memory Usage: ' + str(
                    int(psutil.virtual_memory().used * 100 / psutil.virtual_memory().total)) + '%' +
                '      CPU Usage: ' + str(psutil.cpu_percent()) + '%')
            old_net_speed = new_net_speed
