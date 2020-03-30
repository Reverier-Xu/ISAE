from PyQt5 import QtGui
from CryptoPanel.FenceModule.ui_FenceModule import ui_FencePanel
from CryptoPanel.FenceModule.FenceModuleUtils import *
from ui_Widgets import ErrorWin


class FencePanel(ui_FencePanel):
    def __init__(self):
        super(FencePanel, self).__init__()
        self.FenceEncryptButton.clicked.connect(self.FenceEncrypt)
        self.FenceDecryptButton.clicked.connect(self.FenceDecrypt)
        self.FenceCipherBox.textChanged.connect(self.setFontColorCipher)
        self.FenceTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.FenceCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.FenceTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def FenceEncrypt(self):
        try:
            disp = int(self.FenceDispBox.text())
            self.FenceCipherBox.setText(FenceEncrypt(
                self.FenceTextBox.toPlainText(), disp))
        except:
            self.FenceDispBox.setText('0')
            ErrorWin.errorInfo(self, '输入的位移并非纯整数！')
            

    def FenceDecrypt(self):
        try:
            disp = int(self.FenceDispBox.text())
            self.FenceTextBox.setText(FenceDecrypt(
                self.FenceCipherBox.toPlainText(), disp))
        except:
            self.FenceDispBox.setText('0')
            ErrorWin.errorInfo(self, '输入的位移并非纯整数！')        
