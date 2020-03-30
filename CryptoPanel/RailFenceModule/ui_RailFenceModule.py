from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_RailFencePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_RailFencePanel, self).__init__()

        # RailFence Encrypt button
        self.RailFenceEncryptButton = uni_Widget.ICTFEButton(self)
        self.RailFenceEncryptButton.setObjectName('RailFenceEncryptButton')
        self.RailFenceEncryptButton.setGeometry(QtCore.QRect(580, 20, 120, 45))
        self.RailFenceEncryptButton.setText('加密')

        # RailFence Div edit box and label
        self.RailFenceDivTips = uni_Widget.ICTFELabel(self)
        self.RailFenceDivTips.setObjectName('RailFenceDivTips')
        self.RailFenceDivTips.setText('每组字数:')
        self.RailFenceDivTips.setGeometry(QtCore.QRect(50, 20, 130, 45))

        self.RailFenceDivBox = uni_Widget.ICTFELineBox(self)
        self.RailFenceDivBox.setObjectName('RailFenceDivBox')
        self.RailFenceDivBox.setGeometry(QtCore.QRect(150, 20, 100, 45))

        # RailFence Decrypt button
        self.RailFenceDecryptButton = uni_Widget.ICTFEButton(self)
        self.RailFenceDecryptButton.setObjectName('RailFenceDecryptButton')
        self.RailFenceDecryptButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.RailFenceDecryptButton.setText('解密')

        self.RailFenceTextBox = uni_Widget.ICTFETextBox(self)
        self.RailFenceTextBox.setObjectName('RailFenceTextBox')
        self.RailFenceTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.RailFenceTextBox.setPlaceholderText('RailFence Encrypt\n这里写明文')

        self.RailFenceCipherBox = uni_Widget.ICTFETextBox(self)
        self.RailFenceCipherBox.setObjectName('RailFenceCipherBox')
        self.RailFenceCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.RailFenceCipherBox.setPlaceholderText('RailFence Decrypt\n这里写编码')
        # end RailFence panel