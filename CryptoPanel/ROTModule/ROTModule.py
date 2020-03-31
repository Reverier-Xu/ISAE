from PyQt5 import QtCore
from PyQt5 import Qt

from CryptoPanel.ROTModule.ui_ROTModule import ui_ROTPanel
from CryptoPanel.ROTModule.ROTModuleUtils import *


class ROTPanel(ui_ROTPanel):
    def __init__(self):
        super(ROTPanel, self).__init__()
        self.ROT13Button.clicked.connect(self.ChangeROT13)
        self.ROT47Button.clicked.connect(self.ChangeROT47)
        self.ROTEncodeButton.clicked.connect(self.ROTEncode)

    def ChangeROT13(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.ROTChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.ROTChooserBox[self.ROTMode], 65))
        self.ROTMode = 1
        animation.setEndValue(QtCore.QPoint(
            self.ROTChooserBox[self.ROTMode], 65))
        animation.setDuration(200)
        animation.start()

    def ChangeROT47(self):
        animation = Qt.QPropertyAnimation(self)
        animation.setTargetObject(self.ROTChooser)
        animation.setPropertyName(b'pos')
        animation.setStartValue(QtCore.QPoint(
            self.ROTChooserBox[self.ROTMode], 65))
        self.ROTMode = 2
        animation.setEndValue(QtCore.QPoint(
            self.ROTChooserBox[self.ROTMode], 65))
        animation.setDuration(200)
        animation.start()

    def ROTEncode(self):
        text = self.ROTTextBox.toPlainText()
        if self.ROTMode == 1:
            output = ROT13(text)
        else:
            output = ROT47(text)
        self.ROTCipherBox.setText(output)
