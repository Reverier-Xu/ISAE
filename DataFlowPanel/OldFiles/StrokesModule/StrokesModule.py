from PyQt5 import QtGui
from DataFlowPanel.StrokesModule.ui_StrokesModule import ui_StrokesPanel
from DataFlowPanel.StrokesModule.StrokesModuleUtils import *
from ui_Widgets import ErrorWin


class StrokesPanel(ui_StrokesPanel):
    def __init__(self):
        super(StrokesPanel, self).__init__()
        self.StrokesDecryptButton.clicked.connect(self.StrokesDecrypt)
        self.StrokesCipherBox.textChanged.connect(self.setFontColorCipher)
        self.StrokesTextBox.textChanged.connect(self.setFontColorText)

    def setFontColorCipher(self):
        self.StrokesCipherBox.setTextColor(QtGui.QColor(200, 200, 200))

    def setFontColorText(self):
        self.StrokesTextBox.setTextColor(QtGui.QColor(200, 200, 200))

    def StrokesDecrypt(self):
        self.StrokesCipherBox.setText(StrokesDecrypt(
            self.StrokesTextBox.toPlainText()))
