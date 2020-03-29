from PyQt5 import QtWidgets, QtCore, QtGui
from ui_Widgets import uni_Widget

class ui_TapPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_TapPanel, self).__init__()

        # Tap Encode button
        self.TapEncodeButton = uni_Widget.ICTFEButton(self)
        self.TapEncodeButton.setObjectName('TapEncodeButton')
        self.TapEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.TapEncodeButton.setText('编码')

        # Tap Decode button
        self.TapDecodeButton = uni_Widget.ICTFEButton(self)
        self.TapDecodeButton.setObjectName('TapDecodeButton')
        self.TapDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.TapDecodeButton.setText('解码')

        self.TapTextBox = uni_Widget.ICTFETextBox(self)
        self.TapTextBox.setObjectName('TapTextBox')
        self.TapTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.TapTextBox.setPlaceholderText('Tap Encode\n这里写明文')

        self.TapCipherBox = uni_Widget.ICTFETextBox(self)
        self.TapCipherBox.setObjectName('TapCipherBox')
        self.TapCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.TapCipherBox.setPlaceholderText('Tap Decode\n这里写编码')
        # end Tap panel
