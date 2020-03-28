# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ICTFE.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import resource
from basecom import *
import quopri
from urllib import parse
import binascii
import html


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # some varibles
        self.TypeMode = 0
        self.BaseMode = 1
        self.CryptoMode = 1

        # font config
        QtGui.QFontDatabase.addApplicationFont("./Resources/wqy-microhei.ttc")

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
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("")
        self.centralwidget.setObjectName("centralwidget")

        # Close Button
        self.CloseButton = QtWidgets.QPushButton(self.centralwidget)
        self.CloseButton.setGeometry(QtCore.QRect(1544, 2, 54, 32))
        self.CloseButton.setStyleSheet("QPushButton#CloseButton{image:url(:/img/close);border:none;}\n"
                                       "QPushButton#CloseButton:hover{image:url(:/img/close1);border:none;}\n"
                                       "QPushButton#CloseButton:pressed{image:url(:/img/close2);border:none;}")
        self.CloseButton.setText("")
        self.CloseButton.setObjectName("CloseButton")

        # Minimize Button
        self.MiniButton = QtWidgets.QPushButton(self.centralwidget)
        self.MiniButton.setGeometry(QtCore.QRect(1490, 2, 54, 32))
        self.MiniButton.setStyleSheet("QPushButton#MiniButton{image:url(:/img/mini);border:none;}\n"
                                      "QPushButton#MiniButton:hover{image:url(:/img/mini1);border:none;}\n"
                                      "QPushButton#MiniButton:pressed{image:url(:/img/mini2);border:none;}")
        self.MiniButton.setText("")
        self.MiniButton.setObjectName("MiniButton")

        '''Start define Type Change Button'''

        # Crypto Button
        self.CryptoButton = QtWidgets.QPushButton(self.centralwidget)
        self.CryptoButton.setGeometry(QtCore.QRect(20, 350, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)
        self.CryptoButton.setFont(font)
        self.CryptoButton.setStyleSheet(
            "QPushButton#CryptoButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.CryptoButton.setFlat(True)
        self.CryptoButton.setObjectName("CryptoButton")

        # Misc Button
        self.MiscButton = QtWidgets.QPushButton(self.centralwidget)
        self.MiscButton.setGeometry(QtCore.QRect(20, 550, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)
        self.MiscButton.setFont(font)
        self.MiscButton.setStyleSheet(
            "QPushButton#MiscButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.MiscButton.setFlat(True)
        self.MiscButton.setObjectName("MiscButton")

        # Reverse Button
        self.ReverseButton = QtWidgets.QPushButton(self.centralwidget)
        self.ReverseButton.setGeometry(QtCore.QRect(20, 150, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)
        self.ReverseButton.setFont(font)
        self.ReverseButton.setStyleSheet(
            "QPushButton#ReverseButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.ReverseButton.setFlat(True)
        self.ReverseButton.setObjectName("ReverseButton")

        # Web Button
        self.WebButton = QtWidgets.QPushButton(self.centralwidget)
        self.WebButton.setGeometry(QtCore.QRect(20, 250, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)
        self.WebButton.setFont(font)
        self.WebButton.setStyleSheet(
            "QPushButton#WebButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.WebButton.setFlat(True)
        self.WebButton.setObjectName("WebButton")

        # Pwn Button
        self.PwnButton = QtWidgets.QPushButton(self.centralwidget)
        self.PwnButton.setGeometry(QtCore.QRect(20, 450, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)
        self.PwnButton.setFont(font)
        self.PwnButton.setStyleSheet(
            "QPushButton#PwnButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.PwnButton.setFlat(True)
        self.PwnButton.setObjectName("PwnButton")

        '''End define Type Change Button'''

        # File Temp Stack
        self.FileTempStackTip = QtWidgets.QLabel(self.centralwidget)
        self.FileTempStackTip.setGeometry(QtCore.QRect(20, 630, 120, 30))
        self.FileTempStackTip.setObjectName('FileTempStackTip')
        self.FileTempStackTip.setStyleSheet('#FileTempStackTip{color: white;}')
        self.FileTempStackTip.setText('暂存池')
        self.FileTempStackTip.setFont(font)
        self.FileTempStackDelButton = QtWidgets.QPushButton(self.centralwidget)
        self.FileTempStackDelButton.setGeometry(QtCore.QRect(110, 632, 30, 30))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)
        self.FileTempStackDelButton.setFont(font)
        self.FileTempStackDelButton.setStyleSheet(
            "QPushButton#FileTempStackDelButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.FileTempStackDelButton.setFlat(True)
        self.FileTempStackDelButton.setObjectName("FileTempStackDelButton")
        self.FileTempStackDelButton.setText('×')
        font.setFamily("consolas")
        font.setPointSize(12)
        self.FileTempStack = QtWidgets.QListWidget(self.centralwidget)
        self.FileTempStack.setGeometry(QtCore.QRect(20, 670, 120, 200))
        self.FileTempStack.setObjectName('FileTempStack')
        self.FileTempStack.setFont(font)
        self.FileTempStack.setStyleSheet(
            '#FileTempStack{background-color: rgb(20,20,20); color: white}')
        self.FileTempStack.setDragEnabled(True)
        self.FileTempStack.setAcceptDrops(True)
        self.FileTempStack.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.FileTempStack.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        font.setFamily("文泉驿微米黑")
        font.setPointSize(20)

        '''Begin define Type panel change method'''
        self.TypeStack = QtWidgets.QStackedWidget(self.centralwidget)
        self.TypeStack.setGeometry(QtCore.QRect(170, 130, 1425, 765))
        self.TypeStack.setObjectName("TypeStack")

        # Choose ticker
        self.TypeChooserBox = [-10, 195, 295, 395, 495, 595]
        self.TypeChooser = QtWidgets.QLabel(self.centralwidget)
        self.TypeChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.TypeChooser.setGeometry(QtCore.QRect(
            20, self.TypeChooserBox[self.TypeMode], 120, 8))

        # Reverse Panel
        self.ReversePanel = QtWidgets.QWidget()
        self.ReversePanel.setObjectName("ReversePanel")
        self.TypeStack.addWidget(self.ReversePanel)

        # Web Panel
        self.WebPanel = QtWidgets.QWidget()
        self.WebPanel.setObjectName("WebPanel")
        self.TypeStack.addWidget(self.WebPanel)

        # Crypto Panel
        self.CryptoPanel = QtWidgets.QWidget()
        self.CryptoPanel.setObjectName("CryptoPanel")

        # Crypto Buttons

        self.CryptoChoosePanel = QtWidgets.QWidget()
        self.CryptoChoosePanel.setObjectName('CryptoChoosePanel')
        self.CryptoChoosePanel.setGeometry(0, 0, 1420, 300)

        self.CryptoChoosePanelScroll = QtWidgets.QScrollArea(self.CryptoPanel)
        self.CryptoChoosePanelScroll.setGeometry(0, 0, 1426, 128)
        self.CryptoChoosePanelScroll.setStyleSheet(
            '#CryptoChoosePanelScroll{background-color:transparent}')
        self.CryptoChoosePanelScroll.viewport().setStyleSheet(
            'background-color:transparent;')
        self.CryptoChoosePanelScroll.setWidget(self.CryptoChoosePanel)
        self.CryptoChoosePanelScroll.setHorizontalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)
        self.CryptoChoosePanelScroll.setVerticalScrollBarPolicy(
            QtCore.Qt.ScrollBarAlwaysOff)

        # Choose ticker
        self.CryptoChooserBox = [0, 11, 141, 271, 401, 531, 661, 791]
        self.CryptoChooser = QtWidgets.QLabel(self.CryptoChoosePanel)
        self.CryptoChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.CryptoChooser.setGeometry(QtCore.QRect(
            self.CryptoChooserBox[self.CryptoMode], 55, 120, 8))

        # Base Button
        self.BaseButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.BaseButton.setGeometry(QtCore.QRect(11, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.BaseButton.setFont(font)
        self.BaseButton.setStyleSheet(
            "QPushButton#BaseButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseButton.setText("Base系列")
        self.BaseButton.setFlat(True)
        self.BaseButton.setObjectName("BaseButton")

        # Quote-Printable Button
        self.QuoteButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.QuoteButton.setGeometry(QtCore.QRect(141, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.QuoteButton.setFont(font)
        self.QuoteButton.setStyleSheet(
            "QPushButton#QuoteButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteButton.setText("Quote-P")
        self.QuoteButton.setFlat(True)
        self.QuoteButton.setObjectName("QuoteButton")

        # Url Button
        self.UrlButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.UrlButton.setGeometry(QtCore.QRect(271, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.UrlButton.setFont(font)
        self.UrlButton.setStyleSheet(
            "QPushButton#UrlButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.UrlButton.setText("Url编码")
        self.UrlButton.setFlat(True)
        self.UrlButton.setObjectName("UrlButton")

        # Hex Button
        self.HexButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.HexButton.setGeometry(QtCore.QRect(401, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.HexButton.setFont(font)
        self.HexButton.setStyleSheet(
            "QPushButton#HexButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HexButton.setText("Hex编码")
        self.HexButton.setFlat(True)
        self.HexButton.setObjectName("HexButton")

        # HTML Button
        self.HTMLButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.HTMLButton.setGeometry(QtCore.QRect(531, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.HTMLButton.setFont(font)
        self.HTMLButton.setStyleSheet(
            "QPushButton#HTMLButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HTMLButton.setText("HTML编码")
        self.HTMLButton.setFlat(True)
        self.HTMLButton.setObjectName("HTMLButton")

        # Escape Button
        self.EscapeButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.EscapeButton.setGeometry(QtCore.QRect(661, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.EscapeButton.setFont(font)
        self.EscapeButton.setStyleSheet(
            "QPushButton#EscapeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.EscapeButton.setText("Escape")
        self.EscapeButton.setFlat(True)
        self.EscapeButton.setObjectName("EscapeButton")

        # Tap Button
        self.TapButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.TapButton.setGeometry(QtCore.QRect(791, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.TapButton.setFont(font)
        self.TapButton.setStyleSheet(
            "QPushButton#TapButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.TapButton.setText("敲击码")
        self.TapButton.setFlat(True)
        self.TapButton.setObjectName("TapButton")

        # Morse Button
        self.MorseButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.MorseButton.setGeometry(QtCore.QRect(921, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.MorseButton.setFont(font)
        self.MorseButton.setStyleSheet(
            "QPushButton#MorseButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.MorseButton.setText("摩斯电码")
        self.MorseButton.setFlat(True)
        self.MorseButton.setObjectName("MorseButton")

        # Hash Button
        self.HashButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.HashButton.setGeometry(QtCore.QRect(1051, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.HashButton.setFont(font)
        self.HashButton.setStyleSheet(
            "QPushButton#HashButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HashButton.setText("Hash计算")
        self.HashButton.setFlat(True)
        self.HashButton.setObjectName("HashButton")

        # AES Button
        self.AESButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.AESButton.setGeometry(QtCore.QRect(1181, 10, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.AESButton.setFont(font)
        self.AESButton.setStyleSheet(
            "QPushButton#AESButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.AESButton.setText("AES加密")
        self.AESButton.setFlat(True)
        self.AESButton.setObjectName("AESButton")

        # DES Button
        self.DESButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.DESButton.setGeometry(QtCore.QRect(11, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.DESButton.setFont(font)
        self.DESButton.setStyleSheet(
            "QPushButton#DESButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.DESButton.setText("DES加密")
        self.DESButton.setFlat(True)
        self.DESButton.setObjectName("DESButton")

        # RC4 Button
        self.RC4Button = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.RC4Button.setGeometry(QtCore.QRect(141, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.RC4Button.setFont(font)
        self.RC4Button.setStyleSheet(
            "QPushButton#RC4Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.RC4Button.setText("RC4编码")
        self.RC4Button.setFlat(True)
        self.RC4Button.setObjectName("RC4Button")

        # ASCIITranslate Button
        self.ASCIITranslateButton = QtWidgets.QPushButton(
            self.CryptoChoosePanel)
        self.ASCIITranslateButton.setGeometry(QtCore.QRect(271, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.ASCIITranslateButton.setFont(font)
        self.ASCIITranslateButton.setStyleSheet(
            "QPushButton#ASCIITranslateButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.ASCIITranslateButton.setText("进制转换")
        self.ASCIITranslateButton.setFlat(True)
        self.ASCIITranslateButton.setObjectName("ASCIITranslateButton")

        # RSA Button
        self.RSAButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.RSAButton.setGeometry(QtCore.QRect(401, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.RSAButton.setFont(font)
        self.RSAButton.setStyleSheet(
            "QPushButton#RSAButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.RSAButton.setText("RSA工具")
        self.RSAButton.setFlat(True)
        self.RSAButton.setObjectName("RSAButton")

        # CodeTranslate Button
        self.CodeTranslateButton = QtWidgets.QPushButton(
            self.CryptoChoosePanel)
        self.CodeTranslateButton.setGeometry(QtCore.QRect(531, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.CodeTranslateButton.setFont(font)
        self.CodeTranslateButton.setStyleSheet(
            "QPushButton#CodeTranslateButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.CodeTranslateButton.setText("编码转换")
        self.CodeTranslateButton.setFlat(True)
        self.CodeTranslateButton.setObjectName("CodeTranslateButton")

        # ADFGVX Button
        self.ADFGVXButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.ADFGVXButton.setGeometry(QtCore.QRect(661, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.ADFGVXButton.setFont(font)
        self.ADFGVXButton.setStyleSheet(
            "QPushButton#ADFGVXButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.ADFGVXButton.setText("ADFGVX")
        self.ADFGVXButton.setFlat(True)
        self.ADFGVXButton.setObjectName("ADFGVXButton")

        # Affine Button
        self.AffineButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.AffineButton.setGeometry(QtCore.QRect(791, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.AffineButton.setFont(font)
        self.AffineButton.setStyleSheet(
            "QPushButton#AffineButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.AffineButton.setText("仿射密码")
        self.AffineButton.setFlat(True)
        self.AffineButton.setObjectName("AffineButton")

        # AutoKey Button
        self.AutoKeyButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.AutoKeyButton.setGeometry(QtCore.QRect(921, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.AutoKeyButton.setFont(font)
        self.AutoKeyButton.setStyleSheet(
            "QPushButton#AutoKeyButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.AutoKeyButton.setText("自动密钥机")
        self.AutoKeyButton.setFlat(True)
        self.AutoKeyButton.setObjectName("AutoKeyButton")

        # Atbash Button
        self.AtbashButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.AtbashButton.setGeometry(QtCore.QRect(1051, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.AtbashButton.setFont(font)
        self.AtbashButton.setStyleSheet(
            "QPushButton#AtbashButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.AtbashButton.setText("Atbash")
        self.AtbashButton.setFlat(True)
        self.AtbashButton.setObjectName("AtbashButton")

        # Beaufort Button
        self.BeaufortButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.BeaufortButton.setGeometry(QtCore.QRect(1181, 75, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.BeaufortButton.setFont(font)
        self.BeaufortButton.setStyleSheet(
            "QPushButton#BeaufortButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BeaufortButton.setText("Beaufort")
        self.BeaufortButton.setFlat(True)
        self.BeaufortButton.setObjectName("BeaufortButton")

        # Bifid Button
        self.BifidButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.BifidButton.setGeometry(QtCore.QRect(11, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.BifidButton.setFont(font)
        self.BifidButton.setStyleSheet(
            "QPushButton#BifidButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BifidButton.setText("Bifid")
        self.BifidButton.setFlat(True)
        self.BifidButton.setObjectName("BifidButton")

        # Casar Button
        self.CasarButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.CasarButton.setGeometry(QtCore.QRect(141, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.CasarButton.setFont(font)
        self.CasarButton.setStyleSheet(
            "QPushButton#CasarButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.CasarButton.setText("Casar")
        self.CasarButton.setFlat(True)
        self.CasarButton.setObjectName("CasarButton")

        # CT Button
        self.CTButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.CTButton.setGeometry(QtCore.QRect(271, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.CTButton.setFont(font)
        self.CTButton.setStyleSheet(
            "QPushButton#CTButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.CTButton.setText("列移位")
        self.CTButton.setFlat(True)
        self.CTButton.setObjectName("CTButton")

        # Enigma Button
        self.EnigmaButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.EnigmaButton.setGeometry(QtCore.QRect(401, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.EnigmaButton.setFont(font)
        self.EnigmaButton.setStyleSheet(
            "QPushButton#EnigmaButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.EnigmaButton.setText("Enigma")
        self.EnigmaButton.setFlat(True)
        self.EnigmaButton.setObjectName("EnigmaButton")

        # FourSquare Button
        self.FourSquareButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.FourSquareButton.setGeometry(QtCore.QRect(531, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.FourSquareButton.setFont(font)
        self.FourSquareButton.setStyleSheet(
            "QPushButton#FourSquareButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.FourSquareButton.setText("四方密码")
        self.FourSquareButton.setFlat(True)
        self.FourSquareButton.setObjectName("FourSquareButton")

        # GronsFeld Button
        self.GronsFeldButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.GronsFeldButton.setGeometry(QtCore.QRect(661, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.GronsFeldButton.setFont(font)
        self.GronsFeldButton.setStyleSheet(
            "QPushButton#GronsFeldButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.GronsFeldButton.setText("GronsFeld")
        self.GronsFeldButton.setFlat(True)
        self.GronsFeldButton.setObjectName("GronsFeldButton")

        # M209 Button
        self.M209Button = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.M209Button.setGeometry(QtCore.QRect(791, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.M209Button.setFont(font)
        self.M209Button.setStyleSheet(
            "QPushButton#M209Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.M209Button.setText("M-209")
        self.M209Button.setFlat(True)
        self.M209Button.setObjectName("M209Button")

        # PlayFair Button
        self.PlayFairButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.PlayFairButton.setGeometry(QtCore.QRect(921, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.PlayFairButton.setFont(font)
        self.PlayFairButton.setStyleSheet(
            "QPushButton#PlayFairButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.PlayFairButton.setText("PlayFair")
        self.PlayFairButton.setFlat(True)
        self.PlayFairButton.setObjectName("PlayFairButton")

        # Polybius Button
        self.PolybiusButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.PolybiusButton.setGeometry(QtCore.QRect(1051, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.PolybiusButton.setFont(font)
        self.PolybiusButton.setStyleSheet(
            "QPushButton#PolybiusButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.PolybiusButton.setText("Polybius")
        self.PolybiusButton.setFlat(True)
        self.PolybiusButton.setObjectName("PolybiusButton")

        # Porta Button
        self.PortaButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.PortaButton.setGeometry(QtCore.QRect(1181, 130, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.PortaButton.setFont(font)
        self.PortaButton.setStyleSheet(
            "QPushButton#PortaButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.PortaButton.setText("Porta")
        self.PortaButton.setFlat(True)
        self.PortaButton.setObjectName("PortaButton")

        # Railfence Button
        self.RailFenceButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.RailFenceButton.setGeometry(QtCore.QRect(11, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.RailFenceButton.setFont(font)
        self.RailFenceButton.setStyleSheet(
            "QPushButton#RailFenceButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.RailFenceButton.setText("栅栏密码")
        self.RailFenceButton.setFlat(True)
        self.RailFenceButton.setObjectName("RailFenceButton")

        # Rot13 Button
        self.Rot13Button = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.Rot13Button.setGeometry(QtCore.QRect(141, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.Rot13Button.setFont(font)
        self.Rot13Button.setStyleSheet(
            "QPushButton#Rot13Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Rot13Button.setText("Rot13")
        self.Rot13Button.setFlat(True)
        self.Rot13Button.setObjectName("Rot13Button")

        # Substitution Button
        self.SubstitutionButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.SubstitutionButton.setGeometry(QtCore.QRect(271, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.SubstitutionButton.setFont(font)
        self.SubstitutionButton.setStyleSheet(
            "QPushButton#SubstitutionButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.SubstitutionButton.setText("简单换位")
        self.SubstitutionButton.setFlat(True)
        self.SubstitutionButton.setObjectName("SubstitutionButton")

        # Vigenere Button
        self.VigenereButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.VigenereButton.setGeometry(QtCore.QRect(401, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.VigenereButton.setFont(font)
        self.VigenereButton.setStyleSheet(
            "QPushButton#VigenereButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.VigenereButton.setText("Vigenere")
        self.VigenereButton.setFlat(True)
        self.VigenereButton.setObjectName("VigenereButton")

        # Pigen Button
        self.PigenButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.PigenButton.setGeometry(QtCore.QRect(531, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.PigenButton.setFont(font)
        self.PigenButton.setStyleSheet(
            "QPushButton#PigenButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.PigenButton.setText("猪圈密码")
        self.PigenButton.setFlat(True)
        self.PigenButton.setObjectName("PigenButton")

        # Bacon Button
        self.BaconButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.BaconButton.setGeometry(QtCore.QRect(661, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.BaconButton.setFont(font)
        self.BaconButton.setStyleSheet(
            "QPushButton#BaconButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaconButton.setText("培根密码")
        self.BaconButton.setFlat(True)
        self.BaconButton.setObjectName("BaconButton")

        # RunningKey Button
        self.RunningKeyButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.RunningKeyButton.setGeometry(QtCore.QRect(791, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.RunningKeyButton.setFont(font)
        self.RunningKeyButton.setStyleSheet(
            "QPushButton#RunningKeyButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.RunningKeyButton.setText("滚动密钥")
        self.RunningKeyButton.setFlat(True)
        self.RunningKeyButton.setObjectName("RunningKeyButton")

        # Hill Button
        self.HillButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.HillButton.setGeometry(QtCore.QRect(921, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.HillButton.setFont(font)
        self.HillButton.setStyleSheet(
            "QPushButton#HillButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HillButton.setText("希尔密码")
        self.HillButton.setFlat(True)
        self.HillButton.setObjectName("HillButton")

        # A1z26 Button
        self.A1z26Button = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.A1z26Button.setGeometry(QtCore.QRect(1051, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.A1z26Button.setFont(font)
        self.A1z26Button.setStyleSheet(
            "QPushButton#A1z26Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.A1z26Button.setText("A1z26")
        self.A1z26Button.setFlat(True)
        self.A1z26Button.setObjectName("A1z26Button")

        # Beaufort Button
        self.BeaufortButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.BeaufortButton.setGeometry(QtCore.QRect(1181, 185, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.BeaufortButton.setFont(font)
        self.BeaufortButton.setStyleSheet(
            "QPushButton#BeaufortButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BeaufortButton.setText("Beaufort")
        self.BeaufortButton.setFlat(True)
        self.BeaufortButton.setObjectName("BeaufortButton")

        # OtherCipher Button
        self.OtherCipherButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.OtherCipherButton.setGeometry(QtCore.QRect(11, 240, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.OtherCipherButton.setFont(font)
        self.OtherCipherButton.setStyleSheet(
            "QPushButton#OtherCipherButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.OtherCipherButton.setText("编码杂项")
        self.OtherCipherButton.setFlat(True)
        self.OtherCipherButton.setObjectName("OtherCipherButton")

        # JSFuck Button
        self.JSFuckButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.JSFuckButton.setGeometry(QtCore.QRect(141, 240, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.JSFuckButton.setFont(font)
        self.JSFuckButton.setStyleSheet(
            "QPushButton#JSFuckButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.JSFuckButton.setText("JSFuck")
        self.JSFuckButton.setFlat(True)
        self.JSFuckButton.setObjectName("JSFuckButton")

        # BrainFuck Button
        self.BrainFuckButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.BrainFuckButton.setGeometry(QtCore.QRect(271, 240, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.BrainFuckButton.setFont(font)
        self.BrainFuckButton.setStyleSheet(
            "QPushButton#BrainFuckButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BrainFuckButton.setText("BrainFuck")
        self.BrainFuckButton.setFlat(True)
        self.BrainFuckButton.setObjectName("BrainFuckButton")

        # Ook Button
        self.OokButton = QtWidgets.QPushButton(self.CryptoChoosePanel)
        self.OokButton.setGeometry(QtCore.QRect(401, 240, 120, 45))
        font = QtGui.QFont()
        font.setFamily("文泉驿微米黑")
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.OokButton.setFont(font)
        self.OokButton.setStyleSheet(
            "QPushButton#OokButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.OokButton.setText("Ook!")
        self.OokButton.setFlat(True)
        self.OokButton.setObjectName("OokButton")

        # end Crypto Buttons

        # Crypto Panel change methods
        self.CryptoStack = QtWidgets.QStackedWidget(self.CryptoPanel)
        self.CryptoStack.setGeometry(QtCore.QRect(1, 135, 1423, 613))
        self.CryptoStack.setObjectName('CryptoStack')

        # Base panel
        self.BasePanel = QtWidgets.QWidget()
        self.BasePanel.setObjectName('BasePanel')
        self.CryptoStack.addWidget(self.BasePanel)

        # Base Ticker
        self.BaseChooserBox = [0, 10, 140, 270, 400, 530]
        self.BaseChooser = QtWidgets.QLabel(self.BasePanel)
        self.BaseChooser.setPixmap(
            QtGui.QPixmap('./Resources/chooser.png'))
        self.BaseChooser.setGeometry(QtCore.QRect(
            self.BaseChooserBox[self.BaseMode], 55, 120, 8))

        # Base change Buttons
        self.Base64Button = QtWidgets.QPushButton(self.BasePanel)
        self.Base64Button.setObjectName('Base64Button')
        self.Base64Button.setGeometry(QtCore.QRect(10, 10, 120, 45))
        self.Base64Button.setText('Base64')
        self.Base64Button.setFont(font)
        self.Base64Button.setStyleSheet(
            "QPushButton#Base64Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Base64Button.setFlat(True)

        self.Base32Button = QtWidgets.QPushButton(self.BasePanel)
        self.Base32Button.setObjectName('Base32Button')
        self.Base32Button.setGeometry(QtCore.QRect(140, 10, 120, 45))
        self.Base32Button.setText('Base32')
        self.Base32Button.setFont(font)
        self.Base32Button.setStyleSheet(
            "QPushButton#Base32Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Base32Button.setFlat(True)

        self.Base16Button = QtWidgets.QPushButton(self.BasePanel)
        self.Base16Button.setObjectName('Base16Button')
        self.Base16Button.setGeometry(QtCore.QRect(270, 10, 120, 45))
        self.Base16Button.setText('Base16')
        self.Base16Button.setFont(font)
        self.Base16Button.setStyleSheet(
            "QPushButton#Base16Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Base16Button.setFlat(True)

        self.Base85Button = QtWidgets.QPushButton(self.BasePanel)
        self.Base85Button.setObjectName('Base85Button')
        self.Base85Button.setGeometry(QtCore.QRect(400, 10, 120, 45))
        self.Base85Button.setText('Base85ASC')
        self.Base85Button.setFont(font)
        self.Base85Button.setStyleSheet(
            "QPushButton#Base85Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Base85Button.setFlat(True)

        self.Base85RFCButton = QtWidgets.QPushButton(self.BasePanel)
        self.Base85RFCButton.setObjectName('Base85RFCButton')
        self.Base85RFCButton.setGeometry(QtCore.QRect(530, 10, 120, 45))
        self.Base85RFCButton.setText('Base85RFC')
        self.Base85RFCButton.setFont(font)
        self.Base85RFCButton.setStyleSheet(
            "QPushButton#Base85RFCButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Base85RFCButton.setFlat(True)

        self.BaseEButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseEButton.setObjectName('BaseEButton')
        self.BaseEButton.setGeometry(QtCore.QRect(1180, 10, 200, 45))
        self.BaseEButton.setText('Base64隐写提取')
        self.BaseEButton.setFont(font)
        self.BaseEButton.setStyleSheet(
            "QPushButton#BaseEButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseEButton.setFlat(True)

        # end base change buttons

        # eval support
        self.BaseTextEvalCheckBox = QtWidgets.QCheckBox(
            '启用eval', self.BasePanel)
        self.BaseTextEvalCheckBox.setGeometry(QtCore.QRect(580, 135, 120, 40))
        self.BaseTextEvalCheckBox.setObjectName('BaseTextEvalCheckBox')
        self.BaseTextEvalCheckBox.setStyleSheet(
            'QCheckBox:unchecked{ border:none; color: white; }\
                QCheckBox:checked{ border:none; color: cyan; }')
        self.BaseTextEvalCheckBox.setFont(font)

        # base table edit box and label
        self.BaseTableTips = QtWidgets.QLabel(self.BasePanel)
        self.BaseTableTips.setObjectName('BaseTableTips')
        self.BaseTableTips.setText('编码表:')
        self.BaseTableTips.setFont(font)
        self.BaseTableTips.setStyleSheet('color: white;')
        self.BaseTableTips.setGeometry(QtCore.QRect(50, 70, 130, 45))
        self.BaseTableBox = QtWidgets.QLineEdit(self.BasePanel)
        font.setFamily("Consolas")
        self.BaseTableBox.setFont(font)
        self.BaseTableBox.setStyleSheet('color: white;\
            border: 2px solid gray;\
            border-radius: 10px;\
            padding: 0 8px;\
            background: rgb(20, 20, 20);\
            selection-background-color: blue;')
        self.BaseTableBox.setObjectName('BaseTableBox')
        self.BaseTableBox.setGeometry(QtCore.QRect(150, 70, 1000, 45))
        font.setFamily("文泉驿微米黑")
        # base enc button
        self.BaseEncButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseEncButton.setObjectName('BaseEncButton')
        self.BaseEncButton.setGeometry(QtCore.QRect(1160, 70, 120, 45))
        self.BaseEncButton.setText('编码')
        self.BaseEncButton.setFont(font)
        self.BaseEncButton.setStyleSheet(
            "QPushButton#BaseEncButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseEncButton.setFlat(True)

        # base dec button
        self.BaseDecButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseDecButton.setObjectName('BaseDecButton')
        self.BaseDecButton.setGeometry(QtCore.QRect(1280, 70, 120, 45))
        self.BaseDecButton.setText('解码')
        self.BaseDecButton.setFont(font)
        self.BaseDecButton.setStyleSheet(
            "QPushButton#BaseDecButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseDecButton.setFlat(True)

        # input text file button
        self.BaseTextInputPath = ''
        self.BaseTextInputButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseTextInputButton.setObjectName('BaseTextInputButton')
        self.BaseTextInputButton.setGeometry(QtCore.QRect(20, 125, 120, 45))
        self.BaseTextInputButton.setText('打开...')
        self.BaseTextInputButton.setToolTip('点击选择文件')
        self.BaseTextInputButton.setFont(font)
        self.BaseTextInputButton.setStyleSheet(
            "QPushButton#BaseTextInputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseTextInputButton.setFlat(True)

        # output text file button
        self.BaseTextOutputPath = ''
        self.BaseTextOutputButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseTextOutputButton.setObjectName('BaseTextOutputButton')
        self.BaseTextOutputButton.setGeometry(QtCore.QRect(360, 125, 120, 45))
        self.BaseTextOutputButton.setText('另存为...')
        self.BaseTextOutputButton.setToolTip('点击选择文件')
        self.BaseTextOutputButton.setFont(font)
        self.BaseTextOutputButton.setStyleSheet(
            "QPushButton#BaseTextOutputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseTextOutputButton.setFlat(True)

        # input cipher file button
        self.BaseCipherInputPath = ''
        self.BaseCipherInputButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseCipherInputButton.setObjectName('BaseCipherInputButton')
        self.BaseCipherInputButton.setGeometry(QtCore.QRect(720, 125, 120, 45))
        self.BaseCipherInputButton.setText('打开...')
        self.BaseCipherInputButton.setToolTip('点击选择文件')
        self.BaseCipherInputButton.setFont(font)
        self.BaseCipherInputButton.setStyleSheet(
            "QPushButton#BaseCipherInputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseCipherInputButton.setFlat(True)

        # output cipher file button
        self.BaseCipherOutputPath = ''
        self.BaseCipherOutputButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseCipherOutputButton.setObjectName('BaseCipherOutputButton')
        self.BaseCipherOutputButton.setGeometry(
            QtCore.QRect(1060, 125, 120, 45))
        self.BaseCipherOutputButton.setText('另存为...')
        self.BaseCipherOutputButton.setToolTip('点击选择文件')
        self.BaseCipherOutputButton.setFont(font)
        self.BaseCipherOutputButton.setStyleSheet(
            "QPushButton#BaseCipherOutputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseCipherOutputButton.setFlat(True)

        # base text box and cipher box
        font.setFamily("Consolas")
        self.BaseTextBox = QtWidgets.QTextEdit(self.BasePanel)
        self.BaseTextBox.setObjectName('BaseTextBox')
        self.BaseTextBox.setFont(font)
        self.BaseTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.BaseTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.BaseTextBox.setGeometry(QtCore.QRect(20, 180, 640, 430))
        self.BaseTextBox.setPlaceholderText('Base Encode\n这里写明文')
        self.BaseTextBox.setAcceptDrops(True)
        self.BaseTextBox.setAcceptRichText(False)

        self.BaseTranslateButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseTranslateButton.setObjectName('BaseTranslateButton')
        self.BaseTranslateButton.setGeometry(QtCore.QRect(665, 330, 90, 45))
        self.BaseTranslateButton.setText('交换')
        self.BaseTranslateButton.setFont(font)
        self.BaseTranslateButton.setStyleSheet(
            "QPushButton#BaseTranslateButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.BaseTranslateButton.setFlat(True)

        self.BaseCipherBox = QtWidgets.QTextEdit(self.BasePanel)
        self.BaseCipherBox.setObjectName('BaseTextBox')
        self.BaseCipherBox.setFont(font)
        self.BaseCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.BaseCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.BaseCipherBox.setGeometry(QtCore.QRect(760, 180, 640, 430))
        self.BaseCipherBox.setPlaceholderText('Base Decode\n这里写编码')
        self.BaseCipherBox.setAcceptDrops(True)
        self.BaseCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")
        # end base panel

        # begin quote panel
        self.QuotePanel = QtWidgets.QWidget()
        self.QuotePanel.setObjectName('QuotePanel')
        self.CryptoStack.addWidget(self.QuotePanel)

        # input text file button
        self.QuoteTextInputPath = ''
        self.QuoteTextInputButton = QtWidgets.QPushButton(self.QuotePanel)
        self.QuoteTextInputButton.setObjectName('QuoteTextInputButton')
        self.QuoteTextInputButton.setGeometry(QtCore.QRect(20, 20, 120, 45))
        self.QuoteTextInputButton.setText('打开...')
        self.QuoteTextInputButton.setToolTip('点击选择文件')
        self.QuoteTextInputButton.setFont(font)
        self.QuoteTextInputButton.setStyleSheet(
            "QPushButton#QuoteTextInputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteTextInputButton.setFlat(True)

        # output text file button
        self.QuoteTextOutputPath = ''
        self.QuoteTextOutputButton = QtWidgets.QPushButton(self.QuotePanel)
        self.QuoteTextOutputButton.setObjectName('QuoteTextOutputButton')
        self.QuoteTextOutputButton.setGeometry(QtCore.QRect(260, 20, 120, 45))
        self.QuoteTextOutputButton.setText('另存为...')
        self.QuoteTextOutputButton.setToolTip('点击选择文件')
        self.QuoteTextOutputButton.setFont(font)
        self.QuoteTextOutputButton.setStyleSheet(
            "QPushButton#QuoteTextOutputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteTextOutputButton.setFlat(True)

        # eval support
        self.QuoteTextEvalCheckBox = QtWidgets.QCheckBox(
            '启用eval', self.QuotePanel)
        font.setFamily('文泉驿微米黑')
        self.QuoteTextEvalCheckBox.setGeometry(QtCore.QRect(450, 35, 120, 40))
        self.QuoteTextEvalCheckBox.setObjectName('QuoteTextEvalCheckBox')
        self.QuoteTextEvalCheckBox.setStyleSheet(
            'QCheckBox:unchecked{ border:none; color: white; }\
                QCheckBox:checked{ border:none; color: cyan; }')
        self.QuoteTextEvalCheckBox.setFont(font)

        # Quote Encode button
        self.QuoteEncodeButton = QtWidgets.QPushButton(self.QuotePanel)
        self.QuoteEncodeButton.setObjectName('QuoteEncodeButton')
        self.QuoteEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.QuoteEncodeButton.setText('编码')
        self.QuoteEncodeButton.setFont(font)
        self.QuoteEncodeButton.setStyleSheet(
            "QPushButton#QuoteEncodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteEncodeButton.setFlat(True)

        # input cipher file button
        self.QuoteCipherInputPath = ''
        self.QuoteCipherInputButton = QtWidgets.QPushButton(self.QuotePanel)
        self.QuoteCipherInputButton.setObjectName('QuoteCipherInputButton')
        self.QuoteCipherInputButton.setGeometry(
            QtCore.QRect(720, 20, 120, 45))
        self.QuoteCipherInputButton.setText('打开...')
        self.QuoteCipherInputButton.setToolTip('点击选择文件')
        self.QuoteCipherInputButton.setFont(font)
        self.QuoteCipherInputButton.setStyleSheet(
            "QPushButton#QuoteCipherInputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteCipherInputButton.setFlat(True)

        # output cipher file button
        self.QuoteCipherOutputPath = ''
        self.QuoteCipherOutputButton = QtWidgets.QPushButton(self.QuotePanel)
        self.QuoteCipherOutputButton.setObjectName('QuoteCipherOutputButton')
        self.QuoteCipherOutputButton.setGeometry(
            QtCore.QRect(960, 20, 120, 45))
        self.QuoteCipherOutputButton.setText('另存为...')
        self.QuoteCipherOutputButton.setToolTip('点击选择文件')
        self.QuoteCipherOutputButton.setFont(font)
        self.QuoteCipherOutputButton.setStyleSheet(
            "QPushButton#QuoteCipherOutputButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteCipherOutputButton.setFlat(True)

        # Quote Decode button
        self.QuoteDecodeButton = QtWidgets.QPushButton(self.QuotePanel)
        self.QuoteDecodeButton.setObjectName('QuoteDecodeButton')
        self.QuoteDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.QuoteDecodeButton.setText('解码')
        self.QuoteDecodeButton.setFont(font)
        self.QuoteDecodeButton.setStyleSheet(
            "QPushButton#QuoteDecodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.QuoteDecodeButton.setFlat(True)

        font.setFamily("Consolas")
        self.QuoteTextBox = QtWidgets.QTextEdit(self.QuotePanel)
        self.QuoteTextBox.setObjectName('QuoteTextBox')
        self.QuoteTextBox.setFont(font)
        self.QuoteTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.QuoteTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.QuoteTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.QuoteTextBox.setPlaceholderText('Quote - Printable\n这里写明文')
        self.QuoteTextBox.setAcceptDrops(True)
        self.QuoteTextBox.setAcceptRichText(False)

        self.QuoteCipherBox = QtWidgets.QTextEdit(self.QuotePanel)
        self.QuoteCipherBox.setObjectName('QuoteCipherBox')
        self.QuoteCipherBox.setFont(font)
        self.QuoteCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.QuoteCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.QuoteCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.QuoteCipherBox.setPlaceholderText('Quote - Printable\n这里写编码')
        self.QuoteCipherBox.setAcceptDrops(True)
        self.QuoteCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")
        # end quote panel

        # begin url panel
        self.UrlPanel = QtWidgets.QWidget()
        self.UrlPanel.setObjectName('UrlPanel')
        self.CryptoStack.addWidget(self.UrlPanel)

        # Url Encode button
        self.UrlEncodeButton = QtWidgets.QPushButton(self.UrlPanel)
        self.UrlEncodeButton.setObjectName('UrlEncodeButton')
        self.UrlEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.UrlEncodeButton.setText('编码')
        self.UrlEncodeButton.setFont(font)
        self.UrlEncodeButton.setStyleSheet(
            "QPushButton#UrlEncodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.UrlEncodeButton.setFlat(True)

        # Url Decode button
        self.UrlDecodeButton = QtWidgets.QPushButton(self.UrlPanel)
        self.UrlDecodeButton.setObjectName('UrlDecodeButton')
        self.UrlDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.UrlDecodeButton.setText('解码')
        self.UrlDecodeButton.setFont(font)
        self.UrlDecodeButton.setStyleSheet(
            "QPushButton#UrlDecodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.UrlDecodeButton.setFlat(True)

        # url table edit box and label
        self.UrlTableTips = QtWidgets.QLabel(self.UrlPanel)
        self.UrlTableTips.setObjectName('UrlTableTips')
        self.UrlTableTips.setText('编码表:')
        self.UrlTableTips.setFont(font)
        self.UrlTableTips.setStyleSheet('color: white;')
        self.UrlTableTips.setGeometry(QtCore.QRect(50, 20, 130, 45))
        self.UrlTableBox = QtWidgets.QLineEdit(self.UrlPanel)
        font.setFamily("Consolas")
        self.UrlTableBox.setFont(font)
        self.UrlTableBox.setStyleSheet('color: white;\
            border: 2px solid gray;\
            border-radius: 10px;\
            padding: 0 8px;\
            background: rgb(20, 20, 20);\
            selection-background-color: blue;')
        self.UrlTableBox.setObjectName('UrlTableBox')
        self.UrlTableBox.setGeometry(QtCore.QRect(150, 20, 100, 45))
        font.setFamily("文泉驿微米黑")

        font.setFamily("Consolas")
        self.UrlTextBox = QtWidgets.QTextEdit(self.UrlPanel)
        self.UrlTextBox.setObjectName('UrlTextBox')
        self.UrlTextBox.setFont(font)
        self.UrlTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.UrlTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.UrlTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.UrlTextBox.setPlaceholderText('Url Encode\n这里写明文')
        self.UrlTextBox.setAcceptDrops(True)
        self.UrlTextBox.setAcceptRichText(False)

        self.UrlCipherBox = QtWidgets.QTextEdit(self.UrlPanel)
        self.UrlCipherBox.setObjectName('UrlCipherBox')
        self.UrlCipherBox.setFont(font)
        self.UrlCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.UrlCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.UrlCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.UrlCipherBox.setPlaceholderText('Url Decode\n这里写编码')
        self.UrlCipherBox.setAcceptDrops(True)
        self.UrlCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")

        # end url panel

        # begin Hex panel
        self.HexPanel = QtWidgets.QWidget()
        self.HexPanel.setObjectName('HexPanel')
        self.CryptoStack.addWidget(self.HexPanel)

        # Hex Splits
        self.HexSplitTips = QtWidgets.QLabel(self.HexPanel)
        self.HexSplitTips.setObjectName('HexSplitTips')
        self.HexSplitTips.setText('分隔符:')
        self.HexSplitTips.setFont(font)
        self.HexSplitTips.setStyleSheet('color: white;')
        self.HexSplitTips.setGeometry(QtCore.QRect(50, 20, 130, 45))
        self.HexSplitBox = QtWidgets.QLineEdit(self.HexPanel)
        font.setFamily("Consolas")
        self.HexSplitBox.setFont(font)
        self.HexSplitBox.setStyleSheet('color: white;\
            border: 2px solid gray;\
            border-radius: 10px;\
            padding: 0 8px;\
            background: rgb(20, 20, 20);\
            selection-background-color: blue;')
        self.HexSplitBox.setObjectName('HexSplitBox')
        self.HexSplitBox.setGeometry(QtCore.QRect(150, 20, 100, 45))
        font.setFamily("文泉驿微米黑")

        # Hex Encode button
        self.HexEncodeButton = QtWidgets.QPushButton(self.HexPanel)
        self.HexEncodeButton.setObjectName('HexEncodeButton')
        self.HexEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.HexEncodeButton.setText('编码')
        self.HexEncodeButton.setFont(font)
        self.HexEncodeButton.setStyleSheet(
            "QPushButton#HexEncodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HexEncodeButton.setFlat(True)

        # Hex Decode button
        self.HexDecodeButton = QtWidgets.QPushButton(self.HexPanel)
        self.HexDecodeButton.setObjectName('HexDecodeButton')
        self.HexDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.HexDecodeButton.setText('解码')
        self.HexDecodeButton.setFont(font)
        self.HexDecodeButton.setStyleSheet(
            "QPushButton#HexDecodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HexDecodeButton.setFlat(True)

        font.setFamily("Consolas")
        self.HexTextBox = QtWidgets.QTextEdit(self.HexPanel)
        self.HexTextBox.setObjectName('HexTextBox')
        self.HexTextBox.setFont(font)
        self.HexTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.HexTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.HexTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.HexTextBox.setPlaceholderText('Hex Encode\n这里写明文')
        self.HexTextBox.setAcceptDrops(True)
        self.HexTextBox.setAcceptRichText(False)

        self.HexCipherBox = QtWidgets.QTextEdit(self.HexPanel)
        self.HexCipherBox.setObjectName('HexCipherBox')
        self.HexCipherBox.setFont(font)
        self.HexCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.HexCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.HexCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.HexCipherBox.setPlaceholderText('Hex Decode\n这里写编码')
        self.HexCipherBox.setAcceptDrops(True)
        self.HexCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")
        # end hex panel

        # begin HTML panel
        self.HTMLPanel = QtWidgets.QWidget()
        self.HTMLPanel.setObjectName('HTMLPanel')
        self.CryptoStack.addWidget(self.HTMLPanel)

        # HTML Encode button
        self.HTMLEncodeButton = QtWidgets.QPushButton(self.HTMLPanel)
        self.HTMLEncodeButton.setObjectName('HTMLEncodeButton')
        self.HTMLEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.HTMLEncodeButton.setText('编码')
        self.HTMLEncodeButton.setFont(font)
        self.HTMLEncodeButton.setStyleSheet(
            "QPushButton#HTMLEncodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HTMLEncodeButton.setFlat(True)

        # HTML Decode button
        self.HTMLDecodeButton = QtWidgets.QPushButton(self.HTMLPanel)
        self.HTMLDecodeButton.setObjectName('HTMLDecodeButton')
        self.HTMLDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.HTMLDecodeButton.setText('解码')
        self.HTMLDecodeButton.setFont(font)
        self.HTMLDecodeButton.setStyleSheet(
            "QPushButton#HTMLDecodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.HTMLDecodeButton.setFlat(True)

        font.setFamily("Consolas")
        self.HTMLTextBox = QtWidgets.QTextEdit(self.HTMLPanel)
        self.HTMLTextBox.setObjectName('HTMLTextBox')
        self.HTMLTextBox.setFont(font)
        self.HTMLTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.HTMLTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.HTMLTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.HTMLTextBox.setPlaceholderText('HTML Encode\n这里写明文')
        self.HTMLTextBox.setAcceptDrops(True)
        self.HTMLTextBox.setAcceptRichText(False)

        self.HTMLCipherBox = QtWidgets.QTextEdit(self.HTMLPanel)
        self.HTMLCipherBox.setObjectName('HTMLCipherBox')
        self.HTMLCipherBox.setFont(font)
        self.HTMLCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.HTMLCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.HTMLCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.HTMLCipherBox.setPlaceholderText('HTML Decode\n这里写编码')
        self.HTMLCipherBox.setAcceptDrops(True)
        self.HTMLCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")
        # end HTML panel

        # begin Escape panel
        self.EscapePanel = QtWidgets.QWidget()
        self.EscapePanel.setObjectName('EscapePanel')
        self.CryptoStack.addWidget(self.EscapePanel)

        # Escape Encode button
        self.EscapeEncodeButton = QtWidgets.QPushButton(self.EscapePanel)
        self.EscapeEncodeButton.setObjectName('EscapeEncodeButton')
        self.EscapeEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.EscapeEncodeButton.setText('编码')
        self.EscapeEncodeButton.setFont(font)
        self.EscapeEncodeButton.setStyleSheet(
            "QPushButton#EscapeEncodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.EscapeEncodeButton.setFlat(True)

        # Escape Decode button
        self.EscapeDecodeButton = QtWidgets.QPushButton(self.EscapePanel)
        self.EscapeDecodeButton.setObjectName('EscapeDecodeButton')
        self.EscapeDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.EscapeDecodeButton.setText('解码')
        self.EscapeDecodeButton.setFont(font)
        self.EscapeDecodeButton.setStyleSheet(
            "QPushButton#EscapeDecodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.EscapeDecodeButton.setFlat(True)

        font.setFamily("Consolas")
        self.EscapeTextBox = QtWidgets.QTextEdit(self.EscapePanel)
        self.EscapeTextBox.setObjectName('EscapeTextBox')
        self.EscapeTextBox.setFont(font)
        self.EscapeTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.EscapeTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.EscapeTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.EscapeTextBox.setPlaceholderText('Escape Encode\n这里写明文')
        self.EscapeTextBox.setAcceptDrops(True)
        self.EscapeTextBox.setAcceptRichText(False)

        self.EscapeCipherBox = QtWidgets.QTextEdit(self.EscapePanel)
        self.EscapeCipherBox.setObjectName('EscapeCipherBox')
        self.EscapeCipherBox.setFont(font)
        self.EscapeCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.EscapeCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.EscapeCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.EscapeCipherBox.setPlaceholderText('Escape Decode\n这里写编码')
        self.EscapeCipherBox.setAcceptDrops(True)
        self.EscapeCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")
        # end Escape panel

        # begin Tap panel
        self.TapPanel = QtWidgets.QWidget()
        self.TapPanel.setObjectName('TapPanel')
        self.CryptoStack.addWidget(self.TapPanel)

        # Tap Encode button
        self.TapEncodeButton = QtWidgets.QPushButton(self.TapPanel)
        self.TapEncodeButton.setObjectName('TapEncodeButton')
        self.TapEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.TapEncodeButton.setText('编码')
        self.TapEncodeButton.setFont(font)
        self.TapEncodeButton.setStyleSheet(
            "QPushButton#TapEncodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.TapEncodeButton.setFlat(True)

        # Tap Decode button
        self.TapDecodeButton = QtWidgets.QPushButton(self.TapPanel)
        self.TapDecodeButton.setObjectName('TapDecodeButton')
        self.TapDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.TapDecodeButton.setText('解码')
        self.TapDecodeButton.setFont(font)
        self.TapDecodeButton.setStyleSheet(
            "QPushButton#TapDecodeButton{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.TapDecodeButton.setFlat(True)

        font.setFamily("Consolas")
        self.TapTextBox = QtWidgets.QTextEdit(self.TapPanel)
        self.TapTextBox.setObjectName('TapTextBox')
        self.TapTextBox.setFont(font)
        self.TapTextBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.TapTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.TapTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.TapTextBox.setPlaceholderText('Tap Encode\n这里写明文')
        self.TapTextBox.setAcceptDrops(True)
        self.TapTextBox.setAcceptRichText(False)

        self.TapCipherBox = QtWidgets.QTextEdit(self.TapPanel)
        self.TapCipherBox.setObjectName('TapCipherBox')
        self.TapCipherBox.setFont(font)
        self.TapCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20)')
        self.TapCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.TapCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.TapCipherBox.setPlaceholderText('Tap Decode\n这里写编码')
        self.TapCipherBox.setAcceptDrops(True)
        self.TapCipherBox.setAcceptRichText(False)
        font.setFamily("文泉驿微米黑")
        # end Tap panel

        self.TypeStack.addWidget(self.CryptoPanel)

        # end Crypto panel

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
        MainWindow.setCentralWidget(self.centralwidget)

        # other process.
        self.retranslateUi(MainWindow)
        self.CloseButton.clicked.connect(MainWindow.close)
        self.MiniButton.clicked.connect(MainWindow.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.FileTempStackDelButton, self.CryptoButton)
        MainWindow.setTabOrder(self.CryptoButton, self.ReverseButton)
        MainWindow.setTabOrder(self.ReverseButton, self.WebButton)
        MainWindow.setTabOrder(self.WebButton, self.PwnButton)
        MainWindow.setTabOrder(self.PwnButton, self.MiscButton)
        MainWindow.setTabOrder(self.MiscButton, self.MiniButton)
        MainWindow.setTabOrder(self.MiniButton, self.CloseButton)
        MainWindow.setTabOrder(self.CloseButton, self.BaseButton)
        self.CryptoButton.clicked.connect(self.ChangeTypeStackCrypto)
        self.ReverseButton.clicked.connect(self.ChangeTypeStackReverse)
        self.MiscButton.clicked.connect(self.ChangeTypeStackMisc)
        self.WebButton.clicked.connect(self.ChangeTypeStackWeb)
        self.PwnButton.clicked.connect(self.ChangeTypeStackPwn)
        self.BaseButton.clicked.connect(self.ChangeCryptoBase)
        self.QuoteButton.clicked.connect(self.ChangeCryptoQuote)
        self.UrlButton.clicked.connect(self.ChangeCryptoUrl)
        self.HexButton.clicked.connect(self.ChangeCryptoHex)
        self.HTMLButton.clicked.connect(self.ChangeCryptoHTML)
        self.EscapeButton.clicked.connect(self.ChangeCryptoEscape)
        self.TapButton.clicked.connect(self.ChangeCryptoTap)
        self.Base16Button.clicked.connect(self.ChangeBase16)
        self.Base32Button.clicked.connect(self.ChangeBase32)
        self.Base64Button.clicked.connect(self.ChangeBase64)
        self.Base85Button.clicked.connect(self.ChangeBase85)
        self.Base85RFCButton.clicked.connect(self.ChangeBase85RFC)
        self.BaseEncButton.clicked.connect(self.BaseEnc)
        self.BaseDecButton.clicked.connect(self.BaseDec)
        self.QuoteEncodeButton.clicked.connect(self.QuoteEnc)
        self.QuoteDecodeButton.clicked.connect(self.QuoteDec)
        self.HexEncodeButton.clicked.connect(self.HexEncode)
        self.HexDecodeButton.clicked.connect(self.HexDecode)
        self.HTMLEncodeButton.clicked.connect(self.HTMLEncode)
        self.HTMLDecodeButton.clicked.connect(self.HTMLDecode)
        self.EscapeEncodeButton.clicked.connect(self.EscapeEncode)
        self.EscapeDecodeButton.clicked.connect(self.EscapeDecode)
        self.TapEncodeButton.clicked.connect(self.TapEncode)
        self.TapDecodeButton.clicked.connect(self.TapDecode)
        self.BaseTextInputButton.clicked.connect(self.BaseTextInputFunction)
        self.BaseCipherInputButton.clicked.connect(
            self.BaseCipherInputFunction)
        self.BaseTextOutputButton.clicked.connect(self.BaseTextOutputFunction)
        self.BaseCipherOutputButton.clicked.connect(
            self.BaseCipherOutputFunction)
        self.QuoteTextInputButton.clicked.connect(self.QuoteTextInputFunction)
        self.QuoteCipherInputButton.clicked.connect(
            self.QuoteCipherInputFunction)
        self.QuoteTextOutputButton.clicked.connect(
            self.QuoteTextOutputFunction)
        self.QuoteCipherOutputButton.clicked.connect(
            self.QuoteCipherOutputFunction)
        self.BaseEButton.clicked.connect(self.BaseEDecodeFunction)
        self.BaseTranslateButton.clicked.connect(self.BaseTranslateFunction)
        self.UrlEncodeButton.clicked.connect(self.UrlEncode)
        self.UrlDecodeButton.clicked.connect(self.UrlDecode)
        self.FileTempStack.doubleClicked.connect(self.FileStackCopy)
        self.FileTempStackDelButton.clicked.connect(self.DelFileTempStack)
        self.ChangeCryptoBase()
        self.ChangeBase64()
        self.center()

    # functions

    def DelFileTempStack(self):
        item = self.FileTempStack.currentItem()
        self.FileTempStack.takeItem(self.FileTempStack.row(item))

    def TapEncode(self):
        table = {'A': 11, 'B': 12, 'C': 13, 'D': 14, 'E': 15,
                 'F': 21, 'G': 22, 'H': 23, 'I': 24, 'J': 25,
                 'L': 31, 'M': 32, 'N': 33, 'O': 34, 'P': 35,
                 'Q': 41, 'R': 42, 'S': 43, 'T': 44, 'U': 45,
                 'V': 51, 'W': 52, 'X': 53, 'Y': 54, 'Z': 55,
                 'a': 11, 'b': 12, 'c': 13, 'd': 14, 'e': 15,
                 'f': 21, 'g': 22, 'h': 23, 'i': 24, 'j': 25,
                 'l': 31, 'm': 32, 'n': 33, 'o': 34, 'p': 35,
                 'q': 41, 'r': 42, 's': 43, 't': 44, 'u': 45,
                 'v': 51, 'w': 52, 'x': 53, 'y': 54, 'z': 55,
                 'K': 13, 'k': 13}
        text = self.TapTextBox.toPlainText()
        output = ''
        try:
            for i in text:
                output += str(table[i]) + ' '
            self.TapCipherBox.setText(output)
        except:
            self.TapCipherBox.setText('编码出现错误!')
        self.FileTempStack.addItem(self.TapCipherBox.toPlainText())

    def TapDecode(self):
        retable = [['A', 'B', '(C/K)', 'D', 'E'],
                   ['F', 'G', 'H', 'I', 'J'],
                   ['L', 'M', 'N', 'O', 'P'],
                   ['Q', 'R', 'S', 'T', 'U'],
                   ['V', 'W', 'X', 'Y', 'Z']]
        text = self.TapCipherBox.toPlainText()
        output = ''
        temp1 = ''
        temp2 = ''
        try:
            for i in text:
                if len(temp1) == 1 and len(temp2) == 1:
                    output += retable[int(temp1) - 1][int(temp2) - 1]
                    temp1 = ''
                    temp2 = ''
                if '1' <= i <= '5':
                    if len(temp1) == 1:
                        temp2 = i
                    else:
                        temp1 = i
            if len(temp1) == 1 and len(temp2) == 1:
                output += retable[int(temp1)][int(temp2)]
            self.TapTextBox.setText(output)
        except:
            self.TapTextBox.setText('解码出现错误!')
        self.FileTempStack.addItem(self.TapTextBox.toPlainText())

    def UrlEncode(self):
        text = self.UrlTextBox.toPlainText()
        try:
            self.UrlCipherBox.setText(
                parse.quote(text, encoding=self.UrlTableBox.text()))
        except:
            self.UrlCipherBox.setText('出现错误!')
        self.FileTempStack.addItem(self.UrlCipherBox.toPlainText())

    def UrlDecode(self):
        text = self.UrlCipherBox.toPlainText()
        try:
            self.UrlTextBox.setText(parse.unquote(
                text, encoding=self.UrlTableBox.text()))
        except:
            self.UrlTextBox.setText('出现错误!')
        self.FileTempStack.addItem(self.UrlTextBox.toPlainText())

    def HexEncode(self):
        text = self.HexTextBox.toPlainText()
        try:
            temp = self.char2hex(text).decode()
            j = 0
            output = ''
            for i in temp:
                if j % 2 == 0:
                    output += self.HexSplitBox.text()
                output += i
                j += 1
            self.HexCipherBox.setText(output)
        except:
            self.HexCipherBox.setText('编码时出现错误!')
        self.FileTempStack.addItem(self.HexCipherBox.toPlainText())

    def HexDecode(self):
        text = self.HexCipherBox.toPlainText()
        try:
            temp = []
            if self.HexSplitBox.text() != '':
                temp = text.split(self.HexSplitBox.text())
            else:
                temp = text.split()
            output = ''.join(temp)
            self.HexTextBox.setText(self.hex2char(output).decode())
        except:
            self.HexTextBox.setText('解码时出现错误!')
        self.FileTempStack.addItem(self.HexTextBox.toPlainText())

    def hex2char(self, data):
        output = binascii.unhexlify(data.encode())
        return output

    def char2hex(self, data):
        output = binascii.hexlify(data.encode())
        return output

    def EscapeEncode(self):
        try:
            self.EscapeCipherBox.setText(parse.quote(self.EscapeTextBox.toPlainText().encode(
                'unicode-escape')).replace('%5Cu', '%u'))
        except:
            self.EscapeCipherBox.setText('编码失败.')
        self.FileTempStack.addItem(self.EscapeCipherBox.toPlainText())

    def EscapeDecode(self):
        try:
            self.EscapeTextBox.setText(
                parse.unquote(self.EscapeCipherBox.toPlainText().replace('%u', '\\u').encode().decode('unicode-escape')))
        except:
            self.EscapeTextBox.setText('解码失败.')
        self.FileTempStack.addItem(self.EscapeTextBox.toPlainText())

    def HTMLEncode(self):
        text = self.HTMLTextBox.toPlainText()
        try:
            output = html.escape(text)
            self.HTMLCipherBox.setText(output)
        except:
            self.HTMLCipherBox.setText('编码时出现错误!')
        self.FileTempStack.addItem(self.HTMLCipherBox.toPlainText())

    def HTMLDecode(self):
        text = self.HTMLCipherBox.toPlainText()
        try:
            output = html.unescape(text)
            self.HTMLTextBox.setText(output)
        except:
            self.HTMLTextBox.setText('解码时出现错误!')
        self.FileTempStack.addItem(self.HTMLTextBox.toPlainText())

    def ChangeCryptoTap(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 7
        self.CryptoStack.setCurrentIndex(6)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoEscape(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 6
        self.CryptoStack.setCurrentIndex(5)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoHex(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 4
        self.CryptoStack.setCurrentIndex(3)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoHTML(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 5
        self.CryptoStack.setCurrentIndex(4)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoUrl(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 3
        self.CryptoStack.setCurrentIndex(2)
        self.UrlTableBox.setText('utf-8')
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def QuoteEnc(self):
        if self.QuoteTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(self.QuoteTextBox.toPlainText())
            except:
                self.QuoteCipherBox.setText(
                    '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
                return
        else:
            text = self.QuoteTextBox.toPlainText().encode()
        try:
            cipher = quopri.encodestring(text).decode()
        except:
            cipher = '编码时出现错误!'
        self.QuoteCipherBox.setText(cipher)
        self.FileTempStack.addItem(cipher)

    def QuoteDec(self):
        text = self.QuoteCipherBox.toPlainText()
        try:
            cipher = quopri.decodestring(text)
        except:
            self.QuoteTextBox.setText('解码时出现错误!')
            return
        try:
            self.QuoteTextBox.setText(cipher.decode())
        except:
            self.QuoteTextBox.setText(str(cipher))
        self.FileTempStack.addItem(self.QuoteTextBox.toPlainText())

    def ChangeCryptoBase(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 1
        self.CryptoStack.setCurrentIndex(0)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeCryptoQuote(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.CryptoChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        self.CryptoMode = 2
        self.CryptoStack.setCurrentIndex(1)
        animation.setEndValue(QtCore.QPoint(
            self.CryptoChooserBox[self.CryptoMode], 55))
        animation.setDuration(200)
        animation.start()

    def BaseEDecodeFunction(self):
        text = self.BaseCipherBox.toPlainText()
        lines = text.splitlines()
        aim = base64_ste(lines)
        self.BaseTextBox.setText(aim)
        self.FileTempStack.addItem(aim)

    def BaseTranslateFunction(self):
        text = self.BaseCipherBox.toPlainText()
        self.BaseCipherBox.setText(self.BaseTextBox.toPlainText())
        self.BaseTextBox.setText(text)

    def FileStackCopy(self):
        print(self.FileTempStack.selectedItems()[0].text())
        clipboard = QtGui.QGuiApplication.clipboard()
        clipboard.setText(self.FileTempStack.selectedItems()[0].text())

    def BaseTextInputFunction(self):
        self.BaseTextInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.BaseTextInputPath == "":
            return
        with open(self.BaseTextInputPath, 'rb') as inp:
            self.BaseTextBox.setText(str(inp.read()))
        self.BaseTextEvalCheckBox.setChecked(True)

    def BaseTextOutputFunction(self):
        self.BaseTextOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                  "保存文件",
                                                                                  '',
                                                                                  "All Files (*)")
        if self.BaseTextOutputPath == "":
            return
        if self.BaseTextBox.toPlainText()[0:2] == 'b\'':
            with open(self.BaseTextOutputPath, 'wb') as out:
                out.write(eval(self.BaseTextBox.toPlainText()))
        else:
            with open(self.BaseTextOutputPath, 'w') as out:
                out.write(self.BaseTextBox.toPlainText())

    def BaseCipherOutputFunction(self):
        self.BaseCipherOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                    "保存文件",
                                                                                    '',
                                                                                    "All Files (*)")
        if self.BaseCipherOutputPath == "":
            return
        with open(self.BaseCipherOutputPath, 'w') as out:
            out.write(self.BaseCipherBox.toPlainText())

    def BaseCipherInputFunction(self):
        self.BaseCipherInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.BaseCipherInputPath == "":
            return
        with open(self.BaseCipherInputPath, 'r') as inp:
            try:
                self.BaseCipherBox.setText(inp.read().decode())
            except:
                self.BaseCipherBox.setText('文件读取错误.')

    def QuoteTextInputFunction(self):
        self.QuoteTextInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.QuoteTextInputPath == "":
            return
        with open(self.QuoteTextInputPath, 'rb') as inp:
            self.QuoteTextBox.setText(str(inp.read()))
        self.QuoteTextEvalCheckBox.setChecked(True)

    def QuoteTextOutputFunction(self):
        self.QuoteTextOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                   "保存文件",
                                                                                   '',
                                                                                   "All Files (*)")
        if self.QuoteTextOutputPath == "":
            return
        if self.QuoteTextBox.toPlainText()[0:2] == 'b\'':
            with open(self.QuoteTextOutputPath, 'wb') as out:
                out.write(eval(self.QuoteTextBox.toPlainText()))
        else:
            with open(self.QuoteTextOutputPath, 'w') as out:
                out.write(self.QuoteTextBox.toPlainText())

    def QuoteCipherOutputFunction(self):
        self.QuoteCipherOutputPath, filetype = QtWidgets.QFileDialog.getSaveFileName(self,
                                                                                     "保存文件",
                                                                                     '',
                                                                                     "All Files (*)")
        if self.QuoteCipherOutputPath == "":
            return
        with open(self.QuoteCipherOutputPath, 'w') as out:
            out.write(self.QuoteCipherBox.toPlainText())

    def QuoteCipherInputFunction(self):
        self.QuoteCipherInputPath, filetype = \
            QtWidgets.QFileDialog.getOpenFileName(self,
                                                  "选取文件",
                                                  '',
                                                  "All Files (*);;Text Files (*.txt)")
        if self.QuoteCipherInputPath == "":
            return
        with open(self.QuoteCipherInputPath, 'r') as inp:
            try:
                self.QuoteCipherBox.setText(inp.read().decode())
            except:
                self.QuoteCipherBox.setText('文件读取错误.')

    def ChangeBase16(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 3
        self.BaseTableBox.setText(Base16StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase32(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 2
        self.BaseTableBox.setText(Base32StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase64(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 1
        self.BaseTableBox.setText(Base64StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase85(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 4
        self.BaseTableBox.setText(Base85StandardTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def ChangeBase85RFC(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.BaseChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        self.BaseMode = 5
        self.BaseTableBox.setText(Base85ReverseTable)
        animation.setEndValue(QtCore.QPoint(
            self.BaseChooserBox[self.BaseMode], 55))
        animation.setDuration(200)
        animation.start()

    def BaseEnc(self):
        if self.BaseMode == 1:
            self.Base64Enc()
        elif self.BaseMode == 2:
            self.Base32Enc()
        elif self.BaseMode == 3:
            self.Base16Enc()
        elif self.BaseMode == 4:
            self.Base85Enc()
        elif self.BaseMode == 5:
            self.Base85RFCEnc()
        else:
            pass
        self.FileTempStack.addItem(self.BaseCipherBox.toPlainText())

    def BaseDec(self):
        if self.BaseMode == 1:
            self.Base64Dec()
        elif self.BaseMode == 2:
            self.Base32Dec()
        elif self.BaseMode == 3:
            self.Base16Dec()
        elif self.BaseMode == 4:
            self.Base85Dec()
        elif self.BaseMode == 5:
            self.Base85RFCDec()
        else:
            pass
        self.FileTempStack.addItem(self.BaseTextBox.toPlainText())

    def CheckBaseCipher(self, x, newtable):
        if (self.BaseMode == 1):
            try:
                ChangeTableBase64Decode(x, newtable)
            except:
                return False
            return True
        elif (self.BaseMode == 2):
            try:
                ChangeTableBase32Decode(x, newtable)
            except:
                return False
            return True
        elif (self.BaseMode == 3):
            try:
                ChangeTableBase16Decode(x, newtable)
            except:
                return False
            return True
        elif (self.BaseMode == 4):
            try:
                ChangeTableBase85Decode(x, newtable)
            except:
                return False
        elif (self.BaseMode == 5):
            try:
                ChangeTableBase85RFCDecode(x, newtable)
            except:
                return False
            return True

    def Base64Dec(self):
        text = self.BaseCipherBox.toPlainText()
        padding = len(text) % 4
        if padding != 0:
            text += '=' * padding
        if self.CheckBase64Table(self.BaseTableBox.text()) == False or self.CheckBaseCipher(text, self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        self.BaseTextBox.setText(str(ChangeTableBase64Decode(
            text, self.BaseTableBox.text())))

    def Base32Dec(self):
        text = self.BaseCipherBox.toPlainText()
        padding = len(text) % 8
        if padding != 0:
            text += '=' * padding
        if self.CheckBase32Table(self.BaseTableBox.text()) == False or self.CheckBaseCipher(text, self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        self.BaseTextBox.setText(str(ChangeTableBase32Decode(
            text, self.BaseTableBox.text())))

    def Base16Dec(self):
        text = self.BaseCipherBox.toPlainText()
        if self.CheckBase16Table(self.BaseTableBox.text()) == False or self.CheckBaseCipher(text, self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        self.BaseTextBox.setText(str(ChangeTableBase16Decode(
            text, self.BaseTableBox.text())))

    def Base85Dec(self):
        text = self.BaseCipherBox.toPlainText()
        if self.CheckBase85Table(self.BaseTableBox.text()) == False or self.CheckBaseCipher(text, self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效或者要解码的字符串不是合法的编码字符串!!\nTable or Cipher Error!!!!!!!')
            return
        self.BaseTextBox.setText(str(ChangeTableBase85Decode(
            text, self.BaseTableBox.text())))

    def Base85RFCDec(self):
        text = self.BaseCipherBox.toPlainText()
        try:
            self.BaseTextBox.setText(str(ChangeTableBase85RFCDecode(
                text, self.BaseTableBox.text())))
        except:
            self.BaseTextBox.setText('解码失败.')

    def CheckBase64Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 64:
            return False
        return True

    def Base64Enc(self):
        text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                self.BaseCipherBox.setText(
                    '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase64Table(self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效!!\nTable Error!!!!!!!')
            return
        self.BaseCipherBox.setText(ChangeTableBase64Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def CheckBase32Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 32:
            return False
        return True

    def Base32Enc(self):
        text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                self.BaseCipherBox.setText(
                    '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase32Table(self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效!!\nTable Error!!!!!!!')
            return
        self.BaseCipherBox.setText(ChangeTableBase32Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def CheckBase16Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 16:
            return False
        return True

    def Base16Enc(self):
        text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                self.BaseCipherBox.setText(
                    '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase16Table(self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效!!\nTable Error!!!!!!!')
            return
        self.BaseCipherBox.setText(ChangeTableBase16Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def CheckBase85Table(self, x):
        checkx = set(list(x))
        if len(checkx) != 85:
            return False
        return True

    def CheckBase85RFCTable(self, x):
        checkx = set(list(x))
        if len(checkx) != 85:
            return False
        return True

    def Base85Enc(self):
        text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                self.BaseCipherBox.setText(
                    '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase85Table(self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效!!\nTable Error!!!!!!!')
            return
        self.BaseCipherBox.setText(ChangeTableBase85Encode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def Base85RFCEnc(self):
        text = self.BaseTextBox.toPlainText()
        if self.BaseTextEvalCheckBox.isChecked() == True:
            try:
                text = eval(text)
            except:
                self.BaseCipherBox.setText(
                    '输入不是有效的Python语句! eval()执行错误!\nInvalid Python expression! eval() Failed!')
                return
        if self.CheckBase85RFCTable(self.BaseTableBox.text()) == False:
            self.BaseTextBox.setText(
                '编码表无效!!\nTable Error!!!!!!!')
            return
        self.BaseCipherBox.setText(ChangeTableBase85RFCEncode(
            text, self.BaseTableBox.text(), self.BaseTextEvalCheckBox.isChecked()))

    def ChangeTypeStackCrypto(self):
        '''改变类型控件组 密码学'''
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.TypeChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 3
        self.TypeStack.setCurrentIndex(self.TypeMode - 1)
        animation.setEndValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackReverse(self):
        '''改变类型控件组 逆向'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 1
        self.TypeStack.setCurrentIndex(self.TypeMode - 1)
        animation.setEndValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackWeb(self):
        '''改变类型控件组 web'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 2
        self.TypeStack.setCurrentIndex(self.TypeMode - 1)
        animation.setEndValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackMisc(self):
        '''改变类型控件组 杂项'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 5
        self.TypeStack.setCurrentIndex(self.TypeMode - 1)
        animation.setEndValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        animation.setDuration(200)
        animation.start()

    def ChangeTypeStackPwn(self):
        '''改变类型控件组 pwn'''
        animation = Qt.QPropertyAnimation(self.TypeChooser, b'pos', self)
        animation.setStartValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
        self.TypeMode = 4
        self.TypeStack.setCurrentIndex(self.TypeMode - 1)
        animation.setEndValue(QtCore.QPoint(
            20, self.TypeChooserBox[self.TypeMode]))
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
