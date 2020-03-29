# -*- coding: utf-8 -*-

################################################
#                                              #
#  Powered By Reverier, XDSEC     2020 03 25   #
#                                              #
################################################

from PyQt5 import QtCore, QtGui, QtWidgets, Qt
from CryptoPanel import Crypto
from ui_Widgets import uni_Widget


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        QtGui.QFontDatabase.addApplicationFont('./Resources/wqy-microhei.ttc')
        # some variables
        self.TypeMode = 0
        # define MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1600, 900)
        MainWindow.setMinimumSize(QtCore.QSize(1600, 900))
        MainWindow.setMaximumSize(QtCore.QSize(1600, 900))
        MainWindow.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        MainWindow.setStyleSheet(
            "QWidget#centralwidget{image:url(./Resources/background.png)}")
        self.setWindowIcon(QtGui.QIcon('./Resources/icon.png'))

        # central widget
        self.CentralWidget = QtWidgets.QWidget(MainWindow)
        self.CentralWidget.setStyleSheet("")
        self.CentralWidget.setObjectName("centralwidget")

        # Close Button
        self.CloseButton = QtWidgets.QPushButton(self.CentralWidget)
        self.CloseButton.setGeometry(QtCore.QRect(1544, 2, 54, 32))
        self.CloseButton.setStyleSheet(
            "QPushButton#CloseButton{"
            "image:url(./Resources/close);"
            "border:none;"
            "}\n"
            "QPushButton#CloseButton:hover{"
            "image:url(./Resources/close1);"
            "border:none;"
            "}\n"
            "QPushButton#CloseButton:pressed{"
            "image:url(./Resources/close2);"
            "border:none;"
            "}")
        self.CloseButton.setText("")
        self.CloseButton.setObjectName("CloseButton")

        # Minimize Button
        self.MiniButton = QtWidgets.QPushButton(self.CentralWidget)
        self.MiniButton.setGeometry(QtCore.QRect(1490, 2, 54, 32))
        self.MiniButton.setStyleSheet(
            "QPushButton#MiniButton{"
            "image:url(./Resources/mini);"
            "border:none;"
            "}\n"
            "QPushButton#MiniButton:hover{"
            "image:url(./Resources/mini1);"
            "border:none;"
            "}\n"
            "QPushButton#MiniButton:pressed{"
            "image:url(./Resources/mini2);"
            "border:none;"
            "}")
        self.MiniButton.setText("")
        self.MiniButton.setObjectName("MiniButton")

        '''Start define Type Change Button'''

        # Crypto Button
        self.CryptoButton = uni_Widget.ICTFEButton(self.CentralWidget)
        self.CryptoButton.setGeometry(QtCore.QRect(24, 350, 120, 45))
        self.CryptoButton.setObjectName("CryptoButton")

        # Misc Button
        self.MiscButton = uni_Widget.ICTFEButton(self.CentralWidget)
        self.MiscButton.setGeometry(QtCore.QRect(24, 550, 120, 45))
        self.MiscButton.setObjectName("MiscButton")

        # Reverse Button
        self.ReverseButton = uni_Widget.ICTFEButton(self.CentralWidget)
        self.ReverseButton.setGeometry(QtCore.QRect(24, 150, 120, 45))
        self.ReverseButton.setObjectName("ReverseButton")

        # Web Button
        self.WebButton = uni_Widget.ICTFEButton(self.CentralWidget)
        self.WebButton.setGeometry(QtCore.QRect(24, 250, 120, 45))
        self.WebButton.setObjectName("WebButton")

        # Pwn Button
        self.PwnButton = uni_Widget.ICTFEButton(self.CentralWidget)
        self.PwnButton.setGeometry(QtCore.QRect(24, 450, 120, 45))
        self.PwnButton.setObjectName("PwnButton")

        '''End define Type Change Button'''

        # File Temp Stack
        self.FileTempStackTip = uni_Widget.ICTFELabel(self.CentralWidget)
        self.FileTempStackTip.setGeometry(QtCore.QRect(24, 630, 120, 30))
        self.FileTempStackTip.setObjectName('FileTempStackTip')
        self.FileTempStackTip.setText('暂存池')
        
        self.FileTempStackDelButton = uni_Widget.ICTFEButton(self.CentralWidget)
        self.FileTempStackDelButton.setGeometry(QtCore.QRect(114, 632, 30, 30))
        self.FileTempStackDelButton.setObjectName("FileTempStackDelButton")
        self.FileTempStackDelButton.setText('×')
        
        self.FileTempStack = uni_Widget.ICTFEList(self.CentralWidget)
        self.FileTempStack.setGeometry(QtCore.QRect(24, 670, 120, 200))
        self.FileTempStack.setObjectName('FileTempStack')

        '''Begin define Type panel change method'''
        self.TypeStack = QtWidgets.QStackedWidget(self.CentralWidget)
        self.TypeStack.setGeometry(QtCore.QRect(170, 130, 1425, 765))
        self.TypeStack.setObjectName("TypeStack")

        # Choose ticker
        self.TypeChooserBox = [-10, 195, 295, 395, 495, 595]
        self.TypeChooser = QtWidgets.QLabel(self.CentralWidget)
        self.TypeChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.TypeChooser.setGeometry(QtCore.QRect(
            24, self.TypeChooserBox[self.TypeMode], 120, 8))

        # Reverse Panel
        self.ReversePanel = QtWidgets.QWidget()
        self.ReversePanel.setObjectName("ReversePanel")
        self.TypeStack.addWidget(self.ReversePanel)

        # Web Panel
        self.WebPanel = QtWidgets.QWidget()
        self.WebPanel.setObjectName("WebPanel")
        self.TypeStack.addWidget(self.WebPanel)

        # Crypto Panel
        self.CryptoPanel = Crypto.CryptoPanel()
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

        # Welcome Panel
        self.WelcomePanel = QtWidgets.QWidget()
        self.WelcomePanel.setObjectName('WelcomePanel')
        self.WelcomePanel.setStyleSheet(
            'QWidget#WelcomePanel{image:url(./Resources/welcome.png)}')
        self.TypeStack.addWidget(self.WelcomePanel)

        # Set MainWindow Widget
        MainWindow.setCentralWidget(self.CentralWidget)

        # other process.
        self.retranslateUi(MainWindow)
        self.CloseButton.clicked.connect(MainWindow.close)
        self.MiniButton.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.CryptoButton.clicked.connect(self.ChangeTypeStackCrypto)
        self.ReverseButton.clicked.connect(self.ChangeTypeStackReverse)
        self.MiscButton.clicked.connect(self.ChangeTypeStackMisc)
        self.WebButton.clicked.connect(self.ChangeTypeStackWeb)
        self.PwnButton.clicked.connect(self.ChangeTypeStackPwn)

        self.FileTempStack.doubleClicked.connect(self.FileStackCopy)
        self.FileTempStackDelButton.clicked.connect(self.DelFileTempStack)
        self.center()

    # functions

    def DelFileTempStack(self):
        item = self.FileTempStack.currentItem()
        self.FileTempStack.takeItem(self.FileTempStack.row(item))

    def FileStackCopy(self):
        print(self.FileTempStack.selectedItems()[0].text())
        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.setText(self.FileTempStack.selectedItems()[0].text())

    def ChangeTypeStackCrypto(self):
        '''改变类型控件组 密码学'''
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.TypeChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 3
        self.TypeStack.setCurrentWidget(self.CryptoPanel)
        self.CryptoPanel.ChangeCryptoBase()
        animation.setEndValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackReverse(self):
        '''改变类型控件组 逆向'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 1
        self.TypeStack.setCurrentWidget(self.ReversePanel)
        animation.setEndValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackWeb(self):
        '''改变类型控件组 web'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 2
        self.TypeStack.setCurrentWidget(self.WebPanel)
        animation.setEndValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackMisc(self):
        '''改变类型控件组 杂项'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 5
        self.TypeStack.setCurrentWidget(self.MiscPanel)
        animation.setEndValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackPwn(self):
        '''改变类型控件组 pwn'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 4
        self.TypeStack.setCurrentWidget(self.PwnPanel)
        animation.setEndValue(QtCore.QPoint(
            24, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def center(self):
        '''窗口居中显示'''
        qr = self.frameGeometry()
        cp = QtWidgets.QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.CryptoButton.setText(_translate("MainWindow", "密码"))
        self.MiscButton.setText(_translate("MainWindow", "杂项"))
        self.ReverseButton.setText(_translate("MainWindow", "逆向"))
        self.WebButton.setText(_translate("MainWindow", "Web"))
        self.PwnButton.setText(_translate("MainWindow", "Pwn"))
