from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_HexPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_HexPanel, self).__init__()

        self.HexSplitTips = uni_Widget.ICTFELabel(self)
        self.HexSplitTips.setObjectName('HexSplitTips')
        self.HexSplitTips.setText('分隔符:')
        self.HexSplitTips.setGeometry(QtCore.QRect(50, 20, 130, 45))

        self.HexSplitBox = uni_Widget.ICTFELineBox(self)
        self.HexSplitBox.setObjectName('HexSplitBox')
        self.HexSplitBox.setGeometry(QtCore.QRect(150, 20, 100, 45))

        # Hex Encode button
        self.HexEncodeButton = uni_Widget.ICTFEButton(self)
        self.HexEncodeButton.setObjectName('HexEncodeButton')
        self.HexEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.HexEncodeButton.setText('编码')

        # Hex Decode button
        self.HexDecodeButton = uni_Widget.ICTFEButton(self)
        self.HexDecodeButton.setObjectName('HexDecodeButton')
        self.HexDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.HexDecodeButton.setText('解码')

        self.HexTextBox = uni_Widget.ICTFETextBox(self)
        self.HexTextBox.setObjectName('HexTextBox')
        self.HexTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.HexTextBox.setPlaceholderText('Hex Encode\n这里写明文')

        self.HexCipherBox = uni_Widget.ICTFETextBox(self)
        self.HexCipherBox.setObjectName('HexCipherBox')
        self.HexCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.HexCipherBox.setPlaceholderText('Hex Decode\n这里写编码')
        # end hex panel
