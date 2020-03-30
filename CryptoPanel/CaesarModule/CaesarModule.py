from PyQt5 import QtCore, QtWidgets, QtGui
from CryptoPanel.CaesarModule.ui_CaesarModule import ui_CaesarPanel
from CryptoPanel.CaesarModule.CaesarModuleUtils import *


class CaesarPanel(ui_CaesarPanel):
    def __init__(self):
        super(CaesarPanel, self).__init__()
        self.CaesarEncryptButton.clicked.connect(self.CaesarEncrypt)
        self.CaesarDecryptButton.clicked.connect(self.CaesarDecrypt)
        self.CaesarCipherBox.textChanged.connect(self.setFontColorCipher)
        self.CaesarTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.CaesarCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.CaesarTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def CaesarEncrypt(self):
        try:
            disp = int(self.CaesarDispBox.text())
        except:
            self.CaesarDisprBox.setText('位移输入错误！')
        self.CaesarCipherBox.setText(CaesarEncrypt(
                self.CaesarTextBox.toPlainText(), disp))

    def CaesarDecrypt(self):
        try:
            disp = int(self.CaesarDispBox.text())
        except:
            self.CaesarDisprBox.setText('位移输入错误！')
        self.CaesarTextBox.setText(CaesarDecrypt(
                self.CaesarCipherBox.toPlainText(), disp))
