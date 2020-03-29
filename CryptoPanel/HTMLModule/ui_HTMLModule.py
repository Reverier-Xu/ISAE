from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_HTMLPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_HTMLPanel, self).__init__()
        
        # HTML Encode button
        self.HTMLEncodeButton = uni_Widget.ICTFEButton(self)
        self.HTMLEncodeButton.setObjectName('HTMLEncodeButton')
        self.HTMLEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.HTMLEncodeButton.setText('编码')

        # HTML Decode button
        self.HTMLDecodeButton = uni_Widget.ICTFEButton(self)
        self.HTMLDecodeButton.setObjectName('HTMLDecodeButton')
        self.HTMLDecodeButton.setGeometry(
            QtCore.QRect(1280, 20, 120, 45))
        self.HTMLDecodeButton.setText('解码')

        self.HTMLTextBox = uni_Widget.ICTFETextBox(self)
        self.HTMLTextBox.setObjectName('HTMLTextBox')
        self.HTMLTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.HTMLTextBox.setPlaceholderText('HTML Encode\n这里写明文')

        self.HTMLCipherBox = uni_Widget.ICTFETextBox(self)
        self.HTMLCipherBox.setObjectName('HTMLCipherBox')
        self.HTMLCipherBox.setGeometry(QtCore.QRect(720, 80, 680, 530))
        self.HTMLCipherBox.setPlaceholderText('HTML Decode\n这里写编码')
        # end HTML panel
