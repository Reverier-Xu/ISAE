from ui_Widgets import uni_Widget

from CryptoPanel.ROTModule.ui_ROTModule import ui_ROTPanel
from CryptoPanel.ROTModule.ROTModuleUtils import *


class ROTPanel(ui_ROTPanel):
    def __init__(self):
        super(ROTPanel, self).__init__()
        self.ROT13Button.clicked.connect(self.ChangeROT13)
        self.ROT47Button.clicked.connect(self.ChangeROT47)
        self.ROTEncodeButton.clicked.connect(self.ROTEncode)
        self.ChangeROT13()

    def ChangeROT13(self):
        self.ROTMode = 1
        self.ROT13Button.setStyleSheet(uni_Widget.ButtonStyleSelected)
        self.ROT47Button.setStyleSheet(uni_Widget.ButtonStyleNormal)

    def ChangeROT47(self):
        self.ROTMode = 2
        self.ROT47Button.setStyleSheet(uni_Widget.ButtonStyleSelected)
        self.ROT13Button.setStyleSheet(uni_Widget.ButtonStyleNormal)

    def ROTEncode(self):
        text = self.ROTTextBox.toPlainText()
        if self.ROTMode == 1:
            output = ROT13(text)
        else:
            output = ROT47(text)
        self.ROTCipherBox.setText(output)
