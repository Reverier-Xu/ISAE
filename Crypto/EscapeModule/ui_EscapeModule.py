from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_EscapePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_EscapePanel, self).__init__()

        # Escape Encode button
        self.EscapeEncodeButton = uni_Widget.ICTFEButton(self)
        self.EscapeEncodeButton.setObjectName('EscapeEncodeButton')
        self.EscapeEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.EscapeEncodeButton.setText('编码')

        # Escape Decode button
        self.EscapeDecodeButton = uni_Widget.ICTFEButton(self)
        self.EscapeDecodeButton.setObjectName('EscapeDecodeButton')
        self.EscapeDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.EscapeDecodeButton.setText('解码')

        self.EscapeTextBox = uni_Widget.ICTFETextBox(self)
        self.EscapeTextBox.setObjectName('EscapeTextBox')
        self.EscapeTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.EscapeTextBox.setPlaceholderText('Escape Encode\n这里写明文')

        self.EscapeCipherBox = uni_Widget.ICTFETextBox(self)
        self.EscapeCipherBox.setObjectName('EscapeCipherBox')
        self.EscapeCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.EscapeCipherBox.setPlaceholderText('Escape Decode\n这里写编码')
        # end Escape panel
