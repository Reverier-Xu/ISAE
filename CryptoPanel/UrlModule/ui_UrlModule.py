from PyQt5 import QtCore, QtGui, QtWidgets
from ui_Widgets import uni_Widget


class ui_UrlPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_UrlPanel, self).__init__()

        # Url Encode button
        self.UrlEncodeButton = uni_Widget.ICTFEButton(self)
        self.UrlEncodeButton.setObjectName('UrlEncodeButton')
        self.UrlEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.UrlEncodeButton.setText('编码')

        # Url Decode button
        self.UrlDecodeButton = uni_Widget.ICTFEButton(self)
        self.UrlDecodeButton.setObjectName('UrlDecodeButton')
        self.UrlDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.UrlDecodeButton.setText('解码')

        # url table edit box and label
        self.UrlTableTips = uni_Widget.ICTFELabel(self)
        self.UrlTableTips.setObjectName('UrlTableTips')
        self.UrlTableTips.setText('编码表:')
        self.UrlTableTips.setGeometry(QtCore.QRect(50, 20, 130, 45))

        self.UrlTableBox = uni_Widget.ICTFELineBox(self)
        self.UrlTableBox.setObjectName('UrlTableBox')
        self.UrlTableBox.setGeometry(QtCore.QRect(150, 20, 100, 45))

        self.AllCheckBox = uni_Widget.ICTFECheckBox(self)
        self.AllCheckBox.setObjectName('AllCheckBox')
        self.AllCheckBox.setText('All')
        self.AllCheckBox.setGeometry(QtCore.QRect(270, 20, 100, 45))

        self.UrlTextBox = uni_Widget.ICTFETextBox(self)
        self.UrlTextBox.setObjectName('UrlTextBox')
        self.UrlTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.UrlTextBox.setPlaceholderText('Url Encode\n这里写明文')

        self.UrlCipherBox = uni_Widget.ICTFETextBox(self)
        self.UrlCipherBox.setObjectName('UrlCipherBox')
        self.UrlCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.UrlCipherBox.setPlaceholderText('Url Decode\n这里写编码')
        # end url panel
