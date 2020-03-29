from PyQt5 import QtCore, QtWidgets
from ui_Widgets import uni_Widget


class ui_HashPanel(QtWidgets.QWidget):
    def __init__(self):
        super(ui_HashPanel, self).__init__()

        # input text file button
        self.HashTextInputPath = ''
        self.HashTextInputButton = uni_Widget.ICTFEButton(self)
        self.HashTextInputButton.setObjectName('HashTextInputButton')
        self.HashTextInputButton.setGeometry(QtCore.QRect(20, 20, 120, 45))
        self.HashTextInputButton.setText('打开...')
        self.HashTextInputButton.setToolTip('点击选择文件')

        # Hash Encode button
        self.HashEncodeButton = uni_Widget.ICTFEButton(self)
        self.HashEncodeButton.setObjectName('HashEncodeButton')
        self.HashEncodeButton.setGeometry(
            QtCore.QRect(580, 20, 120, 45))
        self.HashEncodeButton.setText('计算')

        self.HashTextBox = uni_Widget.ICTFETextBox(self)
        self.HashTextBox.setObjectName('HashTextBox')
        self.HashTextBox.setGeometry(QtCore.QRect(20, 80, 680, 530))
        self.HashTextBox.setPlaceholderText('Hash Calculate\n这里写明文')

        self.HashValueBox = uni_Widget.ICTFELineBox(self)
        self.HashValueBox.setObjectName('HashValueBox')
        self.HashValueBox.setGeometry(QtCore.QRect(800, 80, 600, 45))


        self.MD5ValueBox = uni_Widget.ICTFELineBox(self)
        self.MD5ValueBox.setObjectName('MD5ValueBox')
        self.MD5ValueBox.setGeometry(QtCore.QRect(800, 145, 600, 45))

        self.SHA1ValueBox = uni_Widget.ICTFELineBox(self)
        self.SHA1ValueBox.setObjectName('SHA1ValueBox')
        self.SHA1ValueBox.setGeometry(QtCore.QRect(800, 210, 600, 45))

        self.SHA3ValueBox = uni_Widget.ICTFELineBox(self)
        self.SHA3ValueBox.setObjectName('SHA3ValueBox')
        self.SHA3ValueBox.setGeometry(QtCore.QRect(800, 275, 600, 45))

        self.SHA224ValueBox = uni_Widget.ICTFELineBox(self)
        self.SHA224ValueBox.setObjectName('SHA224ValueBox')
        self.SHA224ValueBox.setGeometry(QtCore.QRect(800, 340, 600, 45))

        self.SHA256ValueBox = uni_Widget.ICTFELineBox(self)
        self.SHA256ValueBox.setObjectName('SHA256ValueBox')
        self.SHA256ValueBox.setGeometry(QtCore.QRect(800, 405, 600, 45))

        self.SHA384ValueBox = uni_Widget.ICTFELineBox(self)
        self.SHA384ValueBox.setObjectName('SHA384ValueBox')
        self.SHA384ValueBox.setGeometry(QtCore.QRect(800, 470, 600, 45))

        self.SHA512ValueBox = uni_Widget.ICTFELineBox(self)
        self.SHA512ValueBox.setObjectName('SHA512ValueBox')
        self.SHA512ValueBox.setGeometry(QtCore.QRect(800, 535, 600, 45))

        # end Hash panel
