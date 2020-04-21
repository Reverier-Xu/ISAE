from PyQt5 import QtGui
from DataFlowPanel.RailFenceModule.ui_RailFenceModule import ui_RailFencePanel
from DataFlowPanel.RailFenceModule.RailFenceModuleUtils import *
from ui_Widgets import ErrorWin


class RailFencePanel(ui_RailFencePanel):
    def __init__(self):
        super(RailFencePanel, self).__init__()
        self.RailFenceEncryptButton.clicked.connect(self.RailFenceEncrypt)
        self.RailFenceDecryptButton.clicked.connect(self.RailFenceDecrypt)
        self.RailFenceCipherBox.textChanged.connect(self.setFontColorCipher)
        self.RailFenceTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.RailFenceCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.RailFenceTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def RailFenceEncrypt(self):
        try:
            div = int(self.RailFenceDivBox.text())
            if div < 1:
                ErrorWin.errorInfo(self, '输入的数字小于1！')
                return
            self.RailFenceCipherBox.setText(RailFenceEncrypt(
                self.RailFenceTextBox.toPlainText(), div))
        except:
            self.RailFenceDivBox.setText('2')
            ErrorWin.errorInfo(self, '输入的分组数字并非纯整数！')

    def RailFenceDecrypt(self):
        try:
            div = int(self.RailFenceDivBox.text())
            if div < 1:
                ErrorWin.errorInfo(self, '输入的数字小于1！')
                return
            self.RailFenceTextBox.setText(RailFenceDecrypt(
                self.RailFenceCipherBox.toPlainText(), div))
        except:
            self.RailFenceDivBox.setText('2')
            ErrorWin.errorInfo(self, '输入的分组数字并非纯整数！')
