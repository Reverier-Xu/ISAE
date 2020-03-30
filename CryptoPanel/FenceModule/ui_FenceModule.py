from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_FencePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_FencePanel, self).__init__()

        # Fence Encrypt button
        self.FenceEncryptButton = uni_Widget.ICTFEButton(self)
        self.FenceEncryptButton.setObjectName('FenceEncryptButton')
        self.FenceEncryptButton.setGeometry(QtCore.QRect(580, 20, 120, 45))
        self.FenceEncryptButton.setText('加密')

        # Fence Disp edit box and label
        self.FenceDispTips = uni_Widget.ICTFELabel(self)
        self.FenceDispTips.setObjectName('FenceDispTips')
        self.FenceDispTips.setText('每组字数:')
        self.FenceDispTips.setGeometry(QtCore.QRect(50, 20, 130, 45))

        self.FenceDispBox = uni_Widget.ICTFELineBox(self)
        self.FenceDispBox.setObjectName('FenceDispBox')
        self.FenceDispBox.setGeometry(QtCore.QRect(150, 20, 100, 45))

        # Fence Decrypt button
        self.FenceDecryptButton = uni_Widget.ICTFEButton(self)
        self.FenceDecryptButton.setObjectName('FenceDecryptButton')
        self.FenceDecryptButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.FenceDecryptButton.setText('解密')

        self.FenceTextBox = uni_Widget.ICTFETextBox(self)
        self.FenceTextBox.setObjectName('FenceTextBox')
        self.FenceTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.FenceTextBox.setPlaceholderText('Fence Encrypt\n这里写明文')

        self.FenceCipherBox = uni_Widget.ICTFETextBox(self)
        self.FenceCipherBox.setObjectName('FenceCipherBox')
        self.FenceCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.FenceCipherBox.setPlaceholderText('Fence Decrypt\n这里写编码')
        # end Fence panel