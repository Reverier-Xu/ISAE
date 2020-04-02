from PyQt5 import QtCore, QtWidgets, QtGui, Qt
from CryptoPanel.RSAModule.ui_RSAModule import ui_RSAPanel
from CryptoPanel.RSAModule.RSAModuleUtils import *
from ui_Widgets.ErrorWin import errorInfo


class RSAPanel(ui_RSAPanel):
    def __init__(self):
        super(RSAPanel, self).__init__()
        self.epqButton.clicked.connect(self.Changeepq)
        self.dnButton.clicked.connect(self.Changeedn)
        self.dpdqpqButton.clicked.connect(self.Changedpdqpq)
        self.edpnButton.clicked.connect(self.Changeedpn)
        # self.RSAEncodeButton.clicked.connect(self.RSAEncode)
        # self.RSADecodeButton.clicked.connect(self.RSADecode)
        # self.RSACipherBox.textChanged.connect(self.setFontColorCipher)
        # self.RSATextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.RSACipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.RSATextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def Changeepq(self):
        try:
            animation = Qt.QPropertyAnimation(self)
            animation.setTargetObject(self.RSAChooser)
            animation.setPropertyName(b'pos')
            animation.setStartValue(QtCore.QPoint(
                self.RSAChooserBox[self.RSAMode], 55))
            self.RSAMode = 1

            animation.setEndValue(QtCore.QPoint(
                self.RSAChooserBox[self.RSAMode], 55))
            animation.setDuration(200)
            animation.start()
        except Exception as e:
            print(str(e))

    def Changeedn(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 2
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()

    def Changedpdqpq(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 3
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()

    def Changeedpn(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.RSAChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        self.RSAMode = 4
        animation.setEndValue(QtCore.QPoint(
            self.RSAChooserBox[self.RSAMode], 55))
        animation.setDuration(200)
        animation.start()
