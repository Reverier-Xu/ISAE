from PyQt5 import QtGui
from CryptoPanel.PawnshopModule.ui_PawnshopModule import ui_PawnshopPanel
from CryptoPanel.PawnshopModule.PawnshopModuleUtils import *
from ui_Widgets import ErrorWin


class PawnshopPanel(ui_PawnshopPanel):
    def __init__(self):
        super(PawnshopPanel, self).__init__()
        self.PawnshopEncryptButton.clicked.connect(self.PawnshopEncrypt)
        self.PawnshopDecryptButton.clicked.connect(self.PawnshopDecrypt)
        self.PawnshopCipherBox.textChanged.connect(self.setFontColorCipher)
        self.PawnshopTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.PawnshopCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.PawnshopTextBox.setTextColor(QtGui.QColor(200, 200, 200))            

    def PawnshopDecrypt(self):
        self.PawnshopCipherBox.setText(PawnshopDecrypt(
            self.PawnshopTextBox.toPlainText()))      
