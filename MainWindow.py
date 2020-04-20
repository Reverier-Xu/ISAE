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
from CryptoPanel import CryptoPanel
from kiwix.KiwixPanel import KiwixPanel
import psutil
import time
import random


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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.MainWindow.setStyleSheet("QMainWindow#MainWindow{\n"
                                      "background-color: rgb(30, 30, 30);\n"
                                      "border: 1px rgb(50, 50, 50);\n"
                                      "border-style: solid;\n"
                                      "}")
        self.centralwidget.setObjectName("centralwidget")
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
        self.horizontalLayout.addWidget(self.TitleLabel)
        self.TabLayout = QtWidgets.QHBoxLayout()
        self.TabLayout.setContentsMargins(0, 0, 0, 0)
        self.TabLayout.setObjectName("TabLayout")
        self.horizontalLayout.addLayout(self.TabLayout)
        spacerItem = QtWidgets.QSpacerItem(
            1088, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.MiniButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MiniButton.sizePolicy().hasHeightForWidth())
        self.MiniButton.setSizePolicy(sizePolicy)
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
        self.horizontalLayout.addWidget(self.MiniButton)
        self.MaxButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MaxButton.sizePolicy().hasHeightForWidth())
        self.MaxButton.setSizePolicy(sizePolicy)
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
        self.horizontalLayout.addWidget(self.MaxButton)
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CloseButton.sizePolicy().hasHeightForWidth())
        self.CloseButton.setSizePolicy(sizePolicy)
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
        self.horizontalLayout.addWidget(self.CloseButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.ReverseButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.ReverseButton.sizePolicy().hasHeightForWidth())
        self.ReverseButton.setSizePolicy(sizePolicy)
        self.ReverseButton.setObjectName("ReverseButton")
        self.ReverseButton.setMaximumHeight(32)

        self.TabLayout.setSpacing(0)


        self.TabLayout.addWidget(self.ReverseButton)
        self.WebButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.WebButton.sizePolicy().hasHeightForWidth())
        self.WebButton.setSizePolicy(sizePolicy)
        self.WebButton.setObjectName("WebButton")
        self.WebButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.WebButton)
        self.CryptoButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.CryptoButton.sizePolicy().hasHeightForWidth())
        self.CryptoButton.setSizePolicy(sizePolicy)
        self.CryptoButton.setObjectName("CryptoButton")
        self.CryptoButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.CryptoButton)
        self.PwnButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.PwnButton.sizePolicy().hasHeightForWidth())
        self.PwnButton.setSizePolicy(sizePolicy)
        self.PwnButton.setObjectName("PwnButton")
        self.PwnButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.PwnButton)
        self.MiscButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.MiscButton.sizePolicy().hasHeightForWidth())
        self.MiscButton.setSizePolicy(sizePolicy)
        self.MiscButton.setObjectName("MiscButton")
        self.MiscButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.MiscButton)
        self.TerminalButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.TerminalButton.sizePolicy().hasHeightForWidth())
        self.TerminalButton.setSizePolicy(sizePolicy)
        self.TerminalButton.setObjectName("TerminalButton")
        self.TerminalButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.TerminalButton)
        self.WikiButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.WikiButton.sizePolicy().hasHeightForWidth())
        self.WikiButton.setSizePolicy(sizePolicy)
        self.WikiButton.setMaximumHeight(32)
        self.WikiButton.setObjectName("WikiButton")
        self.TabLayout.addWidget(self.WikiButton)
        self.BrowserButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.BrowserButton.sizePolicy().hasHeightForWidth())
        self.BrowserButton.setSizePolicy(sizePolicy)
        self.BrowserButton.setObjectName("BrowserButton")
        self.BrowserButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.BrowserButton)
        self.KiwixButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.KiwixButton.sizePolicy().hasHeightForWidth())
        self.KiwixButton.setSizePolicy(sizePolicy)
        self.KiwixButton.setObjectName("KiwixButton")
        self.KiwixButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.KiwixButton)
        self.DIYButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.DIYButton.sizePolicy().hasHeightForWidth())
        self.DIYButton.setSizePolicy(sizePolicy)
        self.DIYButton.setObjectName("DIYButton")
        self.DIYButton.setMaximumHeight(32)
        self.TabLayout.addWidget(self.DIYButton)
        self.PDFJSButton = uni_Widget.ICTFEButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.PDFJSButton.sizePolicy().hasHeightForWidth())
        self.PDFJSButton.setSizePolicy(sizePolicy)
        self.PDFJSButton.setMaximumHeight(32)
        self.PDFJSButton.setObjectName("PDFJSButton")
        self.TabLayout.addWidget(self.PDFJSButton)

        self.TypeStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.TypeStack.setMinimumSize(QtCore.QSize(1000, 600))
        self.TypeStack.setStyleSheet("QWidget#TypeStack{\n"
                                     "background-color: transparent;\n"
                                     "}")
        self.TypeStack.setObjectName("TypeStack")

        # Reverse Panel
        self.ReversePanel = QtWidgets.QWidget()
        self.ReversePanel.setObjectName("ReversePanel")
        self.TypeStack.addWidget(self.ReversePanel)

        # Web Panel
        self.WebPanel = QtWidgets.QWidget()
        self.WebPanel.setObjectName("WebPanel")
        self.TypeStack.addWidget(self.WebPanel)

        # Crypto Panel
        self.CryptoPanel = CryptoPanel.CryptoPanel()
        self.CryptoPanel.setObjectName("CryptoPanel")
        self.TypeStack.addWidget(self.CryptoPanel)

        # Pwn panel
        self.PwnPanel = QtWidgets.QWidget()
        self.PwnPanel.setObjectName("PwnPanel")
        self.TypeStack.addWidget(self.PwnPanel)

        # Misc Panel
        self.MiscPanel = QtWidgets.QWidget()
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

        self.SplitterWidget1 = QtWidgets.QWidget(self)
        self.SplitterWidget1.setMaximumHeight(3)
        self.SplitterWidget1.setMinimumHeight(3)
        self.SplitterWidget1.setStyleSheet("QWidget{\n"
                                           "background-color: rgb(130, 50, 235);\n"
                                           "border: 2px rgb(130, 50, 235);\n"
                                           "border-style: solid;\n"
                                           "}")
        self.verticalLayout.addWidget(self.SplitterWidget1)
        self.styleGetter = 0

        self.verticalLayout.addWidget(self.TypeStack)
        MainWindow.setCentralWidget(self.centralwidget)
        self.MaxFlag = False

        self.retranslateUi(MainWindow)
        self.MiniButton.clicked.connect(MainWindow.showMinimized)
        self.CloseButton.clicked.connect(self.FormClosing)
        self.MaxButton.clicked.connect(MainWindow.MaximumWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.CryptoButton.clicked.connect(self.ChangeTypeStackCrypto)
        self.ReverseButton.clicked.connect(self.ChangeTypeStackReverse)
        self.MiscButton.clicked.connect(self.ChangeTypeStackMisc)
        self.WebButton.clicked.connect(self.ChangeTypeStackWeb)
        self.PwnButton.clicked.connect(self.ChangeTypeStackPwn)
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
        self.PwnButton.setStyleSheet(uni_Widget.ButtonStyleNormal)
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
        '''改变类型控件组 密码学'''
        self.TypeStack.setCurrentWidget(self.CryptoPanel)
        self.setTabButtonColor(self.CryptoButton)

    def ChangeTypeStackReverse(self):
        '''改变类型控件组 逆向'''
        self.TypeStack.setCurrentWidget(self.ReversePanel)
        self.setTabButtonColor(self.ReverseButton)

    def ChangeTypeStackWeb(self):
        '''改变类型控件组 web'''
        self.TypeStack.setCurrentWidget(self.WebPanel)
        self.setTabButtonColor(self.WebButton)

    def ChangeTypeStackMisc(self):
        '''改变类型控件组 杂项'''
        self.TypeStack.setCurrentWidget(self.MiscPanel)
        self.setTabButtonColor(self.MiscButton)

    def ChangeTypeStackPwn(self):
        '''改变类型控件组 pwn'''
        self.TypeStack.setCurrentWidget(self.PwnPanel)
        self.setTabButtonColor(self.PwnButton)

    def ChangeTypeStackDIY(self):
        '''改变类型控件组 DIY'''
        self.TypeStack.setCurrentWidget(self.DIYPanel)
        self.setTabButtonColor(self.DIYButton)

    def ChangeTypeStackPDFJS(self):
        '''改变类型控件组 PDFJS'''
        self.TypeStack.setCurrentWidget(self.PDFJSPanel)
        self.setTabButtonColor(self.PDFJSButton)

    def ChangeTypeStackTerminal(self):
        '''改变类型控件组 Terminal'''
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
        '''窗口居中显示'''
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def FormClosing(self):
        self.StatusThread.exit()
        self.MainWindow.close()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ReverseButton.setText(_translate("MainWindow", "逆向工程"))
        self.WebButton.setText(_translate("MainWindow", "Web渗透"))
        self.CryptoButton.setText(_translate("MainWindow", "密码编码"))
        self.PwnButton.setText(_translate("MainWindow", "PWN!"))
        self.MiscButton.setText(_translate("MainWindow", "杂项工具"))
        self.TerminalButton.setText(_translate("MainWindow", "数据厨师"))
        self.WikiButton.setText(_translate("MainWindow", "Wiki"))
        self.BrowserButton.setText(_translate("MainWindow", "浏览器"))
        self.KiwixButton.setText(_translate("MainWindow", "Kiwix"))
        self.DIYButton.setText(_translate("MainWindow", "启动器"))
        self.PDFJSButton.setText(_translate("MainWindow", "PDF阅读"))


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
