# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ICTFE.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets, Qt
import resource
from basecom import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):

        # some varibles
        self.TypeMode = 0
        self.BaseMode = 1

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
        self.FileTempStackTip.setGeometry(QtCore.QRect(38, 630, 120, 30))
        self.FileTempStackTip.setObjectName('FileTempStackTip')
        self.FileTempStackTip.setStyleSheet('#FileTempStackTip{color: white;}')
        self.FileTempStackTip.setText('暂存池')
        self.FileTempStackTip.setFont(font)
        self.FileTempStack = QtWidgets.QListWidget(self.centralwidget)
        self.FileTempStack.setGeometry(QtCore.QRect(20, 670, 120, 200))
        self.FileTempStack.setObjectName('FileTempStack')
        self.FileTempStack.setStyleSheet(
            '#FileTempStack{background-color: rgb(20,20,20)}')

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

        # Base Button
        self.BaseButton = QtWidgets.QPushButton(self.CryptoPanel)
        self.BaseButton.setGeometry(QtCore.QRect(20, 20, 120, 45))
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
        self.BaseChooserBox = [0, 10, 140, 270, 400]
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
        self.Base85Button.setText('Base85')
        self.Base85Button.setFont(font)
        self.Base85Button.setStyleSheet(
            "QPushButton#Base85Button{background-color:rgb(40, 40, 40);color:rgb(200,200,200);border-width:1px;border-color:rgb(50,50,50);}")
        self.Base85Button.setFlat(True)

        self.BaseEButton = QtWidgets.QPushButton(self.BasePanel)
        self.BaseEButton.setObjectName('BaseEButton')
        self.BaseEButton.setGeometry(QtCore.QRect(1180, 10, 200, 45))
        self.BaseEButton.setText('Base隐写提取')
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
        self.BaseTextInputFlag = False
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
        self.BaseTextOutputFlag = False
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
        self.BaseCipherInputFlag = False
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
        self.BaseCipherOutputFlag = False
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
        self.BaseTextBox = QtWidgets.QTextEdit(self.BasePanel)
        self.BaseTextBox.setObjectName('BaseTextBox')
        self.BaseTextBox.setFont(font)
        self.BaseTextBox.setStyleSheet(
            'background-color: rgb(20,20,20);')
        self.BaseTextBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.BaseTextBox.setGeometry(QtCore.QRect(20, 180, 680, 430))
        self.BaseTextBox.setPlaceholderText('这里写明文')

        self.BaseCipherBox = QtWidgets.QTextEdit(self.BasePanel)
        self.BaseCipherBox.setObjectName('BaseTextBox')
        self.BaseCipherBox.setFont(font)
        self.BaseCipherBox.setStyleSheet(
            'background-color: rgb(20,20,20);')
        self.BaseCipherBox.setTextColor(QtGui.QColor(200, 200, 200))
        self.BaseCipherBox.setGeometry(QtCore.QRect(720, 180, 680, 430))
        self.BaseCipherBox.setPlaceholderText('这里写编码')

        # end base panel
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
        self.Base16Button.clicked.connect(self.ChangeBase16)
        self.Base32Button.clicked.connect(self.ChangeBase32)
        self.Base64Button.clicked.connect(self.ChangeBase64)
        self.Base85Button.clicked.connect(self.ChangeBase85)
        self.BaseEncButton.clicked.connect(self.BaseEnc)
        self.BaseDecButton.clicked.connect(self.BaseDec)
        self.BaseTextInputButton.clicked.connect(self.BaseTextInputFunction)
        self.BaseCipherInputButton.clicked.connect(
            self.BaseCipherInputFunction)
        self.BaseTextOutputButton.clicked.connect(self.BaseTextOutputFunction)
        self.BaseCipherOutputButton.clicked.connect(
            self.BaseCipherOutputFunction)
        self.FileTempStack.doubleClicked.connect(self.FileStackCopy)
        self.ChangeBase64()
        self.center()

    # functions
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

    def BaseEnc(self):
        if self.BaseMode == 1:
            self.Base64Enc()
        elif self.BaseMode == 2:
            self.Base32Enc()
        elif self.BaseMode == 3:
            self.Base16Enc()
        elif self.BaseMode == 4:
            self.Base85Enc()
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
