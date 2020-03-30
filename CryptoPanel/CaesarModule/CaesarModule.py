from PyQt5 import QtGui
from CryptoPanel.CaesarModule.ui_CaesarModule import ui_CaesarPanel
from CryptoPanel.CaesarModule.CaesarModuleUtils import *
from ui_Widgets import ErrorWin


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
            self.CaesarCipherBox.setText(CaesarEncrypt(
                self.CaesarTextBox.toPlainText(), disp))
        except:
            self.CaesarDispBox.setText('0')
            ErrorWin.errorInfo(self, '输入的位移并非纯整数！')
            

    def CaesarDecrypt(self):
        try:
            disp = int(self.CaesarDispBox.text())
            self.CaesarTextBox.setText(CaesarDecrypt(
                self.CaesarCipherBox.toPlainText(), disp))
        except:
            self.CaesarDispBox.setText('0')
            ErrorWin.errorInfo(self, '输入的位移并非纯整数！')        
