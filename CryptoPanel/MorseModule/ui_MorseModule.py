from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_MorsePanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_MorsePanel, self).__init__()

        # Morse Encode button
        self.MorseEncodeButton = uni_Widget.ICTFEButton(self)
        self.MorseEncodeButton.setObjectName('MorseEncodeButton')
        self.MorseEncodeButton.setGeometry(QtCore.QRect(580, 20, 120, 45))
        self.MorseEncodeButton.setText('编码')

        # Morse Spilt edit box and label
        self.MorseSpiltTips = uni_Widget.ICTFELabel(self)
        self.MorseSpiltTips.setObjectName('MorseSpiltTips')
        self.MorseSpiltTips.setText('分隔符:')
        self.MorseSpiltTips.setGeometry(QtCore.QRect(50, 20, 130, 45))

        self.MorseSpiltBox = uni_Widget.ICTFELineBox(self)
        self.MorseSpiltBox.setObjectName('MorseSpiltBox')
        self.MorseSpiltBox.setGeometry(QtCore.QRect(150, 20, 100, 45))

        self.MorseChineseCheckBox = uni_Widget.ICTFECheckBox(self)
        self.MorseChineseCheckBox.setObjectName('MorseChineseCheckBox')
        self.MorseChineseCheckBox.setGeometry(QtCore.QRect(260, 20, 100, 45))
        self.MorseChineseCheckBox.setText('中文')

        # Morse Decode button
        self.MorseDecodeButton = uni_Widget.ICTFEButton(self)
        self.MorseDecodeButton.setObjectName('MorseDecodeButton')
        self.MorseDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.MorseDecodeButton.setText('解码')

        self.MorseTextBox = uni_Widget.ICTFETextBox(self)
        self.MorseTextBox.setObjectName('MorseTextBox')
        self.MorseTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.MorseTextBox.setPlaceholderText('Morse Encode\n这里写明文')

        self.MorseCipherBox = uni_Widget.ICTFETextBox(self)
        self.MorseCipherBox.setObjectName('MorseCipherBox')
        self.MorseCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.MorseCipherBox.setPlaceholderText('Morse Decode\n这里写编码')
        # end Morse panel